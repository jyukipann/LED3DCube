import numpy as np
mat5 = np.zeros((5,5,5,3),dtype=int)
f = np.array([0,255,0])
u = np.array([255,255,255])
d = np.array([244,213,0])
r = np.array([255,0,0])
l = np.array([255,165,0])
b = np.array([0,0,255])
mat5[0:1,1:4,1:4] = d
#print(mat5)
m2s = np.array(
	[[[  4,   3 ,  2 ,  1 ,  0],
	[  5  , 6 ,  7  , 8  , 9],
	[ 14 , 13 , 12,  11 , 10],
	[ 15 , 16,  17 , 18,  19],
	[ 24 , 23,  22,  21  ,20],],

	[[ 45 , 46 , 47,  48  ,49],
	[ 44 , 43 , 42,  41 , 40],
	[ 35 , 36  ,37 , 38,  39],
	[ 34,  33 , 32 , 31 , 30],
	[ 25,  26 , 27  ,28 , 29],],

	[[ 54  ,53 , 52,  51 , 50],
	[ 55 , 56,  57 , 58 , 59],
	[ 64,  63,  62 , 61 , 60],
	[ 65,  66 , 67 , 68  ,69],
	[ 74  ,73,  72  ,71  ,70],],

	[[ 95  ,96 , 97 , 98  ,99],
	[ 94 , 93 , 92 , 91  ,90],
	[ 85 , 86 , 87 , 88 , 89],
	[ 84 , 83 , 82 , 81 , 80],
	[ 75  ,76  ,77 , 78,  79],],

	[[104, 103, 102 ,101 ,100],
	[105, 106 ,107 ,108 ,109],
	[114 ,113 ,112 ,111 ,110],
	[115 ,116, 117, 118, 119],
	[124, 123, 122, 121, 120],]]
)
import time, random
def flying_bee(strip,color,wait_ms=60):
	global m2s
	dir = [-1,0,1]
	pos = [3,3,3]
	mat5 = np.zeros((5,5,5,3),dtype=int)
	#strip.setPixelColor(m2s[*pos],mat5[*pos])
	#strip.show()
	time.sleep(wait_ms/1000.0)
	for i in range(100):
		nextPos = pos
		nextPos[0] += random.choice(dir)
		nextPos[1] += random.choice(dir)
		nextPos[2] += random.choice(dir)
		for j in range(3):
			if(nextPos[j] < 0):
				nextPos[j] = 0
			if(nextPos[j] >= 5):
				nextPos[j] = 4
		pos = nextPos
		#strip.setPixelColor(m2s[*pos],mat5[*pos])
		#strip.show()
		time.sleep(wait_ms/1000.0)
		print(*pos)

flying_bee(1,225)