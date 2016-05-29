

m1=[[2,3,4],[8,0,6],[8,9]]
m2=[[4,1,3],[0,5,2],[9,0]]
result=[]



def printArray(arr):
	#for i in range(len(arr)):
		#for j in range(len(arr[i])):
	print(arr)
		#print("\n")
	
def add():
	assert len(m1[0])==len(m2[0])
	sum=0
	for i in range(len(m1)):
		#print(i)
		row=[]
		for j in range(len(m2[i])):
			sum=m1[i][j]+m2[i][j]
			row.append(sum)
		result.append(row)
def main():
	add()
	printArray(result)

main()