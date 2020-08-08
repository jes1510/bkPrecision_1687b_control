"""Subclass of Frame, which is generated by wxFormBuilder."""

import wx
import bk1687bGUI
import glob
import serial
import time
import wx.lib.gizmos.ledctrl as led

# Implementing Frame
class bk1687bFrame( bk1687bGUI.Frame ):
	def __init__( self, parent ):
		bk1687bGUI.Frame.__init__( self, parent )
		self.ports = glob.glob("/dev/ttyUSB*")
		for i in self.ports :
			self.sp_choice.Append(i)
		self.sp_choice.SetSelection(0)
		self.enToggle_button.SetBackgroundColour("RED")
		self.enToggle_button.SetLabel("Not Connected")
		self.poll_button.SetValue(True)
		self.timer.Start(100)
		self.vStatus_Led = led.LEDNumberCtrl(self.vStatus_panel, -1, size = (250,100))
		self.vStatus_Led.SetValue("0.000")
		self.iStatus_Led = led.LEDNumberCtrl(self.iStatus_panel, -1, size = (250,100))
		self.iStatus_Led.SetValue("0.000")

		try :
			self.setPort()
			ret = self.sendCommand("SOUT1")
			assert ret == 'OK\r'
			self.enToggle_button.SetValue(0)
			self.enToggle_button.SetBackgroundColour("RED")
			self.enToggle_button.SetLabel("Disabled")
			self.enToggle_button.SetValue(0)
			self.onSingle(None)

		except :
			print "Not connected...", ret


	def onEn_Button(self, event) :
		if self.enToggle_button.GetValue() :
			self.enToggle_button.SetBackgroundColour("GREEN")
			self.enToggle_button.SetLabel("Enabled")
			self.sendCommand("SOUT0")


		else :
			self.enToggle_button.SetBackgroundColour("RED")
			self.enToggle_button.SetLabel("Disabled")
			self.sendCommand("SOUT1")


	def setPort (self) :
		s = self.sp_choice.GetSelection()
		p = self.ports[s]
		self.port = serial.Serial(p, 9600, timeout=0.5)

	def sendCommand(self, command) :
		#print "Sending: " + command
		if not '\r'  in command :
			command += "\r"
		self.setPort()
		self.port.write(command)
		return self.getAck()

	def getAck(self) :
		ch = ''
		ret = ''
		while ch != '\r' :
			ch = self.port.read()
			if not ch :
				break
			ret += ch
		return ret

	def parseInput(self) :
		v = str(float(self.input_txtCtrl.GetValue())).replace(".", "")
		v = v[:3]
		if len (v) < 3 :
			v = "0" + v

		self.input_txtCtrl.SetValue('')
		return v

	def onSetV( self, event ):
		self.sendCommand("VOLT" + self.parseInput())



	def onTimer(self, event) :
		self.onSingle(None)

	def onSetC( self, event ):
		self.sendCommand("CURR" + self.parseInput())


	def onPoll( self, event ):
		self.timer.Stop()

		if self.poll_button.GetValue() :
			try :
				t = int(self.pollmS_txtCtrl.GetValue())
				if t < 250 : t = 250
				self.timer.Start(t)

			except :
				self.poll_button.SetValue(0)

	def onSingle( self, event ):
		ret = self.sendCommand("GETS")
		self.getAck()
		v = float(ret[0:3]) / 10
		c = float(ret[3:6]) / 10
		self.voltage_val.SetLabel(str(v))
		self.current_val.SetLabel(str(c))

		ret = self.sendCommand("GETD")
		v = float(ret[0:4]) / 100
		c = float(ret[4:8]) / 100
		self.vStatus_Led.SetValue(str(v))
		self.iStatus_Led.SetValue(str(c))



if __name__ == "__main__" :
	app = wx.App(False)
	frame = bk1687bFrame(None)
	frame.Show(True)
	app.MainLoop()
