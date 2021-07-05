#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import argparse
import numpy as np
import random

# LED strip configuration:
LED_COUNT      = 125      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

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

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def strip2mat(strip, mat5):
	#strip.numPixels()
	global m2s
	for z in range(5):
		for y in range(5):
			for x in range(5):
				strip.setPixelColor(m2s[z,y,x], Color(*mat5[x,y,z]))
	strip.show()

def Cube_color():
	mat5 = np.zeros((5,5,5,3),dtype=int)
	f = np.array([0,255,0])
	u = np.array([255,255,255])
	d = np.array([244,213,0])
	r = np.array([255,0,0])
	l = np.array([255,165,0])
	b = np.array([0,0,255])

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
def flying_bee(strip,colors,wait_ms=500):
	global m2s
	colorWipe(strip, Color(0,0,0), 10)
	num = len(colors)
	pos = []
	nextPos = []
	for i in range(num):
		if(i >= 5):
			num = 4
			colors = colors[:5]
			break
		pos.append([i,i,i])
		nextPos.append([i,i,i])
		strip.setPixelColor(int(m2s[pos[i][0],pos[i][1],pos[i][2]]),colors[i])
	dir = [-1,0,1]
	strip.show()
	time.sleep(wait_ms/1000.0)

	for i in range(100):
		for k in range(num):
			strip.setPixelColor(int(m2s[pos[k][0],pos[k][1],pos[k][2]]),Color(0,0,0))
			nextPos[k] = pos[k]
			nextPos[k][0] += random.choice(dir)
			nextPos[k][1] += random.choice(dir)
			nextPos[k][2] += random.choice(dir)
			for j in range(3):
				if(nextPos[k][j] < 0):
					nextPos[k][j] = 0
				if(nextPos[k][j] >= 5):
					nextPos[k][j] = 4
			pos[k] = nextPos[k]
			strip.setPixelColor(int(m2s[pos[k][0],pos[k][1],pos[k][2]]),colors[k])
		strip.show()
		time.sleep(wait_ms/1000.0)
		#print(*pos)


# Main program logic follows:
if __name__ == '__main__':
	# Process arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
	args = parser.parse_args()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	if not args.clear:
		print('Use "-c" argument to clear LEDs on exit')

	try:
		while True:
			flying_bee(strip,[Color(244,213,0),Color(0,0,255),Color(255,165,0),Colors(255,0,0),Colors(0,255,0)])
			"""
			print ('Color wipe animations.')
			colorWipe(strip, Color(255, 0, 0))  # Red wipe
			colorWipe(strip, Color(0, 255, 0))  # Blue wipe
			colorWipe(strip, Color(0, 0, 255))  # Green wipe
			print ('Theater chase animations.')
			theaterChase(strip, Color(127, 127, 127))  # White theater chase
			theaterChase(strip, Color(127,   0,   0))  # Red theater chase
			theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
			print ('Rainbow animations.')
			rainbow(strip)
			rainbowCycle(strip)
			theaterChaseRainbow(strip)
			"""

	except KeyboardInterrupt:
		if args.clear:
			colorWipe(strip, Color(0,0,0), 10)