.model small

.data
	string db "NITK Information Technology$"
	len dw 27

.code
	mov ax,@data
	mov ds,ax

	mov si,0
	mov cx,len
	mov bx,0

	A:
		cmp string[si],"A"
		je incr
		cmp string[si],"E"
		je incr
		cmp string[si],"I"
		je incr
		cmp string[si],"O"
		je incr
		cmp string[si],"U"
		je incr
		cmp string[si],"a"
		je incr
		cmp string[si],"e"
		je incr
		cmp string[si],"i"
		je incr
		cmp string[si],"o"
		je incr
		cmp string[si],"u"
		je incr
		jmp over
		incr:
			add bx,1
		over:
			inc si
	loop A

	add bx,'0'
	mov dx,bx
	mov ah,2h
	int 21h

	mov ah,4ch
	int 21h
end