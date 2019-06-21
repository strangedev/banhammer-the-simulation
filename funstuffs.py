import math

def bad_factory(decay_factor, y_scale=1, x_scale=1):
	def bad3(x):
		return (1 + math.exp(-x*x_scale))**(-decay_factor)*y_scale
	return bad3


def log_decay(scale, offset=1):
	def f(x):
		return math.log(x + offset) * scale
	return f

