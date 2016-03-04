from hexdump import hexdump
import socket 
import telnetlib
import struct

q = lambda x: struct.pack("I", x)
Q = lambda x: struct.unpack("I", x)[0]

def interact():
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

def r_until(st, debug=false):
    ret = "" 
    while st not in ret:
        lret = s.recv(8192)
        if debug and len(lret) > 0:
            print lret
        ret += lret
    return ret

s = socker.creat_connection(("127,0,0,1", 4000))
#f = s.makefile()
print s.recv(8192)
#print r_until("[ ]")

s.send()

interact()
