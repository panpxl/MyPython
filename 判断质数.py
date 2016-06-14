#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def isPrime(n):
	import math
	if n == 1:
		return False
	elif n < 4:
		return True
	elif n & 1 == 0:
		return False
	elif n < 9:
		return True
	elif n %3 == 0:
		return False
	else:
		r = math.floor(math.sqrt(n))
		f = 5
		while f <= r:
			if n % f == 0:
				return False
			if n %(f+2) == 0:
				return False
			f += 6
		return True

print(isPrime(5))