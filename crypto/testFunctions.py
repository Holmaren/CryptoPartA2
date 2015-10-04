#!/usr/bin/python

import supplementary as sup
from base64 import b64encode, b64decode 
import dhex
import stream


print "-----------------TESTING------------------"

key=11380312415897726212538720767584623938377542218843650885786488543557849920563944820657401556147072220807050423844611527817088743264179887246035449031879964033048917437051768727745163996083995699396309860629605332639267450328379289961205789359923142431676348109877819086396004913235006262427231898532203764657706261780748597526471127787542155628754978941021278802504747939847153450812209928520258539639347968927907337576400038705453704498741239631581573919339705649004208586949422810873621196157474272177586468236634536851618181572350294408509526514361027546939234421045026063811415872877733865949984217287267027217419


parity=sup.parityWordChecksum(key)


print "-----------------TEST OUTPUT----------------"

print parity
print "BinRep: " +bin(parity)[2:]
print "Length: " + str(len(bin(parity)[2:]))

if parity==10249015871569703692:
	print "Same"


print "##########MSB#############"
msb=sup.msb(13892949480140891204)

print "MSB: " + str(msb)


print "-----------Testing stream----------------"

cipher=stream.StreamCipher(4L,11,3,5)

#Encrypt

plainText=""

#print "############### PLAIN TEXT ##############"


for line in open("plaintext.txt"):
	plainText=plainText+line

#print plainText

cipherText=""

for line in open("cipherText.txt"):
	cipherText=cipherText+line

#print "############ CIPHER TEXT #################" 
#print cipherText


encrypted=cipher.encrypt(plainText)

print "############### ENCRYPTED TEXT #############" 
print encrypted

print "Encryption:" + encrypted==cipherText

cipher.reset()

decrypted=cipher.decrypt(cipherText)


print "Decryption:" + decrypted.strip()==plainText.strip()

print "################# DECRYPTED TEXT ############"
print decrypted

cipher.reset()


decrypt2=cipher.decrypt(encrypted)

print "########## DECRYPT ENCRYPTED ###########"
print decrypt2==plainText




