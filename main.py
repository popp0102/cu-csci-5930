import sys
import pdb
import gym
from lib.random_agent        import RandomAgent
from lib.game_master         import GameMaster
from lib.analyzer            import Analyzer
from lib.command_line_parser import cmd_parse

#ATARI_GAME = 'SpaceInvaders-v0'
ATARI_GAME = 'CartPole-v0'

def main(argv):
    (command, episodes, season) = cmd_parse(argv)

    env         = gym.make(ATARI_GAME)
    agent       = RandomAgent(env.action_space.n)
    workdir     = "{}/{}/{}".format("runs", agent.type(), season)
    game_master = GameMaster(env, agent)
    analyzer    = Analyzer(ATARI_GAME, agent.type(), season)

    if command == 'train':
        agent.train(env, episodes)
    elif command == 'analyze':
        print("ANALYZING AGENT, season: {}, episodes: {}".format(season, episodes))
        #digest = game_master.run_season(season, episodes)
        #analyzer.run(digest)
    elif command == 'watch':
        print("WATCHING AGENT, season: {}, episodes: {}".format(season, episodes))
        #game_master.watch_game(season)

    env.close()

if __name__ == "__main__":
    main(sys.argv[1:])

