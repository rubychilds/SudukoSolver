import numpy as np
import scipy as sp

# creation of all permutations

# creates identity matrix
identity = sp.diag((1,1,1))
# OR...
ident = sp.identity(3).todense()

PERMUTATION1 = np.array( [[0 , 1 , 0] , [ 1, 0, 0 ], [ 0, 0, 1]])
PERMUTATION2 = np.array( [[0 , 1 , 0 ],  [0, 0, 1], [1, 0, 0]])
PERMUTATION4 = np.array( [[0 , 0 , 1],  [0, 1, 0], [1, 0, 0]])
PERMUTATION5 = np.array( [[0 , 0 , 1],  [1, 0, 0], [0, 1, 0]])
PERMUTATION6 = np.array( [[1 , 0 , 0 ],  [0, 0, 1], [0, 1, 0]])

# array list storing all permutations
Pemutations = [PERMUTATION1, PERMUTATION2, PERMUTATION4, PERMUTATION5, PERMUTATION6]

# difficulty upper and lower bounds
DifficultyVEasy = [2, 1.6]
DifficultyEasy = [1.6 , 1.2]
DifficultyMedium = [1.2 , 0.8]
DifficultyHard = [0.8, 0.5576923]

class generator:

	__init__(self):

		perms = []
		for i in itertools.permutations(range(1,10)):
			perms += i

		current_perm = perms[np.random.randint(len(h))]

		np.reshape(current_perm, [3,3])

		

		rand1 = randint(1,permutations.length)
		rand2 = randint(1,permutations.length)

		## checks they are not the same
		while rand1 == rand2:
			rand2 = np.random.randint(1,permutations.length)
			
		B1 = current_perm

		# Ensure we select two random permutations
		perm1 = Pemutations[rand1]
		perm2 = Pemutations[rand2]

		# now do the permutations
		B2 = np.dot( perm1, B1)
		B3 = np.dot( perm2,B1)

		B4 = np.dot(B1, perm2)
		B5 = np.dot(np.dot(perm1, B1), perm2)
		B6 = np.dot(np.dot(perm2, B1), perm2)

		B7 = np.dot( B1, perm1)
		B8 = np.dot(np.dot( perm1, B1), perm1)
		B9 = np.dot(np.dot( perm2, B1), perm1)

		currentP = [B1,B2,B3,B4,B5,B6,B7,B8,B9]

		self.sudoko = np.reshape(currentP, [9,9])
		self.sudokoElim = self.sudoko
		
		print B1, B2, B3
		print B4, B5, B6
		print B7, B8, B9

		print sudoko


	def elimination(selectedDifficulty):
		# passes in level of difficulty desired
		constraints = []

		if selectedDifficulty == "DifficultyVEasy":
			constraints = DifficultyVEasy
		elif selectedDifficulty == "DifficultyEasy"
			constraints = DifficultyEasy
		elif selectedDifficulty == "DifficultyMedium"
			constraints = DifficultyMedium
		elif selectedDifficulty == "DifficultyHard"
			constraints = DifficultyHard






if __name__ == "__main__":
	generator()













