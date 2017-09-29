.model small

.stack 100h

.data
	msg db 10,13,'Enter a number: $'
	msg2 db 10,13,'Sum: $'
	x db 0
	y db 0

.code
	ADDITION proc
		mov ax,@data
		mov ds,ax

		mov ah,9h
		lea dx,msg
		int 21h

		mov ah,1h
		int 21h
		sub al,'0'
		mov x,al

		mov ah,9h
		lea dx,msg
		int 21h

		mov ah,1h
		int 21h
		sub al,'0'
		mov y,al

		mov ah,9h
		lea dx,msg2
		int 21h

		mov dl,x
		add dl,y
		add dl,'0'

		mov ah,2h
		int 21h

		mov ah,4ch
		int 21h
	ADDITION endp
	end ADDITION