'''
 Implement Foldiak’s (1991) learning rule and demonstrate how it learns a representation that
 is invariant to translation. Compare to the standard Hebbian learning rule.
 '''
from time import sleep
import os
#  Example line:
# [
# [-, -, -, *, -, -, -, -, -],
# [-, -, *, -, -, -, -, -, -],
# [-, *, -, -, -, -, -, -, -],
# [*, -, -, -, -, -, -, -, -],
# [-, -, -, -, -, -, -, -, -],
# [-, -, -, -, -, -, -, -, -],
# [-, -, -, -, -, -, -, -, -],
# [-, -, -, -, -, -, -, -, -]
# ]

empty = [[0 for i in range(8)] for j in range(8)]

# Buffer length will be 8 frames long (completes a full sweep)
buff = []

def pretty(frame, num=False):
	# take a frame and print it out:
	z, o = " - ", " * "
	if num:
		z, o = " 0 ", " 1 "
	for i in frame:
		for j in i:
			if j == 0: 
				print(z, end="")
			else:
				print(o, end="")
		print("")

# Generate a moving lines in a direction
def generate_sweep(direction):
	# generate 16 frames for a diagonal direction
	if direction == "bs":
		for i in range(16):
			frame = []
			for j in range(8):
				row =[]
				for k in range(8):
					if (j+k) == (i) :
						row.append(1)
					else:
						row.append(0)
				frame.append(row)
			buff.append(frame)
		# return length of sweep
		return 16

	if direction == "fs":
		for i in range(16):
			frame = []
			for j in range(8):
				row =[]
				for k in range(8):
					if (j+k) == (i) :
						row.append(1)
					else:
						row.append(0)
				frame.append(row)
			buff.append(frame)


def visualise_frame(frame):
	# Move terminal cursor
	print("\033[%d;%dH" % (0, 0))
	pretty(frame)

# Store model

# Train model

# Test the model
def test_foldiak():
	return True

# Clear the terminal
# print("\033c\033[3J", end='')
# print("\033c", end='')
os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

for i in range(generate_sweep("bs")):
	frame = (buff.pop() if buff else empty)
	visualise_frame(frame)
	sleep(0.5)
