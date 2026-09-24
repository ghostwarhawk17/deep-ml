def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	# Your code here
	if z == 0:
		return 0
	if z > 0:
		return z
	if z < 0:
		return max(z, z * alpha)
