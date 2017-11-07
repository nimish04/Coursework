.model small

.data
	string db "hello",10,'$'
	count dw 5

.code
	mov ax,@data
	mov ds,ax

	mov cx,count

	A:
		lea dx,string
		mov ah,9h
		int 21h
	loop A
	
	mov ah,4ch
	int 21h
end