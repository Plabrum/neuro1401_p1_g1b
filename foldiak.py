
 # Implement Foldiak's (1991) learning rule and demonstrate how it learns a representation that
 # is invariant to translation. Compare to the standard Hebbian learning rule.
 
from time import sleep
import numpy as np
import os

# Empty frame
empty = [[0 for i in range(8)] for j in range(8)]
# Buffer holds frames from a sweep generation
buff = []

def loc_func1(i,j,k):
    return (j+k) == (i)

def loc_func2(i,j,k):
    return ((8-j)+k) == i

def loc_func3(i,j,k):
    return j == i

def loc_func4(i,j,k):
    return k==i


or_dict = {"0": np.array([0,0,0,0]), "bs": np.array([1,0,0,0]), "fs": np.array([0,1,0,0]),
        "vt": np.array([0,0,1,0]), "hz": np.array([0,0,0,1])}

char_dict = {"0": (" "+chr(183)+" "), "bs": " / ", "fs": " \ ", "vt": " - ", "hz": " | "}

to_or = {'[1. 0. 0. 0.]': "bs", '[0. 1. 0. 0.]': "fs", '[0. 0. 1. 0.]': "vt",
             '[0. 0. 0. 1.]': "hz"}

func_dict = {"bs": loc_func1, "fs": loc_func2,
        "vt": loc_func3, "hz": loc_func4}

sweep_length = {"bs": 16, "fs": 16, "vt": 8,
             "hz": 8}

# NEW Generate a moving lines in a direction
# Direction is string val
# Todo add a flattened array for training/predicting
def generate_sweep(direction):
    # add either 8 or 16 frames to the buffer
    for i in range(sweep_length[direction]):
            print_frame = []
            data_frame = []
            for j in range(8):
                print_row =[]
                for k in range(8):
                    if func_dict[direction](i,j,k):
                        data_frame.append(or_dict[direction])
                        print_row.append(char_dict[direction])
                    else:
                        data_frame.append(or_dict["0"])
                        print_row.append(char_dict["0"])
                print_frame.append(print_row)
                
            # flat dataframe should be a 256x1
            flat_data = np.array(data_frame).flatten()
            buff.append((print_frame, flat_data))
        # return length of sweep
    return sweep_length[direction]

def visualise_frame(print_frame, estimate):
    # Move terminal cursor
    print("\033[%d;%dH" % (0, 0))

    if estimate:
        # Green Coloring
        def c(string):
            return ('\033[92m' + string + '\033[0m')
    else:
        # Red Coloring
        def c(string):
            return ('\033[91m' + string + '\033[0m')
        
# Ok so each element of the print frame will be the orientation string,
# all that needs to happen here is the approriate colouring
    for row in print_frame:
        for element in row:
            if element != (" "+chr(183)+" "):
                print(c(element), end='')
            else:
                print(element, end='')

        print("")

# Foldiak model
class Foldiak_model():
    def __init__(self, w_init=None):
        if w_init is not None:
            self.W = w_init
        else:
            self.W = np.random.rand(256, 4)

    def fit(self, alpha, delta, iter):
        print("model fit!")

    def y_hat(self, x):
        # this needs to return an output vector with a single 1 in one spot (winner takes all)
        output_vec = np.zeros(4)
        output_vec[np.argmax(np.dot(x, self.W))] = 1
        # tiebreak senario
        return output_vec

    def predict(self, x):
        return to_or[str(self.y_hat(x))]

row1 = np.array([np.array([1,0,0,0]) for i in range(64)]).flatten()
row2 = np.array([np.array([0,1,0,0]) for i in range(64)]).flatten()
row3 = np.array([np.array([0,0,1,0]) for i in range(64)]).flatten()
row4 = np.array([np.array([0,0,0,1]) for i in range(64)]).flatten()
perfect_weights = np.array([row1, row2, row3, row4]).T

# Test the model
def test_foldiak():
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

    # create a foldiak model:
    model = Foldiak_model(w_init=perfect_weights)

    #### TRAINING ####
    alpha = 0.02
    delta = 0.2
    iterations = 500
    # This should take a learning rate, a number of iterations on which to train
    # model.fit(alpha, delta, iterations)


    #### TESTING #####
    # Loop through each of the four orientations
    for orientation in ['bs', 'fs', 'vt', 'hz']:
        # for each orientation generate a sweep and predict each frame
        for test_case in range(generate_sweep(orientation)):
            print_frame, data_frame = (buff.pop() if buff else empty)
            # Run the frame through the model and check if the prediction is correct
            # predict will probably produce a vector so we'll need some kind of string lookup for this
            accuracy = (model.predict(data_frame) == orientation)

            # draw the frame coloring for the prediction accuracy
            visualise_frame(print_frame, accuracy)
            sleep(0.25)

'''
TODO:

* change to a 32 by 8 frame (for each orientation)
* make sweep length uniform for all directions (think this may not matter)
* figure out the weights required and the training relationship
* 

Add second direction for sweeps, 

'''
test_foldiak()
