import serial 
import time 
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0 )
time.sleep(1)


ser.reset_input_buffer()
print("Serial OK" )

try: 
	while True: 
		time.sleep(0.01)
		ser.write("Hello from Raspberry Pi \n".encode('utf-8'))
		print("message sent")
		while ser.in_waiting <= 0: 
			time.sleep(0.01) 
		response = ser.readline().decode('utf-8').rstrip()
		print(response)
	#while True: 
	#	time.sleep(0.01) #Per una questione di risorse
		#if ser.in_waiting > 0: 
		#	line = ser.readline().decode('UTF-8').rstrip()
		#	print(line)
except KeyboardInterrupt: 
	print("Closing Serial Comm")
	ser.close()
