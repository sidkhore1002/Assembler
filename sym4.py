import sys

sym=[]
sym_value=[]
dddb=[]
size1=[]
lit=[]

reg32=['eax','ebx','ecx','edx']
reg16=['ax','bx','cx','dx']
reg8=['ah','al','bh','bl','ch','cl']

f=open("s2.asm","r")
str1=f.read()
p=str1.split()

print ""

#-----------------------------------------------sy & value creation------------------------------------------------

for i in range(0,len(p)):

	if(p[i]!='.bss'):
		section1='data'

	 
	
	if(p[i]=='dd' or p[i]=='db' or p[i]=='dq'):
		if(p[i]=='dd'):
		 size1.append('4')
		else:
		 size1.append('1')

		dddb.append(p[i])
		sym.append(p[i-1])
		sym_value.append(p[i+1])
#---------------------------------------print symbol table----------------------------------------------------------
f1=open("symbol1.txt","w")	

#print "\n\n\n\n Symbol_No \t Symbols \t Data type  \t   Size  \t Section \t Value "

for i in range(0,len(sym)):
	f1.write("\n  "+str(i+1)+"\t\t "+sym[i]+"\t\t   "+dddb[i]+"\t\t    "+size1[i]+"\t\t  "+section1+"\t\t "+sym_value[i])

	print "\n  "+str(i+1)+"\t\t "+sym[i]+"\t\t   "+dddb[i]+"\t\t    "+size1[i]+"\t\t  "+section1+"\t\t "+sym_value[i]


