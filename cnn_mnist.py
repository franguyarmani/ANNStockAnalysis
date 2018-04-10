from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Imports
import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

# Our application logic will be added here

filename_queue = tf.train.string_input_producer(["data\\AAPL1+2.csv"])

reader = tf.TextLineReader(4)
nextline = reader.read(filename_queue)
tf.Print(nextline)
