.model small

.data
	original db "Random String$"
	copy db ?
	len db 13

.code
	mov ax,@data
	mov ds,ax

	mov cx,len
	mov si,0
	A:
		mov dl,original[si]
		mov copy[si],dl
		inc si
	loop A

	mov al,'$'
	mov copy[si],al
	
	lea dx,copy
	mov ah,9h
	int 21h

	mov ah,4ch
	int 21h
end