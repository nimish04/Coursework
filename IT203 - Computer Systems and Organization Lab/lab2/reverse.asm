.model small

.data
	string db "hello$"
	reverse db ?
	len dw 5

.code
	mov ax,@data
	mov ds,ax

	mov cx,len
	mov si,0
	mov di,len
	dec di

	A:
		mov dl,string[di]
		mov reverse[si],dl
		inc si
		dec di
	loop A

	mov al,'$'
	mov reverse[si],al

	lea dx,reverse
	mov ah,9h
	int 21h

	mov ah,4ch
	int 21h
end
