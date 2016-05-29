import sys

try:
	file_name = raw_input("Enter filename: ") 
	file_word = raw_input("Enter the word to count: ")
	file = open(file_name,"r")
except IOError:
	print ("error")
	sys.exit()
count = 0
for line in file:
	words = line.split()
	for word in words:
		if word == file_word:
			count=count+1
print count

file.close()


