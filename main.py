import gym

env = gym.make('SpaceInvaders-v0')

done = False
moves = 0

observation = env.reset()

while not done:
    env.render()

    moves += 1

    action = env.action_space.sample()

    observation, reward, done, _ = env.step(action)

    if done:
        break

print('game lasted ', moves, " moves\n\n\n\n")

