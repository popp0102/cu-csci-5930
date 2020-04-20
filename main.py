#!./venv/bin/python

import sys
import gym
from lib.agent.space_invaders_agent import SpaceInvadersAgent
from lib.file_manager               import FileManager
from lib.game_master                import GameMaster
from lib.analyzer                   import Analyzer
from lib.command_line_parser        import cmd_parse

# Hyperparameters
ATARI_GAME      = 'SpaceInvaders-v0'
ALPHA           = 0.001
EPSILON         = 1.0
GAMMA           = 0.95
FC_NUM_NEURONS  = 256
MEMORY_CAPACITY = 50000
RECALL_SIZE     = 32
UPDATE_WEIGHTS  = 1000

def main(argv):
    (command, episodes, season) = cmd_parse(argv)

    file_manager = FileManager(ATARI_GAME, season)
    env          = gym.make(ATARI_GAME)
    agent        = SpaceInvadersAgent(env.action_space.n, ALPHA, EPSILON, GAMMA, FC_NUM_NEURONS, MEMORY_CAPACITY, RECALL_SIZE, UPDATE_WEIGHTS)
    game_master  = GameMaster(env, agent)
    #analyzer     = Analyzer(file_manager.cwd)

    if command == 'train':
        game_master.run_season(episodes, training=True, render=False)

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

