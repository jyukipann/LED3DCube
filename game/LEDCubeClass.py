import numpy as np
import threading as thread

class Color:
	def __init__(self,R,G,B):
		self.setColor(R,G,B)

	def setColor(self,R,G,B):
		#int 0 <= R,G,B, <= 255
		try:
			self.R = int(R)
			self.G = int(G)
			self.B = int(B)
			if(0 <= self.R <= 255 and 0 <= self.G <= 255 and 0 <= self.B <= 255):
				return True
			else:
				raise ValueError(int)
		except:
			self.R = 0
			self.G = 0
			self.B = 0
			return False

	def getColor(self):
		return np.array([self.R,self.G,self.B])

class LED_Cube:
	def __init__(self,n=5):
		self.n = 5
		self.cube = np.zeros((self.n,self.n,self.n,3))

	def __reset__(self):
		self.cube = np.zeros((self.n,self.n,self.n,3))
	
	def set_color(self,x,y,z,color):
		#int 0 <= x,y,z < self.n and color isInstans(Color)
		if(isinstance(x,int) and isinstance(y,int) and isinstance(z,int), isinstance(color,Color)):
			if(0 <= x < self.n and 0 <= y < self.n and 0 <= z < self.n):
				self.cube[x,y,z] = color.getColor()
				return True
		else:
			return False
		
	"""
	def __setitem__(self,xyz,color):
	"""

	def __getitem__(self,key):
		return self.cube[key]


	def output(self):
		#転置必要
		print(str(self))

	def __str__(self):
		return str(self.cube)


class gobang3d(LED_Cube):
	def __init__(self,n=5, p1="player1", p2="player2",c1=(255,0,0),c2=(0,255,0)):
		super(gobang3d,self).__init__(n=5)
		self.dir = [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,1],[1,1,1]]
		self.players = {p1:Color(*c1),p2:Color(*c2)}
		
	def set_player(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def isfinish(self,x,y,z):
		#スレッドを用いて並行して、一列揃っているところを探す。
		now_x = x
		now_y = y
		now_z = z
		color = self.cube[x,y,z]
		for dir in self.dir:
			count = 1
			while(0 <= now_x+dir[0] < self.n and 0 <= now_y+dir[1] < self.n and 0 <= now_z+dir[2] < self.n):
				now_x += dir[0]
				now_y += dir[1]
				now_z += dir[2]
				if(color == self.cube[now_x,now_y,now_z]):
					count +=1
				else:
					break
			while(0 <= now_x-dir[0] < self.n and 0 <= now_y-dir[1] < self.n and 0 <= now_z-dir[2] < self.n):
				now_x -= dir[0]
				now_y -= dir[1]
				now_z -= dir[2]
				if(color == self.cube[now_x,now_y,now_z]):
					count +=1
				else:
					break
			if(count == self.n):
				return True
			else:
				return False

	def getSelected(self,x,y,z,player):
		color = None
		try:
			color = self.players[player]
		except:
			return False
		try:
			if(self.cube[x,y,z] == color.getColor()):
				self.setColor(x,y,z,color)
				return True
		except:
			return False
		return False

	def start_game(self):
		self.__reset__()
		#start
		while True:
			for player in self.players:
				x,y,z = 0,0,0
				while(True):
					x, y, z, *_ = list(map(int,input().split()))
					if not self.getSelected(x,y,z,self.players[player]):
						break
				if(self.isfinish(x,y,z)):
					self.win(player)
					return


	def win(self,player):
		print("win :",player)

	
	def lightUp(self,x,y,z,color):
		try:
			x = int(x)
			y = int(y)
			z = int(z)
		except:
			return None
		if(self.cube[x,y,z] == 0):
			self.cube[x,y,z]
			return True
		else:
			return False
		
	def printCube(self):
		print(self.cube)

if __name__ == "__main__":
	#five = gobang()
	#five.printCube()
	c = Color(3,5,7)
	cube = LED_Cube(2)
	#print(cube)
	cube.set_color(0,0,0,c)
	print(cube[0,0,0])

	