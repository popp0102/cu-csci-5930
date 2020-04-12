# 5930-final-project
Reinforcement learning with Space Invaders and Open AI Gym

# Author
Jason Poppler

# Setup and Installation
1. python3 -m venv ./venv
2. source venv/bin/activate
3. pip install -r requirements.txt

# Running the Project
main.py is the primary executable for the project. It has 3 optins you can pass it:

## train
The train command will train the agent for however many episodes passed in. You also specify a "season". The season is an integer that will basically be a container for storing the data and results. A training.json file is saved into the runs/<game>/<season> directory.

## analyze
The analyze command will run the trained agent (or untrained if training.json doesn't exist) for the specified season. You pass in the number of episodes and this will create a digest.json file. The digest.json file keeps track of all of the moves and rewards for the episode. In addition it will create two image files of graphs: scores_vs_episodes.png and moves_vs_episodes.png.  

## watch
The watch command will allow you to watch agent play whatever game it trained for. Note the window will terminate when the agent either won or loss. If the agent does so quickly then you may not see the game played for very long.

# Runs
This section will describe the runs made for various games.

## CartPole-v0
The point of this game is to balance a pole on a cart. The agent can move the cart left or right. See https://gym.openai.com/envs/CartPole-v0/ for details.

### Season 1
The following commands were run from the repos primary directory:
```
./main.py analyze -s 1 -e 100
./main.py watch -s 1
```
This season the model wasn't trained and therefore had varying results.

### Season 2
The following commands were run from the repos primary directory:
```
./main.py train -s 2 -e 1000
./main.py analyze -s 2 -e 1000
./main.py watch -s 2
```
This season the model was trained and was able to get the max reward of 200.

### Running Manually
If you would like to run a version of this agent you need to make a couple code changes in the main.py file:

1. Ensure the Cart Pole Agent is being imported:
```
from lib.cart_pole_agent     import CartPoleAgent
```

2. Set the game to be Cart Pole:
```
ATARI_GAME = 'CartPole-v0'
```

3. Set the agent to be th CartPoleAgent:
```
agent = CartPoleAgent(env.action_space.n)
```
4. Invoke any train, analyze or watch command. Be sure to specify a different season than one that already exists.
