import socket

def main():
	print "What message would you like to send?"
	msg = str(raw_input())
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(("0.0.0.0",54))
	
	s.listen(5)
	while True:
		c,addr = s.accept()
		c.send(msg)
		c.close()

main()
print("thanks")
