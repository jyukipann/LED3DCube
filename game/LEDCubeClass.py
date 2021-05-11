import numpy as np
import threading as thread
import tkinter as tk
from tkinter import messagebox as mg

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
		return np.array([self.R,self.G,self.B],dtype="i2")

	def getCode(self):
		#print("getCode")
		if(self.R == 0 and self.G == 0 and self.B == 0):
			return ""
		#print("#"+str(hex(self.R))[2:]+str(hex(self.G))[2:]+str(hex(self.B))[2:])
		return "#"+str(hex(self.R))[2:]+str(hex(self.G))[2:]+str(hex(self.B)[2:])

class LED_Cube:
	def __init__(self,n=5):
		self.n = n
		self.cube = np.zeros((self.n,self.n,self.n,3),dtype="i2")

	def __reset__(self):
		self.cube = np.zeros((self.n,self.n,self.n,3),dtype="i2")

	def inIndex(self,x,y,z):
		return (isinstance(x,int) and isinstance(y,int) and isinstance(z,int)) and (0 <= x < self.n and 0 <= y < self.n and 0 <= z < self.n)
	
	def set_color(self,x,y,z,color):
		#int 0 <= x,y,z < self.n and color isInstans(Color)
		if(self.inIndex(x,y,z) and isinstance(color,Color)):
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
	def __init__(self,n=5, players=["player1","player2"]):
		super(gobang3d,self).__init__(n)
		self.dir = [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,1],[1,1,1]]
		self.players = dict(zip(players,[Color(0,0,0) for i in range(len(players))]))
		self.game_mode = 0 # 0 == init, 1 == playing, -1 == finished

	def set_player_color(self,player,R,G,B):
		return self.players[player].setColor(R,G,B)
	
	def isfinish(self,x,y,z):
		#スレッドを用いて並行して、一列揃っているところを探す。
		now_x = x
		now_y = y
		now_z = z
		color = self.cube[x,y,z]
		print("isfinish")
		for dir in self.dir:
			count = 1
			while(0 <= now_x+dir[0] < self.n and 0 <= now_y+dir[1] < self.n and 0 <= now_z+dir[2] < self.n):
				now_x += dir[0]
				now_y += dir[1]
				now_z += dir[2]
				if(np.all(color == self.cube[now_x,now_y,now_z])):
					count +=1
				else:
					break
			while(0 <= now_x-dir[0] < self.n and 0 <= now_y-dir[1] < self.n and 0 <= now_z-dir[2] < self.n):
				now_x -= dir[0]
				now_y -= dir[1]
				now_z -= dir[2]
				if(np.all(self.cube[now_x,now_y,now_z] == color)):
					count +=1
				else:
					break
			if(count == self.n):
				return True
		#すべて埋まっているかの判定
		return not np.any((self.cube == np.array([0,0,0])).all(axis=3))

	def getSelected(self,x,y,z,player):
		print(self.cube[x,y,z])
		print(np.array([0,0,0],dtype="i2"))
		if(np.all(self.cube[x,y,z] == np.array([0,0,0],dtype="i2"))):
			print("set color ",player)
			self.set_color(x,y,z,self.players[player])
			return True
		print("False")
		return False
		

	def start_game(self):
		self.__reset__()
		print("gobang",self.n,self.players)
		#start
		"""
		while True:
			for player in self.players:
				print(player)
				x,y,z = 0,0,0
				while(True):
					x, y, z, *_ = list(map(int,input().split()))
					print(x,y,z)
					if (self.inIndex(z,y,z)) and self.getSelected(x,y,z,player):
						break
				if(self.isfinish(x,y,z)):
					self.win(player)
					return
		"""


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


def generate_cube_win():
	global w, h, cube_canvas
	cube_window = tk.Toplevel()
	cube_window.geometry(str(w)+"x"+str(h))
	cube_canvas = tk.Canvas(cube_window, width = w, height = h)
	cube_canvas.place(x = 0, y = 0)

def draw_cube(canvas,Cube):
	global w,h,off
	canvas.delete('all')
	canvas.create_rectangle(0,0,w,h, fill="white")
	
	wi = w - off
	hi = h - off

	cube_dots = ((wi/2+off/2,0+off/2),(wi+off/2,hi/4+off/2),(wi+off/2,3*hi/4+off/2),(wi/2+off/2,hi+off/2),(0+off/2,3*hi/4+off/2),(0+off/2,hi/4+off/2),(wi/2+off/2,hi/2+off/2))
	cube_lines = ((0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(1,6),(3,6),(5,6))
	cube_dot_lines = ((0,6),(2,6),(4,6))
	for line in cube_lines:
		canvas.create_line(*cube_dots[line[0]], *cube_dots[line[1]], fill = "black", width = 1)
	for line in cube_dot_lines:
		canvas.create_line(*cube_dots[line[0]], *cube_dots[line[1]], fill = "black", width = 1, dash=(10, 5))

	for x in range(Cube.n):
		for y in range(Cube.n):
			for z in range(Cube.n):
				color = Color(*Cube[x,y,z]).getCode()
				if(color == ""):
					continue
				X,Y = xyz2xy(x,y,z,Cube.n-1)
				print(X,Y)
				canvas.create_oval(X-3,Y-3,X+3,Y+3,fill=color)

def xyz2xy(x,y,z,n):
	global w, h, off
	wi = w - off
	hi = h - off
	xv = (int(wi/2/n),int(hi/4/n))
	yv = (int(wi/2/n),-1*int(hi/4/n))
	zv = (0,-1*int(hi/2/n))
	X = xv[0]*x + yv[0]*y + zv[0]*z + off/2
	Y = xv[1]*x + yv[1]*y + zv[1]*z + off/2
	return (X,Y+hi*3/4)


cube_canvas = None 
w = 310
h = 310
off = 10
def mainV1():
	root = tk.Tk()
	root.title(u"LEDCubeClass_main()")
	root.geometry("800x480")
	go = gobang3d(n=3)
	go.set_color(0,0,0,Color(254,254,254))
	go.set_color(1,0,0,Color(254,254,254))
	go.set_color(0,1,0,Color(254,254,254))
	go.set_color(0,0,1,Color(254,254,254))
	go.set_color(0,2,1,Color(127,127,254))
	go.set_color(2,2,2,Color(127,255,127))
	print(go.cube)
	generate_cube_win()
	draw_cube(cube_canvas, go)
	root.mainloop()

def test():
	#five = gobang()
	#five.printCube()
	c = Color(3,5,7)
	cube = LED_Cube(2)
	#print(cube)
	cube.set_color(0,0,0,c)
	print(cube[0,0,0])


	go = gobang3d()
	go.start_game()

if __name__ == "__main__":
	mainV1()