import serial
import glob

class bk1687b :
	def __init__(self) :
		self.serial = serial.Serial()
		self.ports = glob.glob("/dev/ttyUSB*")

	def setPortByName(self, name) :
		self.port = serial.Serial(name, 9600, timeout=0.5)

	def setPort(self, selection) :
		p = self.ports[selection]
		self.port = serial.Serial(p, 9600, timeout=0.5)

	def sendCommand(self, command) :
		#print "Sending: " + command
		if not '\r'  in command :
			command += "\r"
		self.port.write(command.encode())
		return self.getAck()

	def getAck(self) :
		ch = ''
		ret = ''
		while ch != '\r' :
			ch = self.port.read()
			if not ch :
				break
			ret += (ch.decode())
		return ret


	def parseInput(self, i) :
		v = str(float(str(i).replace(".", "")))
		v = v[:3]
		if len (v) < 3 :
			v = "0" + v

		return v

	def setV( self, v ):
		self.sendCommand("VOLT" + self.parseInput(v))


	def setC( self, i ):
		self.sendCommand("CURR" + self.parseInput(i))

	def enable(self) :
		self.sendCommand("SOUT0")

	def disable(self) :
		self.sendCommand("SOUT1")

	def getSettings(self) :
		ret = self.sendCommand("GETS")
		self.getAck()
		v = float(ret[0:3]) / 10
		c = float(ret[3:6]) / 10
		return v, c

	def getValues(self) :
		ret = self.sendCommand("GETD")
		v = float(ret[0:4]) / 100
		c = float(ret[4:8]) / 100
		return v, c

if __name__ == "__main__" :
	import argparse

	parser = argparse.ArgumentParser(description='Control program for BK Precision power supply')
	parser.add_argument('-p', action='store', type=str, help='Port to communicate with power supply')
	parser.add_argument('--on', action='store_true', help='Enable the power supply')
	parser.add_argument('--off', action='store_true', help='Disable the power supply')
	parser.add_argument('-v', action='store', type=float, help='Specify a voltage')
	parser.add_argument('-c', action='store', type=float, help='Specify a current')
	parser.add_argument('-s', action='store_true', help='Show settings')
	parser.add_argument('-o', action='store_true', help='Show output')


	args = parser.parse_args()

	bk = bk1687b()
	try :
		bk.setPortByName(args.p)
	except :
		print ("Unable to access port!")

	if args.on :
		bk.enable()

	if args.v :
		bk.setV(args.v)

	if args.c :
		bk.setC(args.c)

	if args.s :
		v, c = bk.getSettings()
		print ("\nSupply Settings")
		print ("_________________")
		print ("Voltage: ", v)
		print ("Current: ", c)
		print ()

	if args.o :
		v, c = bk.getValues()
		print ("\nOutput Values")
		print ("_________________")
		print ("Voltage: ", v)
		print ("Current: ", c)
		print ()

	if args.off :
		bk.disable()
