#!usr/bin/python3

import sys

try:
	# open file stream
	file_name = "/home/nijabinoy/nija"
	file = open(file_name,"w")
except IOError:
 print("There was an error writing to",file_name)
 sys.exit()
file_finish = "##"
print ("Enter'",file_finish)
print "'When finished"
file_text=raw_input("Enter text: ")
while file_text!=file_finish:
	if file_text == file_finish:
		# close the file
		file.close
		break
	file.write(file_text)
	file.write("\n")
	file_text=raw_input("Enter text: ")
file.close()
file_name = raw_input("Enter filename: ") 
if len(file_name) == 0:
	print("Next time please enter something")
	sys.exit()
try:
	file = open(file_name,"r")
except IOError:
	print ("there was an error reading file")
	sys.exit()
print (file.read())
file.close()



