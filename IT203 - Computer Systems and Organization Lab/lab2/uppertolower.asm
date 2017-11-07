.model small

.data
	input db "Enter a uppercase character: $"
	output db 10,"Lower case: $"

.code
	mov ax,@data
	mov ds,ax

	lea dx,input
	mov ah,9h
	int 21h

	mov ah,1h
	int 21h
	add al,32

	lea dx,output
	mov ah,9h
	int 21h

	mov dl,al
	mov ah,2h
	int 21h

	mov ah,4ch
	int 21h
end