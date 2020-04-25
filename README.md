# 5930-final-project
Reinforcement learning with Space Invaders

# Author
Jason Poppler

# Setup and Installation
1. python3 -m venv ./venv
2. source venv/bin/activate
3. pip install -r requirements.txt

## Install CUDA
Go here to install CUDA: https://developer.nvidia.com/cuda-zone

# Running the Project
main.py is the primary executable for the project. It has 3 optins you can pass it:

## train
The train command will train the agent for however many episodes passed in. You also specify a "season". The season is an integer that will basically be a container for storing the data and results. A training.json file is saved into the runs/<game>/<season> directory.

## analyze
The analyze command will run the trained agent (or untrained if training.json doesn't exist) for the specified season. You pass in the number of episodes and this will create a digest.json file. The digest.json file keeps track of all of the moves and rewards for the episode. In addition it will create two image files of graphs: scores_vs_episodes.png and moves_vs_episodes.png.  

## record
The record command will allow you to record an agent play whatever game it trained for. Once the game has finished you it will create an mp4 file that can be viewed.
