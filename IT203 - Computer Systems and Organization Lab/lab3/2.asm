.model small

.data
	string db "Information Technology$"
	len dw 22
	msg1 db "Enter the letter: $"
	msg2 db 10,"$"
	letter db ?

.code
	mov ax,@data
	mov ds,ax

	lea dx,msg1
	mov ah,9h
	int 21h

	mov ah,1h
	int 21h

	mov si,0
	mov cx,len
	mov bx,0

	A:
		cmp string[si],al
		je incr
		jmp over
		incr:
			add bx,1
		over:
			inc si
	loop A

	lea dx,msg2
	mov ah,9h
	int 21h

	add bx,'0'
	mov dx,bx
	mov ah,2h
	int 21h

	mov ah,4ch
	int 21h
end