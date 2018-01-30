import sys
import os


f=open("mymake.txt","r")
s=f.read()

ss=s.split()
print ss

done=[]

#for i in range(0,len(ss)):

c=0
while(c<10):
	i=input("\nenter\n")
	if(i==1):	
		done.append(ss[i-1])
		execfile(ss[i])
		print done
	else:
		if(i==3):
			i=i+2			
			if(ss[i-3] not in done):	
				print "required files are not run"
			else:
				done.append(ss[i-1])
				execfile(ss[i])

		if(i==2):
			i=i+1
			if('.py' in ss[i]):
				if(ss[i-3] in done):	
					done.append(ss[i-1])
					execfile(ss[i])
				else:
					print "required files are not run"
	c=c+1

#files = os.listdir(os.curdir)
#print files


