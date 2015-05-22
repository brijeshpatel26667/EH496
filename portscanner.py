import socket, subprocess, sys
from datetime import datetime

hostIP  = socket.gethostbyname(sys.argv[1])

startTime = datetime.now()			# Time the scan starts



print"*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*"
print""
print"         S C A N N I N G . . .         "
print""
print"*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*"


try:
	#Checks all ports in this range
    for scan_port in range(1,10000):

		#socket, protocol
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		result = s.connect_ex((hostIP, scan_port))

		if result == 0:
            print "Port {}: \t Open".format(scan_port)
        s.close()

#Error: Checks for address-related errors
except socket.gaierror:
    print "Couldn't find host"
    sys.exit()

#Error: Checks for socket-related errors
except socket.error:
    print "Couldn't connect to server"
    sys.exit()

#calculates the time for scan to complete
endTime = datetime.now()
totalTime = endTime - startTime

print"*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*"
print"                                       "
print" SCAN COMPLETED IN : *", totalTime
print"                                       "
print"*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*"
