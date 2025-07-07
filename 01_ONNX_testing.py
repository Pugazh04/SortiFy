import onnxruntime as ort
import numpy as np

# NOTE : This file is used to test the converted onnx model 

onnx_model_path = "<add your path to onnx model>" 
session = ort.InferenceSession(onnx_model_path)

input_name = session.get_inputs()[0].name
input_shape = session.get_inputs()[0].shape
input_dtype = session.get_inputs()[0].type

print(f"Input Name: {input_name}")
print(f"Input Shape: {input_shape}")
print(f"Input Type: {input_dtype}")

dummy_input = np.random.randn(1, 224, 224, 3).astype(np.float32)  

output = session.run(None, {input_name: dummy_input})
print("ONNX model is working correctly!")
