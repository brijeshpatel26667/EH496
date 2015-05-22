import socket

def main():
	address = sys.argv[1]
	port = int(sys.argv[2])
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((address,port))
	s.send("Hello")
	message = s.recv(4096)
	myhexdump(message)

def myhexdump(src):
	length = 16
	result = []
	for i in range(0,len(src),length):
		substring = src[i:i+length]
		result.append("%04X " % i)
		hex = ''.join("%X" % ord(c) for c in substring)
		result.append("%-*s %s\n" % (length*3,hex,substring))
	print b''.join(result)

main()
