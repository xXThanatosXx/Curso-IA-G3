import tensorflow as tf

x = tf.Variable(0.)
with tf.GradientTape() as tape:
    y = 2 * x + 3

grad_of_y_wrt_x = tape.gradient(y, x)

x = tf.Variable(tf.random.uniform((2,2)))

with tf.GradientTape() as tape:
    y = 2*x+3
grad_of_y_wrt_x = tape.gradient(y, x)

w = tf.Variable(tf.random.uniform((2,2)))
b = tf.Variable(tf.zeros((2,2)))
x = tf.random.uniform((2,2))
with tf.GradientTape() as tape:
    y = tf.matmul(x,w) + b
grad_of_y_wrt_x = tape.gradient(y,[w,b])