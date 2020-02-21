# bkPrecision_1687b_control
Simple python program to control a BK Precision 1687B power supply.  Needs WX and serial. 
Written for Linux but should be easily adapted to other platforms.

run the "bk1687b.py" script to launch.  The program will try to connect to the power 
supply on the first serial port in the list of ports.  If it's not found then it
will show "Disconnected". Toggle the button next to the port list to enable or
disable the power supply.

Enter a voltage or current in the text box and press either the "Set Voltage" or 
"Set Current" button to apply that setting.

The poll toggle will force the program to poll the status of the power supply on some
interval in milliSeconds.  The minimum is 500mS.
