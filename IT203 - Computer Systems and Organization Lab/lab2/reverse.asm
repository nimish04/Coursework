.model small

.data
	string db "hello$"
	reverse db "hello$"
	len dw 5

.code
	mov ax,@data
	mov ds,ax

	mov cx,len
	mov bx,0
	dec len

	A:
		mov si,len
		sub si,bx
		mov dl,string[si]
		mov si,bx
		mov reverse[si],dl
		inc bx
	loop A

	inc len
	mov si,len
	mov dl,'$'
	mov string[si],dl
	
	lea dx,reverse
	mov ah,9h
	int 21h


	mov ah,4ch
	int 21h
end