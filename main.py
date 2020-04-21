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
    "epsilon_min": 0.05,
    "epsilon_drop": 0.0001,
    "gamma": 0.99,
    "num_neurons": 512,
    "mem_cap": 10000,
    "recall_size": 32,
    "update_weight_freq": 1000
}

def main(argv):
    (command, episodes, season) = cmd_parse(argv)

    file_manager = FileManager(HP["game"], season)
    env          = gym.make(HP["game"])
    if command == 'record':
        env = gym.wrappers.Monitor(env, "{}/recording".format(file_manager.cwd),force=True)
    agent        = SpaceInvadersAgent(file_manager.cwd, env.action_space.n, HP["alpha"], HP["epsilon"], HP["epsilon_min"], HP["epsilon_drop"],
                                                                            HP["gamma"], HP["num_neurons"], HP["mem_cap"], HP["recall_size"],
                                                                            HP["update_weight_freq"])
    game_master  = GameMaster(env, agent)
    analyzer     = Analyzer(file_manager.cwd)

    if command == 'train':
        training_digest = game_master.run_season(season, episodes, training=True)
        file_manager.save(training_digest.facts, 'analysis.json')
        file_manager.save(HP, 'hyperparameters.json')
        analyzer.create_graphs(training_digest, 'training')
    elif command == 'analyze':
        digest = game_master.run_season(season, episodes, training=False)
        file_manager.save(digest.facts, 'analyze.json')
        analyzer.create_graphs(digest, 'analyze')
    elif command == 'record':
        digest = game_master.run_season(season, 1, training=False)

    env.close()

if __name__ == "__main__":
    main(sys.argv[1:])

