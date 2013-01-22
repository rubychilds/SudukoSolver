import numpy as np

# http://stattrek.com/matrix-algebra/elementary-operations.aspx


PERMUTATION1 = np.array( [[0 , 1 , 0] , [ 1, 0, 0 ], [ 0, 0, 1]])
PERMUTATION2 = np.array( [[0 , 1 , 0 ],  [0, 0, 1], [1, 0, 0]])
PERMUTATION3 = np.array( [[1, 0, 0 ], [0 , 1 , 0 ], [0, 0, 1]])
PERMUTATION4 = np.array( [[0 , 0 , 1],  [0, 1, 0], [1, 0, 0]])
PERMUTATION5 = np.array( [[0 , 0 , 1],  [1, 0, 0], [0, 1, 0]])
PERMUTATION6 = np.array( [[1 , 0 , 0 ],  [0, 0, 1], [0, 1, 0]])

MAINARRAY = array()

def generator:

	__init__(self):

		perms = []
		for i in itertools.permutations(range(1,10)):
			perms += i

		current_perm = perms[np.random.randint(len(h))]

		np.reshape(current_perm, [3,3])


		# now do the permutations
		
		B3 = np.dot( PERMUTATION2,B1)
		B4 = np.dot(B1, PERMUTATION2)
		

		B9 = np.dot(np.dot(PERMUTATION2,B1),PERMUTATION5)

















