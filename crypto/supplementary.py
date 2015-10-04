# COMP90043 Cryptography and Security
# Auxillary Functions Skeleton
# 
# Instructions to candidates:
#	As usual, do not modify function declarations, you may add additional helper functions.
#
# Any enquiries, please email `renlordy[at]unimelb.edu.au`. This code is maintained by Renlord.


# ============== ADD HELPER FUNCTIONS HERE =========================

from base64 import b64decode 

def shiftRight(key,steps):
	#Shifts the key a specified amount of steps right
	key=key>>steps
	return key

def shiftLeft(key,steps):
	#Shifts the key a specified amount of steps left
	key=key<<steps
	return key

def getBitAtLocation(key,location):
	#First shift to the right location
	key=shiftRight(key,location)
	#If the bit is one this will return one, otherwise zero
	ret=key&1
	return ret

def getWord(key,wordNr):
	#Calculate where the word starts (Number of steps to bitshift right)
	nrSteps=wordNr*64
	#Get a partial key where the word we are looking for are furthest right
	partialKey=shiftRight(key,nrSteps)
	word=0
	#Iterate the bits of the word and add 2^bitPosition if the bit is one
	for i in xrange(64):
		if getBitAtLocation(partialKey,i)==1:
			word=word+(2**i)
	return word

def findLeftMostBit(numb):
	'''
	Finds the position of the leftmost bit that is one in a number
	'''
	#Variable to store the position of the leftmost one	
	leftMost=0
	#Variable to store the current position we are on
	curPosition=0
	
	while numb>0:
		#If the current bit furthest to the right is one we update the leftmost variable
		if getBitAtLocation(numb,0)==1:
			leftMost=curPosition
		#Update the current position and shift the numb one step to the right
		curPosition+=1
		numb=shiftRight(numb,1)

	return leftMost

def msb(numb):
	'''
	Gets the most significant byte from numb
	INPUT:
		nothing
	OUTPUT:
		MSB(numb), the most significant byte of numb
	'''
	if numb<((2**8)-1):
		return numb

	msb=0
	#Find the leftmost bit that is one
	leftMost=findLeftMostBit(numb)
	#Iterate the eight bits included in the MSB, including the leftMost bit that is one
	startValue=leftMost-7
	for i in xrange(startValue,startValue+8):
		if getBitAtLocation(numb,i)==1:
			#If the current bit is one add 2^"position in MSB" to MSB
			msb=msb+(2**(i-startValue))
	
	return msb


def checkIfBase64Compatible(msg):
	'''
	Checks if a message can be decoded or not to see if it's a plain text or cipher text
	'''
	try:
		b64decode(msg)
	except TypeError:
		print "Can't be decoded"
		return False

	return True

# ============== END HELPER FUNCTIONS ==============================

# TODO
def parityWordChecksum(key):
	assert(type(key) == type(1L))
	assert(key < (2 ** 2048))
	"""
	parityWordChecksum, takes a 2048 bit key and applies a word by word XOR to yield a 64 bit result at the end. 
	INPUT:
		key, 2048bit Integer from Part A1 Diffie Hellman Key Exchange
	OUTPUT:
		result, 64bit Integer
	"""
	result = 0
	# ======== IMPLEMENTATION GOES HERE =========
	#Calculate the number of words
	nrWords=2048/64
	#Iterate all the words
	for i in xrange(nrWords):
		#Get the current word and XOR with result
		curWord=getWord(key,i)
		result=result^curWord
		#print result

	# ======== END IMPLEMENTATION ===============
	return result

# TODO
def deriveSupplementaryKey(key, p):
	assert(type(key) == type(1L))
	assert(type(p) == type(1))
	assert(key < (2 ** 2048))
	assert(p < (2 ** 64))
	"""
	deriveSupplementaryKeyA, takes a 2048 bit key and applies the modulo operation to yield the modulo of `p1`. 
	INPUT:
		key, 2048bit Integer from Part A1 Diffie Hellman Key Exchange
		p1, 64bit random prime number
	OUTPUT:
		keyA, 64bit Integer for use as `a` key for Stream Cipher
	"""
	# ======== IMPLEMENTATION GOES HERE =========

	subKey=key%p

	# ======== END IMPLEMENTATION ===============
	assert(type(subKey) == type(1) or type(subKey) == type(1L))
	return subKey


# ============== ADD HELPER FUNCTIONS HERE =========================

# ============== END HELPER FUNCTIONS ==============================
