
 # Implement Foldiak's (1991) learning rule and demonstrate how it learns a representation that
 # is invariant to translation. Compare to the standard Hebbian learning rule.
 
from time import sleep
import os

# Empty frame
empty = [[0 for i in range(8)] for j in range(8)]
# Buffer holds frames from a sweep generation
buff = []

# Generate a moving lines in a direction
def generate_sweep(direction):
	# generate 16 frames for a diagonal direction

	if direction == 0:
		orientation_val = 1
		sweep_length = 16
		def loc_func(i,j,k):
			return (j+k) == (i)
	elif direction == 1:
		orientation_val = 2
		sweep_length = 16
		def loc_func(i,j,k):
			return ((8-j)+k) == i
	elif direction == 2:
		orientation_val = 3
		sweep_length = 8
		def loc_func(i,j,k):
			return j == i
	elif direction == 3:
		orientation_val = 4
		sweep_length = 8
		def loc_func(i,j,k):
			return k==i

	# add either 8 or 16 frames to the buffer
	for i in range(sweep_length):
			frame = []
			for j in range(8):
				row =[]
				for k in range(8):
					if loc_func(i,j,k):
						row.append(orientation_val)
					else:
						row.append(0)
				frame.append(row)
			buff.append(frame)
		# return length of sweep
	return sweep_length

def visualise_frame(frame, estimate):
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
	# take a frame and print it out:
	char_dict = {1: " / ", 2: " \ ", 3: " - ", 4: " | "}
	z = " "+chr(183)+" "

	for i in frame:
		for j in i:
			if j == 0: 
				print(z, end='')
			else:
				print(c(char_dict[j]), end='')
		print("")

# Foldiak model
class Foldiak_model():
	def __init__(self):
		# TODO
		self.simple_weights = []
		self.complex_weights = []

	def fit(self, alpha, delta, iter):
		print("model fit!")
	
	def predict(self, frame):
		# TODO
		return 3

# Test the model
def test_foldiak():
	# Clear the terminal
	os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

	# create a foldiak model:
	model = Foldiak_model()

	#### TRAINING ####
	alpha = 0.02
	delta = 0.2
	# This should take a learning rate, a number of iterations on which to train
	model.fit(alpha, delta, iterations)


	# For reference
	# orientation_dictionary = {0: "bs", 1: "fs", 2: "vt", 3: "hz"}
	
	#### TESTING #####
	# Loop through each of the four orientations
	for orientation in [0,1,2,3]:
		# for each orientation generate a sweep and predict each frame
		for test_case in range(generate_sweep(orientation)):
			frame = (buff.pop() if buff else empty)
			# Run the frame through the model and check if the prediction is correct
			accuracy = (model.predict(frame) == orientation)

			# draw the frame coloring for the prediction accuracy
			visualise_frame(frame, accuracy)
			sleep(0.25)
	
test_foldiak()	

'''
	TODO:
	Add second direction for sweeps, change to a 32 by 8 frame (for each orientation)
	make sweep length uniform for all directions
'''

