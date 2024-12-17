import tensorflow as tf
print(tf.test.is_built_with_cuda())  # Check if TensorFlow was built with CUDA support
print(tf.test.is_gpu_available())    # Check if a GPU is available
