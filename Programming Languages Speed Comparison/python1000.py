import timeit
Readfp=open('1GB.txt')
start=timeit.default_timer()		
for line in Readfp: 
	line.upper()
stop=timeit.default_timer()	
Readfp.close()
print("1000MB \npython :",round(stop-start,2))
Readf=open('python.txt','a')
Readf.write(str(round(stop-start,2)))
Readf.close()