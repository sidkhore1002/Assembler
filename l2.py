import lst2
import lst3
import sym3
import sym4

addr=0
addr2=0
cnt=0
cnt2=0
print "\n\t\t\t\t\t<    section .data>"
lst2.data_addr_cal(addr,cnt)
lst3.data_addr_cal(addr,cnt)
print "\n\t\t\t\t\t<    section .bss>"
lst2.bss_addr_cal(addr2,cnt2)
lst3.bss_addr_cal(addr2,cnt2)

f=open("s1.asm")

s=f.readlines()
ss=[]

for i in range(len(s)):
		s[i]=s[i].replace('\t','')
		s[i]=s[i].replace('\n','')
		ss.append(s[i])
print "\n"

sss=[]
for i in range(len(ss)):
	if(ss[i]==''):
		pass
	else:
		sss.append(ss[i])


kk=0
addr3=0
for i in range(len(sss)):
	if('main:' in sss[i]):
		kk=i+1
		print '\t\t\t\t\t'+'<    main:>\n'	
		lst2.main1_cal(kk,addr3)
		break


kk=0
addr3=0
for i in range(len(sss)):
	if('main:' in sss[i]):
		kk=i+1
		#print '\t\t\t\t\t'+'main:\n'	
		lst3.main1_cal(kk,addr3)
		break





