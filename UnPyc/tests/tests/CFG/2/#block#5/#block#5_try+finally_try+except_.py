try:
	try:
		raise NameError('YourNameIncorrect')
	finally:
		raise NameError('YourNameIncorrect')
except:
	try:
		raise NameError('YourNameIncorrect')
	finally:
		raise NameError('YourNameIncorrect')
