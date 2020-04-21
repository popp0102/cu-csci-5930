import pdb
import random
from pathlib import Path
import numpy as np
from .agent import Agent
from .memory import Memory
from .deep_q_neural_network import DeepQNeuralNetwork

NUM_FRAMES = 4

class SpaceInvadersAgent(Agent):
    def __init__(self, cwd, num_actions, alpha, epsilon, epsilon_min, epsilon_drop, gamma, fc_num_neurons, memory_capacity, batch_size, update_weights_threshold):
        super().__init__(num_actions)

        self.epsilon      = epsilon
        self.epsilon_min  = epsilon_min
        self.epsilon_drop = epsilon_drop
        self.gamma        = gamma
        self.memory       = Memory(memory_capacity, batch_size)

        self.batch_size               = batch_size
        self.learn_step               = 0
        self.update_weights_threshold = update_weights_threshold
        self.loss                     = -1

        self.policy_path    = "{}/policy.h".format(cwd)
        self.target_path    = "{}/target.h".format(cwd)
        self.policy_network = DeepQNeuralNetwork(num_actions, alpha, fc_num_neurons)
        self.target_network = DeepQNeuralNetwork(num_actions, alpha, fc_num_neurons)

    def select_action(self, state, env):
        action = None
        if random.uniform(0,1) < self.epsilon:
            action = self.take_random_action()
        else:
            action_q_values = self.policy_network.model.predict(state.reshape(1,84,84,NUM_FRAMES))
            action          = np.argmax(action_q_values)

        return action

    def remember(self, state, new_state, reward, action, done):
        self.memory.memorize(state, new_state, reward, action, done) # this is an experience

    def memory_is_full(self):
        return self.memory.is_full()

    def load_networks(self):
        path_policy = Path(self.policy_path)
        path_target = Path(self.target_path)

        if path_policy.exists() and path_target.exists():
            print("!!! Loading existing models !!!")
            self.policy_network.load(self.policy_path)
            self.target_network.load(self.target_path)
        else:
            print("!!! Warning - not loading models as they don't exist !!!")

    def save_networks(self):
        self.policy_network.save(self.policy_path)
        self.target_network.save(self.target_path)

    def train(self, episode):
        self.learn_step += 1

        if self.learn_step >= self.update_weights_threshold:
            self.learn_step = 0
            policy_weights  = self.policy_network.model.get_weights()
            self.target_network.model.set_weights(policy_weights)

        experiences = self.memory.recall()

        states      = experiences["states"]
        next_states = experiences["next_states"]
        rewards     = experiences["rewards"]
        actions     = experiences["actions"]
        dones       = experiences["dones"]

        targets = np.zeros((self.batch_size, self.num_actions))
        for i in range(self.batch_size):
            q_values               = self.policy_network.model.predict(states[i].reshape(1,84,84,NUM_FRAMES))
            q_next_values          = self.target_network.model.predict(next_states[i].reshape(1,84,84,NUM_FRAMES))
            if self.learn_step % 50 == 0 and i == 0:
                print("state: ", q_values.tolist(), "next: ", q_next_values.tolist())
            targets[i]             = q_values[:]
            targets[i, actions[i]] = rewards[i] + self.gamma*np.max(q_next_values, axis=1)*(1-dones[i]) # Bellman Equation

        self.loss = self.policy_network.model.train_on_batch(states, targets) # update weights

        self.epsilon = self.epsilon - self.epsilon_drop
        if self.epsilon < self.epsilon_min:
            self.epsilon = self.epsilon_min

