.model small

.stack 100h

.data
	msg1 db 10,13,'Enter first number: $'
	msg2 db 10,13,'Enter second number: $'
	msg3 db 10,13,'Product: $'
	x db 0
	y db 0

.code
	PRODUCT proc
		mov ax,@data
		mov ds,ax

		mov ah,9h
		lea dx,msg1
		int 21h

		mov ah,1h
		int 21h
		sub al,'0'
		mov x,al

		mov ah,9h
		lea dx,msg2
		int 21h

		mov ah,1h
		int 21h
		sub al,'0'
		mov y,al

		mov ah,9h
		lea dx,msg3
		int 21h

		mov ax,x
		mul y
		mov dl,ax
		add dl,'0'

		mov ah,2h
		int 21h

		mov ah,4ch
		int 21h
	PRODUCT endp
	end PRODUCT