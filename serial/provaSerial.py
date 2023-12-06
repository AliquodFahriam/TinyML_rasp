
import serial
import time

TX_PIN = 14
RX_PIN = 15

ser = serial.Serial(port = '/dev/ttyUSB0', baudrate=115200, timeout = 1) 
time.sleep(1)
ser.reset_input_buffer()
print("Serial OK" )

stringa = "Raspberry"
ser.write(stringa.encode('UTF-8'))
try: 
	while True: 
		time.sleep(0.01) #Per una questione di risorse
		if ser.in_waiting > 0: 
			line = ser.readline().decode('UTF-8').rstrip()
			print(line)
except KeyboardInterrupt: 
	print("Closing Serial Comm")
	ser.close()
