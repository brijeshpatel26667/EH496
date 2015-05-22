#Simple ip range script that outputs all
#possible host IP addresses into an array

def iprange(network, starthostip, stophostip):
    tempiplist = []
    for i in range (starthostip,stophostip+1):
        tempiplist.append("%s.%i" % (network , i))
    return tempiplist

def main():
    iplist = []
    network = raw_input('Enter your network prefix: ')
    starthostip = int(raw_input('Start range from address %s.' % network))
    stophostip = int(raw_input('Ending range at address %s.' % network))
    print "*******************************************************"
    print "*             Your network is %s               *" % network
    print "*_____________________________________________________*"
    print "*           Your starting IP %s.%i              *" % (network,starthostip)
    print "*_____________________________________________________*"
    print "*       Your ending IP will be %s.%i          *" % (network,stophostip)
    print "*******************************************************"
    iplist = iprange(network, starthostip, stophostip)
    print iplist
main()
