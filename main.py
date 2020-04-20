#!./venv/bin/python

import sys
import gym
from lib.agent.space_invaders_agent import SpaceInvadersAgent
from lib.file_manager               import FileManager
from lib.game_master                import GameMaster
from lib.analyzer                   import Analyzer
from lib.command_line_parser        import cmd_parse

# Hyperparameters
HP = {
    "game": "SpaceInvaders-v0",
    "alpha" : 0.001,
    "epsilon": 1.0,
    "epsilon_min": 0.5,
    "epsilon_drop": 0.0001,
    "gamma": 0.95,
    "num_neurons": 256,
    "mem_cap": 50000,
    "recall_size": 32,
    "update_weight_freq": 1000
}

def main(argv):
    (command, episodes, season) = cmd_parse(argv)

    file_manager = FileManager(HP["game"], season)
    env          = gym.make(HP["game"])
    agent        = SpaceInvadersAgent(file_manager.cwd, env.action_space.n, HP["alpha"], HP["epsilon"], HP["epsilon_min"], HP["epsilon_drop"],
                                                                            HP["gamma"], HP["num_neurons"], HP["mem_cap"], HP["recall_size"],
                                                                            HP["update_weight_freq"])
    game_master  = GameMaster(env, agent)
    analyzer     = Analyzer(file_manager.cwd)

    if command == 'train':
        game_master.run_season(season, episodes, training=True, render=False)
        file_manager.save(HP, 'hyperparameters.json')

    # elif command == 'analyze':
    #     agent.load(file_manager.load('training.json'))
    #     digest = game_master.run_season(episodes)
    #     file_manager.save(digest.facts, 'digest.json')
    #     analyzer.create_graphs(digest)
    # elif command == 'watch':
    #     agent.load(file_manager.load('training.json'))
    #     game_master.run_episode(render=True)

    env.close()

if __name__ == "__main__":
    main(sys.argv[1:])

