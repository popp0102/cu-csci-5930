from keras.models import Sequential
from keras.layers import Conv2D

class DeepQNeuralNetwork(object):
    def __init__(self, num_actions, alpha=0.001, num_neurons=256):
        # Layers to the Deep Q Network
        conv_layer_1   = Conv2D(filters=16, kernel_size=8, strides=4, activation="relu", data_format="channels_first")
        conv_layer_2   = Conv2D(filters=32, kernel_size=4, strides=2, activation="relu", data_format="channels_first")
        hidden_layer_1 = Dense(num_neurons, activation="relu")
        output_layer   = Dense(num_actions, activation="relu")

        # Build the Deep Q Network Model
        self.model = Sequential()
        self.model.add(conv_layer_1)
        self.model.add(conv_layer_2)
        self.model.add(Flatten())
        self.model.add(hidden_layer_1)
        self.model.add(output_layer)

        # stochastic gradient descent optimizer
        self.model.compile(optimizer=Adam(learning_rate=alpha, loss="mean_squared_error")

