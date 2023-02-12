import timeit
Readfp=open('100MB.txt')
start=timeit.default_timer()		
for line in Readfp: 
	line.upper()
stop=timeit.default_timer()	
Readfp.close()
print("100MB \nPython :",round(stop-start,2))
Readf=open('python.txt','w')
Readf.write(str(round(stop-start,2)))
Readf.close()