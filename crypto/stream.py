# COMP90043 Cryptography and Security
# Skeleton for Stream Cipher
# 
# Instructions to candidates:
#   - You may add additional helper functions prior to the declaration of the 
#   class. But I'd advise you to import it from a different file.
#   - Do not modify class declaraction, function declarations or method 
#   declarations.
#   - After you've implemented this, remember to write a few lines to comment
#   on the security of this cipher as specified in the Project Specifications

import cryptoclient.crypto.supplementary as auxillary

#import supplementary as auxillary

from base64 import b64encode, b64decode 

# ============== ADD HELPER FUNCTIONS HERE =========================


# ============== END HELPER FUNCTIONS ==============================

class StreamCipher:
    # TODO
    def __init__(self, dh_key, dh_p, p1, p2):
        """
        __init__, constructor for StreamCipher class.
        INPUT:
            dh_key, 2048bit DH Key from Part A1
            p, DH Key Parameter, Prime Modulus
        OUTPUT:
            returns an instantiated StreamCipher object
        """
        # ======== IMPLEMENTATION GOES HERE =========
        self.dh_key = dh_key # 2048bit DH Key from Part A1
        self.p = dh_p # DH Key Parameter, Prime Modulus

        self.a =  0 # Supplementary Key A for Stream Cipher
        self.b = 0 # Supplementary Key B for Stream Cipher
        self.r_i = 0 # Shift Register 

        #Get the initial shift register
        self.reset()
        #Derive a and b
        self.a=auxillary.deriveSupplementaryKey(self.dh_key,p1)
        self.b=auxillary.deriveSupplementaryKey(self.dh_key,p2)
        # ======== END IMPLEMENTATION ===============

    # =============== ADD CLASS ADDITIONAL METHODS ==================
    
    # =============== END CLASS ADDTIONAL METHODS ===================

    # TODO
    def updateShiftRegister(self):
        """
        updateShiftRegister, updates the shift register for XOR-ing the next 
        byte.
        INPUT:
            nothing
        OUTPUT:
            nothing
        """
        # ======== IMPLEMENTATION GOES HERE =========
        newRi=(self.a*self.r_i+self.b) % self.p
        self.r_i=newRi

        # ======== END IMPLEMENTATION ===============
        return None

    # TODO
    def _crypt(self, msg):
        assert(type(msg) == type("hello"))
        """
        _crypt, takes a cipher text/plain text and decrypts/encrypts it.
        INPUT:
            msg, either Plain Text or Cipher Text.
        OUTPUT:
            new_msg, if PT, then output is CT and vice-versa.
        """
        # ======== IMPLEMENTATION GOES HERE =========
        
        new_msg=""
        new_msg_array=[]
        #Iterate the bytearray of the msg
        for byte in bytearray(msg):
            
            #For every byte perform the encipher/decipher function
            newByte=byte^auxillary.msb(self.r_i)
            #Update the register
            self.updateShiftRegister()
            #Append the new byte to the new message array
            new_msg_array.append(newByte)

        #Turn the new_msg_array into a byte array
        new_msg_array=bytearray(new_msg_array)

        new_msg=str(new_msg_array)		

        # ======== END IMPLEMENTATION ===============
        return new_msg

    # TODO
    def reset(self):
        """
        reset, resets the shift register back to its initial state.
        INPUT:
            nothing
        OUTPUT:
            nothing
        """
        # ======== IMPLEMENTATION GOES HERE =========
		
        r0=auxillary.parityWordChecksum(self.dh_key)
        self.r_i=r0

        # ======== END IMPLEMENTATION ===============
        return None

    # =============== ADD CLASS ADDITIONAL METHODS ==================
	
    def encrypt(self,msg):
		
        #Get the new message
        new_msg=self._crypt(msg)
        #Encoded it with base64 encoding
        new_msg=b64encode(new_msg)
		
        return new_msg

    def decrypt(self,msg):
		
        #This msg is in base64 encoded so we need to decode this
        msg=b64decode(msg)
        #Then we get the plain text
        new_msg=self._crypt(msg)

        return new_msg		
		

    # =============== END CLASS ADDTIONAL METHODS ===================

# ============== ADD HELPER FUNCTIONS HERE =========================

# ============== END HELPER FUNCTIONS ==============================
