import serial
import serial.tools.list_ports

port_list = list(serial.tools.list_ports.grep("VID:PID=239A:800C"))
port = port_list[0] # assume only one is connected
arduino = serial.Serial(None, baudrate=115200, timeout=5, write_timeout=3) # port=None
arduino.port = port # could just replace None with the port but you can change the port like this too

arduino.flush()
arduino.write('test')
msg = arduino.readline()
print(msg)

