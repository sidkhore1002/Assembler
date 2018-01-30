f=open("s2.asm")

s=f.readlines()
ss=[]
sym=[]
sym_addr=[]

reg=['eax','0','ecx','1','edx','2','ebx','3','esi','6','edi','7']

for i in range(len(s)):
		s[i]=s[i].replace('\t','')
		s[i]=s[i].replace('\n','')
		ss.append(s[i])
#print ss
print "\n"

sss=[]
for i in range(len(ss)):
	if(ss[i]==''):
		pass
	else:
		sss.append(ss[i])



def data_addr_cal(addr,cnt):
	#print "\t\t\t\t\tsection .data"
	loc=0
	loc1=[]
	for i in range(len(ss)):
		if('db' in ss[i]):
			if(cnt==0):
				print '{0:08}'.format(0)+"\t\t\t\t\t"+ss[i]
				cnt=cnt+1
				sym.append('{0:08}'.format(0))
				a11=ss[i].split()
				sym.append(a11[0])
								
			addr=addr+2
			sym.append('{0:08}'.format(addr))

			if('dd' in ss[i+1]):
				a11=ss[i+1].split()
				sym.append(a11[0])
				a22=a11[2].split(',')
		
				if(len(a22)==1):
					loc=hex(int(a22[0]))
				else:	
					for i in range(len(a22)):
						loc1.append(hex(int(a22[i])))		
			print '{0:08}'.format(addr)+" "+loc+"\t\t\t\t\t"+ss[i+1]

		if('dd' in ss[i]):
			if(cnt==0):
				print '{0:08}'.format(0)+"\t\t\t\t\t"+ss[i]
				cnt=cnt+1
				sym.append('{0:08}'.format(0))
				a11=ss[i].split()
				sym.append(a11[0])
	
			a1=ss[i].split()
			a2=a1[2].split(',')
			addr=addr+(len(a2)*4)
			sym.append('{0:08}'.format(addr))

			if('dd' in ss[i+1]):
				a11=ss[i+1].split()
				sym.append(a11[0])
				a22=a11[2].split(',')
		
				if(len(a22)==1):
					loc=hex(int(a22[0]))
					print '{0:08}'.format(addr)+" "+loc+"\t\t\t\t\t"+ss[i+1]

				else:	
					for i in range(len(a22)):
						loc1.append(hex(int(a22[i])))		
					print '{0:08}'.format(addr)+" "+','.join(loc1)+"\t\t\t\t"+ss[i+1]
			if('dq' in ss[i+1]):
				a11=ss[i+1].split()
				sym.append(a11[0])
		
				loc=hex(int(a22[0]))
				print '{0:08}'.format(addr)+" "+loc+"\t\t\t\t\t"+ss[i+1]
			
		if('dq' in ss[i]):
			if(cnt==0):
				print '{0:08}'.format(0)+"\t\t\t\t\t"+ss[i]
				cnt=cnt+1

			addr=addr+8


def bss_addr_cal(addr2,cnt2):
	#print "\n\t\t\t\t\tsection .bss"
	lc=0
	for i in range(len(ss)):
		
		if('resb' in ss[i]):
			if(cnt2==0):
				print '{0:08}'.format(0)+"\t\t\t\t\t"+ss[i]
				cnt2=cnt2+1
			
			a1=ss[i].split()
			lc=hex(int(a1[2])*1)

			print '{0:08}'.format(addr2)+" "+lc+"\t\t\t\t\t"+ss[i]

		if('resd' in ss[i]):
			if(cnt2==0):
				a1=ss[i].split()
	
				lc=hex(int(a1[2])*4)
				addr2=addr2+(int(a1[2])*4)

				print '{0:08}'.format(0)+" "+lc+"\t\t\t\t\t"+ss[i]
				
				cnt2=cnt2+1
			else:					
				a1=ss[i-1].split()
				addr2=addr2+(int(a1[2])*1)
				
				a11=ss[i].split()
				lc=hex(int(a11[2])*4)
				print '{0:08}'.format(addr2)+" "+lc+"\t\t\t\t\t"+ss[i]
	
def text_print():
	for i in range(len(ss)):
		if('text' in ss[i]):
			print "\t\t\t\t\t"+ss[i]
			j=i+1
	for i in range(j,len(ss)):
		if('main:' in ss[i]):
			break
		else:			
			print "\t\t\t\t\t\t"+ss[i]


def main1_cal(k,addr3):
#	print sss[k]
	for i in range(k,len(sss)):
#		print '\n'

		if('mov' in sss[i]):

			s1=sss[i].split()
			s2=s1[1].split(',')							
			
			if(s2[0] in reg and s2[1].isdigit()):
				s3=hex(8+int(reg[reg.index(s2[0])+1]))
				h1=hex(int(s2[1]))
		
				st='B'+s3[2].upper()+'0'+h1[2].upper()+'000000'
				addr3=addr3+(len(st)/2)				
				print str('{0:08}'.format(addr3))+'  '+'B'+s3[2].upper()+'[0'+h1[2].upper()+'000000'+']'
				

			if(s2[0] in reg and 'dword' in s2[1]):
				s2[1]=s2[1].replace('dword','')
				s2[1]=s2[1].replace('[','')
				s2[1]=s2[1].replace(']','')
				
				if(s2[1] in sym):
					st='8B'+sym[(sym.index(s2[1])-1)]
					addr3=addr3+(len(st)/2)				
	
					print str('{0:08}'.format(addr3))+'  '+'8B['+sym[(sym.index(s2[1])-1)]+']'

			s2[0]=s2[0].replace('dword','')
			s2[0]=s2[0].replace('[','')
			s2[0]=s2[0].replace(']','')

			if(s2[0] in sym and s2[1].isdigit()):
					h1=hex(int(s2[1]))		

					st='c7'+'05'+sym[(sym.index(s2[0])-1)]+'0'+h1[2]+h1[3]+'000000'
					addr3=addr3+(len(st)/2)				

					print str('{0:08}'.format(addr3))+'  '+'C7'+'05 ['+sym[(sym.index(s2[0])-1)]+']'+'[0'+h1[2]+h1[3]+'000000]'+']'


addr=0		
addr2=0	
cnt=0
cnt2=0

#data_addr_cal(addr,cnt)
#bss_addr_cal(addr2,cnt2)
print "\n"



















