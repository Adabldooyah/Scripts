#!/usr/bin/python3

print("""This program will ask you for the MAC addresses 
associated with your interfaces, starting with eth0.\n""")

iNum = 0
nicMap = {}

while True:
	mac = input("eth"+str(iNum)+" - ") 
	if mac == "":
		confirm = input("""Are you finished mapping all of the interface?
Press Enter to write to files or enter any character to map more interfaces.\n""")
		if confirm == "":
			break
	else:
		nicMap["eth"+str(iNum)] = mac
		iNum += 1

for k, v in nicMap.items():
	fileObject = open(/etc/systemd/network/"10-"+k+".link","w") #provide full path
	contents = [
"MACAdress=" + v
+"\nDriver=!bridge"
+"\n\n[Link]"
+"\nNamePolicy="
+"\nName=" + k + "\n"
]
	fileObject.writelines(contents)
	fileObject.close()