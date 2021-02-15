from numpy import random


test = [[[1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]],

        [[0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]],

        [[0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]
        ]


# simple neurons
def simple(inarray, y, x):
        if inarray[y][x] == 0:  # " "+chr(183)+" "
                output = 0
        else:
                output = 1
        return output


s = []
# define all the simple neurons and store them in a list?
for i in test:
        for y in range(8):
                for x in range(8):
                        s.append(simple(i, y, x))

# define initial weights:
w = random.uniform(0, 0.1, size=(4, 64))
print(w)


# function to update connections
def updateconect(t, j, i):
        if t == 0:
                return w[j][i]
        else:
                return 1
print(updateconect(0, 0, 0))

# define the complex neurons
# def complex(outarray):
#     for i in range(64*4):



# r = Net()
# def complex(simparray):