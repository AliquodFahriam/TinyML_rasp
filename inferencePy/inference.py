#!pip3 install --extra-index-url https://google-coral.github.io/py-repo tflite_runtime
import tflite_runtime
from tflite_runtime.interpreter import Interpreter 
import numpy as np
import time

interpreter = Interpreter("../small_lstm_batch_1_quad.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
processed_test_data = np.float32(np.load("../processed_test_data_np.npy"))


input_shape = input_details[0]['shape']
input_data = processed_test_data[10:11, :30, :14]
interpreter.set_tensor(input_details[0]['index'], input_data)
start_time = time.time()
interpreter.invoke()
end_time = time.time()

inference_time = (end_time - start_time)*1e6 #per avere il tempo in microsecondi

print("Input_shape = ", input_shape)

output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)
print("Inference time: ", inference_time)