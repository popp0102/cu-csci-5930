#!./venv/bin/python

import sys
import gym
from lib.file_manager         import FileManager
from lib.cart_pole_agent      import CartPoleAgent
from lib.space_invaders_agent import SpaceInvadersAgent
from lib.game_master          import GameMaster
from lib.analyzer             import Analyzer
from lib.command_line_parser  import cmd_parse

ATARI_GAME = 'SpaceInvaders-v0'

def main(argv):
    (command, episodes, season) = cmd_parse(argv)

    file_manager = FileManager(ATARI_GAME, season)
    env          = gym.make(ATARI_GAME)
    agent        = SpaceInvadersAgent(env.action_space.n)
    game_master  = GameMaster(env, agent)
    analyzer     = Analyzer(file_manager.cwd)

    if command == 'train':
        agent.train(env, episodes)
        file_manager.save(agent.save(), 'training.json')
    elif command == 'analyze':
        agent.load(file_manager.load('training.json'))
        digest = game_master.run_season(episodes)
        file_manager.save(digest.facts, 'digest.json')
        analyzer.create_graphs(digest)
    elif command == 'watch':
        agent.load(file_manager.load('training.json'))
        game_master.run_episode(render=True)

    env.close()

if __name__ == "__main__":
    main(sys.argv[1:])

