import gym
from lib.random_agent import RandomAgent
from lib.game_master  import GameMaster
from lib.analyzer     import Analyzer

ATARI_GAME   = 'SpaceInvaders-v0'
AGENT        = 'random_agent'
SEASON       = "season_1"
NUM_EPISODES = 50

def main():
    analyzer    = Analyzer(AGENT, SEASON)
    env         = gym.make(ATARI_GAME)
    agent       = RandomAgent(env.action_space.n)
    game_master = GameMaster(env, agent)
    digest      = game_master.run_season(SEASON, NUM_EPISODES, render=False)
    analyzer.run(digest)

main()

