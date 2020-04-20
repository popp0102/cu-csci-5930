from keras.models     import Sequential
from keras.layers     import Conv2D, Dense, Flatten
from keras.optimizers import Adam
import pdb

class DeepQNeuralNetwork(object):
    def __init__(self, num_actions, alpha, fc_num_neurons):
        # Layers to the Deep Q Network
        conv_layer_1   = Conv2D(filters=16, kernel_size=8, strides=4, activation="relu", data_format="channels_last", input_shape=(210,160,3))
        conv_layer_2   = Conv2D(filters=32, kernel_size=4, strides=2, activation="relu", data_format="channels_last")
        hidden_layer_1 = Dense(fc_num_neurons, activation="relu")
        output_layer   = Dense(num_actions, activation="relu")

        # Build the Deep Q Network Model
        self.model = Sequential()
        self.model.add(conv_layer_1)
        self.model.add(conv_layer_2)
        self.model.add(Flatten())
        self.model.add(hidden_layer_1)
        self.model.add(output_layer)

        # stochastic gradient descent optimizer
        self.model.compile(optimizer=Adam(learning_rate=alpha), loss="mean_squared_error")

    def model(self):
        return self.model
