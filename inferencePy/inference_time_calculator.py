import time 
from tflite_runtime.interpreter import Interpreter 
import numpy as np

def inference_time_calculator(interpreter, input_full, input_details): 
    inference_records = []
    inference_sum = 0
    for i in range(10, 20): 
        input_data = input_full[i-1: i, :30, :14]
        interpreter.set_tensor(input_details[0]['index'], input_data)
        
        #calcolare il tempo di inferenza
        
        start_time = time.time()
        interpreter.invoke()
        end_time = time.time() 
	        
        inference_time = (end_time - start_time)*1e6
        print(inference_time)
        inference_records.append(inference_time)
    
    for inference_time in inference_records: 
        inference_sum += inference_time
    
    return inference_sum / len(inference_records)
