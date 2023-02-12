import random as r
import string as s
fp=open('1.5GB.txt','w')
for i in range(0,50331648):
   fp.write("abcdefghijklmnopqrstuvwxyzabcdef")
fp.close()