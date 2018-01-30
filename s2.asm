section .data
	msg db "adition-",10,0
	p dd 24
	q dd 19
	r dq 5.6

section .bss
	p1 resd 12
	p2 resb 10


section .text

	extern printf
	global main

main: 	
	mov eax,12
	mov dword[r],26
	mov eax,11

	mov ebx,dword[p]
	mov ebx,dword[q]
	mov dword[p],19

	mov ebx,dword[r]

	mov dword[p],20
	mov dword[q],27


