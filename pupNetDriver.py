#!/usr/bin/python

# python program to communicate with an MCP3008

# Import our SpiDe wrapper and out sleep function

import spidev
import time
import os

# Establish SPI device on Bus 0, Device 0
spi = spidev.SpiDev()
spi.open(0,0)

def getAdc (channel):
	#check for valid channel
	if ( (channel > 7) or (channel < 0) ):
		return -1
	
	# Preform SPI transaction and store returned bits in 'r'
	r = spi.xfer( [1, (8 + channel) << 4, 0] )

	# Filter data bits from returned bits
	adcOut = ( (r[1] & 3) << 8 ) + r[2]
	percent = int( round( adcOut / 10.24 ) )
	
	# Print out 0 - 1023 value and percentage
	if (adcOut > 700 ):
		print("ADC output: {0:4d}	Percentage: {1:3}%".format( adcOut, percent))
		os.system("fswebcam -r 1280x720 /home/pi/Pictures/pupnettest.jpg")	
		time.sleep(0.1)
		os.system("mpack -s 'WOOF!' /home/pi/Pictures/Pupnet.jpg cheeriereptilian@gmail.com")
		
while True:
	getAdc(0)
