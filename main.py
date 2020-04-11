import pdb
import gym
from lib.random_agent import RandomAgent
from lib.game_master  import GameMaster
from lib.analyzer     import Analyzer

ATARI_GAME   = 'SpaceInvaders-v0'
RUN_NAME     = 'random_agent'
NUM_EPISODES = 50

def main():
    analyzer    = Analyzer(RUN_NAME)
    env         = gym.make(ATARI_GAME)
    agent       = RandomAgent(env.action_space.n)
    game_master = GameMaster(env, agent)
    digest      = game_master.run_season(RUN_NAME, NUM_EPISODES, render=False)
    analyzer.run(digest)

main()

