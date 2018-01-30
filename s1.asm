section .data
	msg db "adition-",10,0
	a dd 22
	aa dd 2,44,56,-1
	b dd 20
	c dq 2.3

section .bss
	s1 resd 10
	s2 resb 10
	s3 resd 5


section .text

	extern printf
	global main

main: 	
	mov eax,10
	mov dword[c],20
	mov eax,10

	mov ebx,dword[a]
	mov ebx,dword[aa]
	mov dword[aa],20

	mov ebx,dword[b]

	mov dword[b],22
	mov dword[c],20


