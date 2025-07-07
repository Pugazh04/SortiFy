import tensorflow as tf
import tf2onnx
import onnx
from tensorflow.keras.models import load_model

# Load your model
model = load_model("D:/Garbage_V2.h5")

# Convert the model
spec = (tf.TensorSpec((None, 224, 224, 3), tf.float32),)  # Adjust shape if necessary
onnx_model, _ = tf2onnx.convert.from_keras(model, input_signature=spec)

# Save the ONNX model
onnx.save(onnx_model, 'D:/Garbage_V2.onnx')
