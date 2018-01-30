import sys

sym=[]
sym_value=[]
dddb=[]
size1=[]
lit=[]

reg32=['eax','ebx','ecx','edx']
reg16=['ax','bx','cx','dx']
reg8=['ah','al','bh','bl','ch','cl']

f=open("one.asm","r")
str1=f.read()
p=str1.split()

print ""

#---------------------------------------------------address cal------------------------------------------------------

def addr_cal(q0,q1,address,cnt):
	
	cnt +=1

	if(cnt==1):
		address=0000
		return address
	
	if(q0 in reg32 and q1 in reg32):
		address +=4
		return address

	if(q0 in reg32 and q1 in sym or  q0 in reg16 and q1 in sym or q0 in reg8 and q1 in sym):
		address +=6
		return address

	if(q0 in reg32 and q1 in lit  or q0 in reg16 and q1 in lit or q0 in reg8 and q1 in lit):
		address +=6
		return address

	if(q0 in sym and q1 in lit):
		address +=8
		return address

	if(q0 in sym and q1 in reg32 or q0 in sym and q1 in reg16 or q0 in sym and q1 in reg8):
		address +=6
		return address

#---------------------------------------------------operand checking------------------------------------------------------
def check_op1(q1):
	op1=""
	if(q1 in reg32):			
		op1="Reg-32"	
		return op1

	if(q1 in reg16):			
		op1="Reg-16"	
		return op1

	if(q1 in reg8):			
		op1="Reg-08"	
		return op1

	elif(q1 in sym):			
		index1=sym.index(q1)			
		op1="Sym- "+str(index1+1)	
		return op1

	else :
		op1="\nerror :- 1st op cant be imd\n"
		return op1

def check_op2(q2):
	op2=""	
	if(q2 in reg32):			
		op2="Reg-32"	
		return op2

	if(q2 in reg16):			
		op2="Reg-16"	
		return op2

	if(q2 in reg8):			
		op2="Reg-08"	
		return op2

	if(q2 in sym):
		index2=sym.index(q2)			
		op2="Sym-"+str(index2+1)	
		return op2

	if(q2 in lit):
		index2=lit.index(q2)			
		op2="Lit-"+str(index2+1)	
		return op2

def check_operands(m1):	

	print "\nSr. no \t   Instruction \t Number_of_operands \t Operand 1 \t   Operand 2 \t Address \tOriginal Instruction"

	addr=0000
	cnt1=0
	for k in range(m1,len(p)):
		if(p[k]=='mov' or p[k]=='add' or p[k]=='sub'):	
			if(p[k]=='mov'):	
				op_no=1
			if(p[k]=='add'):	
				op_no=2

			q=p[k+1].split(',')

			if(q[0] in reg32 or q[0] in sym or q[0].isdigit() or q[0] in reg16   and   q[1] in reg32 or q[1] in sym or q[1].isdigit()):
				op11=check_op1(q[0])
				
				if(q[1].isdigit()):
					lit.append(q[1])
				
				op22=check_op2(q[1])
			       
				addr=addr_cal(q[0],q[1],addr,cnt1)
				cnt1 +=1

			print "\n  "+str(cnt1)+"\t\t"+p[k]+"-"+str(op_no)+"\t\t"+str(len(q))+"\t\t  "+op11+"\t    "+op22+"\t   "+'{0:04}'.format(addr)+"\t\t "+p[k]+" "+p[k+1]	
#-----------------------------------------------sy & value creation------------------------------------------------

for i in range(0,len(p)):

	if(p[i]!='.bss'):
		section1='data'

	if(p[i]=='main'):
		section1='text'
		sym.append(p[i])
	 	size1.append('-')
		sym_value.append('-')
		dddb.append('-')
	
	if(p[i]=='dd' or p[i]=='db' or p[i]=='dq'):
		if(p[i]=='dd'):
		 size1.append('4')
		else:
		 size1.append('1')

		dddb.append(p[i])
		sym.append(p[i-1])
		sym_value.append(p[i+1])

	if(p[i]=='main:'):
		m=i+1

		check_operands(m)
		break			
#---------------------------------------print literal table---------------------------------------------------------
def lit_print():
	
	f=open("Literals.txt","w")	

	print "\n\n\n Literal_No \t Value \t\t   Hex "

	for i in range(0,len(lit)):
		hex_no=hex(int(lit[i]))

		f.write("\n\n  " +str(i+1)+"\t\t  "+lit[i]+"\t\t   "+hex_no)
		print "\n  "+str(i+1)+"\t\t  "+lit[i]+"\t\t   "+hex_no

	print "\n\n"
	
	f.close 
#---------------------------------------print symbol table----------------------------------------------------------
f1=open("symbol.txt","w")	

print "\n\n\n\n Symbol_No \t Symbols \t Data type  \t   Size  \t Section \t Value "

for i in range(0,len(sym)):
	f1.write("\n  "+str(i+1)+"\t\t "+sym[i]+"\t\t   "+dddb[i]+"\t\t    "+size1[i]+"\t\t  "+section1+"\t\t "+sym_value[i])

	print "\n  "+str(i+1)+"\t\t "+sym[i]+"\t\t   "+dddb[i]+"\t\t    "+size1[i]+"\t\t  "+section1+"\t\t "+sym_value[i]

lit_print()
