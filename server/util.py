def flines(f):
	with open(f, 'r') as f:
		yield from f.readlines()

def pad(l, size, padding=None):
	if len(l) < size:
		return l + ([padding] * (size - len(l)))
	else:
		return l
