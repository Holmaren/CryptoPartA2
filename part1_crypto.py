# COMP90043 Cryptography and Security 
# Cryptography Skeleton Function for Project 
# 
# Candidates will have to implement the following skeleton functions.
# Candidates may create additional skeleton functions by importing the skeleton functions from a seperate file. 
# Do not alter the function declarations in this file, or add additional helper functions in this file.

import random

# TO DO. 
def diffie_hellman_private(numbits):
    """
        diffie_hellman_private

        Returns a private secret integer with `numbits`. 
    """
    #Using random.getrandbits(k) which gives me a long int with k random bits. Casting this to an int
    private = int(random.getrandbits(numbits))
    return private

# TODO
def diffie_hellman_pair(generator, modulus, private):
    """
        diffie_hellman_pair

        Given a generator, prime modulus and a private integer, produce the public integer. Return a tuple of (Private Integer, Public Integer)
    """
    #Using my function modexp to calculate the public integer (generator^private)%modulus
    public = modexp(generator,private,modulus)
    return (private, public)

# TODO 
def diffie_hellman_shared(private, public, modulus):
    """
        diffie_hellman_shared

        Given a private integer, public integer and prime modulus. Compute the shared key for the communication channel, then return it.
    """
    #Using my function modexp to calculate the shared key which is (public^private)%modulus
    shared_key = modexp(public,private,modulus)
    return shared_key

# TODO
def modexp(base, exponent, modulo):
    """
        modexp

        Given a base, exponent and modulo. Compute the modular exponentiation.
    """
    result = 1

    '''
    We will use the LSB of the current exponent variable to determine if we should multiply
    the temporary result of the base or if we should just square the base.
    '''
    
    #Also reducing the base in the begining
    if base>modulo:
        base=base%modulo
    
    while exponent:
        #If the current exponent is odd (LSB=1)
        if exponent&1:
            result=(result*base)%modulo
            
        #Square the base
        base=(base*base)%modulo
        #Bitshift the exponent one step to the right
        exponent>>=1

    return result
    
