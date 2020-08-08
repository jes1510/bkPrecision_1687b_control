# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Frame
###########################################################################

class Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BK Precision 1687b", pos = wx.DefaultPosition, size = wx.Size( 500,315 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 500,315 ), wx.Size( 500,315 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Serial Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		sp_choiceChoices = []
		self.sp_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sp_choiceChoices, 0 )
		self.sp_choice.SetSelection( 0 )
		bSizer2.Add( self.sp_choice, 0, wx.ALL, 5 )

		self.enToggle_button = wx.ToggleButton( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.enToggle_button.SetValue( True )
		bSizer2.Add( self.enToggle_button, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.input_txtCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.input_txtCtrl, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Set Voltage", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Set Current", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Poll Rate (mS):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.pollmS_txtCtrl = wx.TextCtrl( self, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.pollmS_txtCtrl, 0, wx.ALL, 5 )

		self.poll_button = wx.ToggleButton( self, wx.ID_ANY, u"Poll", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.poll_button, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button4, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		status_sizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Voltage" ), wx.HORIZONTAL )

		self.vStatus_panel = wx.Panel( status_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		status_sizer.Add( self.vStatus_panel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer7.Add( status_sizer, 1, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Current" ), wx.VERTICAL )

		self.iStatus_panel = wx.Panel( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer4.Add( self.iStatus_panel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer7.Add( sbSizer4, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )

		settings_sizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Settings" ), wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( settings_sizer.GetStaticBox(), wx.ID_ANY, u"Voltage (V):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		settings_sizer.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.voltage_val = wx.StaticText( settings_sizer.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.voltage_val.Wrap( -1 )

		settings_sizer.Add( self.voltage_val, 0, wx.ALL, 5 )


		settings_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( settings_sizer.GetStaticBox(), wx.ID_ANY, u"Current (A):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		settings_sizer.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.current_val = wx.StaticText( settings_sizer.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.current_val.Wrap( -1 )

		settings_sizer.Add( self.current_val, 0, wx.ALL, 5 )


		settings_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( settings_sizer, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.timer = wx.Timer()
		self.timer.SetOwner( self, wx.ID_ANY )
		self.oneShot_Timer = wx.Timer()
		self.oneShot_Timer.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.enToggle_button.Bind( wx.EVT_TOGGLEBUTTON, self.onEn_Button )
		self.m_button2.Bind( wx.EVT_BUTTON, self.onSetV )
		self.m_button3.Bind( wx.EVT_BUTTON, self.onSetC )
		self.poll_button.Bind( wx.EVT_TOGGLEBUTTON, self.onPoll )
		self.m_button4.Bind( wx.EVT_BUTTON, self.onSingle )
		self.Bind( wx.EVT_TIMER, self.onTimer, id=wx.ID_ANY )
		self.Bind( wx.EVT_TIMER, self.onOneShot, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onEn_Button( self, event ):
		event.Skip()

	def onSetV( self, event ):
		event.Skip()

	def onSetC( self, event ):
		event.Skip()

	def onPoll( self, event ):
		event.Skip()

	def onSingle( self, event ):
		event.Skip()

	def onTimer( self, event ):
		event.Skip()

	def onOneShot( self, event ):
		event.Skip()


