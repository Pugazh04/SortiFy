import onnxruntime as ort
import numpy as np

# Load ONNX model
onnx_model_path = "D:/Garbage/dataset_for_model/GarbageV2.onnx"  # Change to your actual model path
session = ort.InferenceSession(onnx_model_path)

# Get model input details
input_name = session.get_inputs()[0].name
input_shape = session.get_inputs()[0].shape
input_dtype = session.get_inputs()[0].type

# Print input details
print(f"Input Name: {input_name}")
print(f"Input Shape: {input_shape}")
print(f"Input Type: {input_dtype}")

# Create a dummy input in NHWC format (batch, height, width, channels)
dummy_input = np.random.randn(1, 224, 224, 3).astype(np.float32)  # Keep it NHWC

# Run inference
output = session.run(None, {input_name: dummy_input})
print("ONNX model is working correctly!")
