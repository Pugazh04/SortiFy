import tensorflow as tf
import tf2onnx
import onnx
from tensorflow.keras.models import load_model

model = load_model("<add your path to tensorflow model>")

spec = (tf.TensorSpec((None, 224, 224, 3), tf.float32),) 
onnx_model, _ = tf2onnx.convert.from_keras(model, input_signature=spec)

onnx.save(onnx_model, '<add your path to save onnx model>')
