import socket
import sys
from time import gmtime, strftime

timestamp = datetime.now()

def main():

	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #Arguement 1 = IP Address of Host
    #Arguement 2 = Port number
    	sock.bind((sys.argv[1],int(sys.argv[2])))
    	#Up to five people can connect
        sock.listen(5)
	while True:
		c,addr = s.accept()
		c.send("Opps.")
        print "Time of Incident :", timestamp
		print "%s on port %i has connected." % (addr)
		sys.stdout.write("\a")
		sys.stdout.flush()
		c.close()

main()
