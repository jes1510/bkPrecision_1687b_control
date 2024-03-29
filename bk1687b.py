"""Subclass of Frame, which is generated by wxFormBuilder."""

import wx
import bk1687bGUI
import glob
import serial
import time
import wx.lib.gizmos.ledctrl as led
import bk1687bdrv

bk = bk1687bdrv.bk1687b()

# Implementing Frame
class bk1687bFrame( bk1687bGUI.Frame ):
	def __init__( self, parent ):
		bk1687bGUI.Frame.__init__( self, parent )

		for i in bk.ports :
			self.sp_choice.Append(i)
		self.sp_choice.SetSelection(0)

		self.poll_button.SetValue(True)
		self.vStatus_Led = led.LEDNumberCtrl(self.vStatus_panel, -1, size = (250,100))
		self.vStatus_Led.SetValue("0.000")
		self.iStatus_Led = led.LEDNumberCtrl(self.iStatus_panel, -1, size = (250,100))
		self.iStatus_Led.SetValue("0.000")

		try :
			bk.setPort()
			self.onSingle(None)
			self.onEn_Button(None)
			self.timer.Start(100)

		except :
			self.enToggle_button.SetBackgroundColour("RED")
			self.enToggle_button.SetLabel("Not Connected")



	def onEn_Button(self, event) :
		sel = self.sp_choice.GetSelection()
		if self.enToggle_button.GetValue() :
			self.enToggle_button.SetBackgroundColour("GREEN")
			self.enToggle_button.SetLabel("Enabled")
			bk.setPort(sel)
			bk.enable()


		else :
			self.enToggle_button.SetBackgroundColour("RED")
			self.enToggle_button.SetLabel("Disabled")
			bk.setPort(sel)
			bk.disable()


	def onTimer(self, event) :
		self.onSingle(None)



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
		v, c = bk.getSettings()

		self.voltage_val.SetLabel(str(v))
		self.current_val.SetLabel(str(c))

		v, c = bk.getValues()

		self.vStatus_Led.SetValue(str(v))
		self.iStatus_Led.SetValue(str(c))

	def onSetV(self, event) :
		v = float(self.input_txtCtrl.GetValue())
		bk.setV(v)

	def onSetC(self, event) :
		c = float(self.input_txtCtrl.GetValue())
		bk.setV(c)


if __name__ == "__main__" :
	app = wx.App(False)
	frame = bk1687bFrame(None)
	frame.Show(True)
	app.MainLoop()
