import matplotlib.pyplot as plt
file1 = open('python.txt','r')
file2 = open('cpp.txt','r')
file3 = open('c.txt','r')
file4 = open('java.txt','r')
file5= open('perl.txt','r')
x=[100,500,1000,1500,2000]
y1=file1.readlines()
y2=file2.readlines()
y3=file3.readlines()
y4=file4.readlines()
y5=file5.readlines()
z1=[]
z2=[]
z3=[]
z4=[]
z5=[]
for i in range(0,5):
  z1.append(float(y1[i]))
  z2.append(float(y2[i]))
  z3.append(float(y3[i]))
  z4.append(float(y4[i]))
  z5.append(float(y5[i]))
plt.plot(x,z1,'r',label="Python")
plt.plot(x,z2,label="C++")
plt.plot(x,z3,label="C")
plt.plot(x,z4,label="Java")
plt.plot(x,z5,'k',label="Perl")
plt.title("Performance Comparison")
plt.xlabel("File size (MB)")
plt.ylabel("Time Taken (secs)")
plt.legend()
plt.savefig("GraphImage.png", dpi=300)
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
