def checkForMAC(MAC):
	packFromPhone=sniff(lfilter=lambda d: d.src=='xx:xx:xx:xx:xx:xx' or d.dst=='xx:xx:xx:xx:xx:xx')
	print "Phone is connected to the network"
	openPassWindow()
