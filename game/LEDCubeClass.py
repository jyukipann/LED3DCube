import numpy as np
import threading as thread

class Color:
	def __init__(self,R,G,B):
		self.setColor(R,G,B)

	def setColor(self,R,G,B):
		#int 0 <= R,G,B, <= 255
		self.R = R
		self.G = G
		self.B = B
	
	def __list__(self):
		return [self.R,self.G,self.B]
	
	def getColor(self):
		return np.ndarray(list(self))

class LED_Cube:
	def __init__(self,n=5):
		self.n = 5
		self.cube = np.zeros((self.n,self.n,self.n,3))

	def __reset__(self):
		self.cube = np.zeros((self.n,self.n,self.n,3))
	
	def set_color(self,x,y,z,color):
		#int x,y,z >= 0 and color isInstans(Color)
		self.cube[x,y,z] = color.getColor()

	def output(self):
		pass

	def __str__(self):
		return str(self.cube)


class gobang:
	def __init__(self,n=5):
		self.n = n
		self.dir = [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,1],[1,1,1]]
		self.cube = None
		self.reset_cube()
		self.p1 = ""
		self.p2 = ""

	def reset_cube(self):
		self.cube = np.zeros((self.n,self.n,self.n))
		
	def set_player(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def isfinish(self):
		#スレッドを用いて並行して、一列揃っているところを探す。
		pass

	def start_game(self):
		self.reset_cube()
		if(self.p1 == "" or self.p2 == ""):
			return
		#start
		#p1
		#isfinish
		#p2
		#isfinish

	
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
	five = gobang()
	five.printCube()
	