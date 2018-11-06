import time

def specialPrint(character): 
	# the end and flush bits are to get the 
	# newline not to happen
	print(character, end='', flush=True)

def rapidTween():
	time.sleep(.2)