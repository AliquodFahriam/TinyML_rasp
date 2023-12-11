import numpy as np 
import serial 
import time

processed_test_data = np.float32(np.load("../processed_test_data_np.npy")) 
data = processed_test_data[:1,:1, :14]

print(data)
data = data.flatten()
stringa = ""  
for i in data: 
	stringa = stringa+str(i)+";" 
	
print(stringa)
print(type(stringa))

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0 )
ser.reset_input_buffer()
print("Serial OK" )


print( "Lunghezza in bytes" ,len(stringa.encode('utf-8')))

ser.write(stringa.encode('utf-8'))
print("message sent")

try: 
	while True: 
		if ser.in_waiting > 0: 
			print((ser.readline()).decode('utf-8'))
except KeyboardInterrupt:
	ser.close();
	print("Closing serial connection")
