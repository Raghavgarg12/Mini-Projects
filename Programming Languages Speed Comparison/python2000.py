import timeit
Readfp=open('2GB.txt')
start=timeit.default_timer()		
for line in Readfp: 
	line.upper()
stop=timeit.default_timer()	
Readfp.close()
print("2000MB \nPython :",round(stop-start,2))
Readf=open('python.txt','a')
Readf.write(str(round(stop-start,2)))
Readf.close()