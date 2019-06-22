"""
Module for mathematical functions
"""

import math


def sigmoid_like_factory(decay_factor=1, y_scale=1, x_scale=1):
	def bad3(x):
		return ((1 + math.exp(-x * x_scale)) ** (-decay_factor)) * y_scale
	return bad3


def log_decay_factory(y_scale=1, x_offset=1):
	def f(x):
		return math.log(x +x_offset) * y_scale
	return f
