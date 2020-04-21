import sys
import argparse

def cmd_parse(argv):
    parser    = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    train_parser   = subparser.add_parser("train")
    analyze_parser = subparser.add_parser("analyze")
    record_parser  = subparser.add_parser("record")

    train_parser.add_argument("-e", "--episodes", help="number of episodes to run during training", type=int, default=100)
    train_parser.add_argument("-s", "--season", help="season number used to store training results", type=int, default=1)
    analyze_parser.add_argument("-e", "--episodes", help="number of episodes to run", type=int, default=100)
    analyze_parser.add_argument("-s", "--season", help="season number used to store run results", type=int, default=1)
    record_parser.add_argument("-s", "--season", help="which season to record", type=int, default=1)

    args    = parser.parse_args()
    command = args.command
    if command == 'train' or command == 'analyze':
        episodes = args.episodes
    elif command == 'record':
        episodes = None
    else:
        parser.print_help()
        sys.exit(0)

    return (command, episodes, args.season)

