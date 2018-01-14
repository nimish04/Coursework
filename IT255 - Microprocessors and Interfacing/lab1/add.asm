.model small

.data
	inpmsg db 10, 13, "Enter a number: $"
	outmsg db 10, 13, "Sum: $"
	x db ?
	y db ?

.code
	mov ax, @data
	mov ds, ax

	lea dx, inpmsg
	mov ah, 9h
	int 21h

	mov ah, 1h
	int 21h
	sub al, '0'
	mov x, al

	lea dx, inpmsg
	mov ah, 9h
	int 21h

	mov ah, 1h
	int 21h
	sub al, '0'
	mov y, al

	lea dx, outmsg
	mov ah, 9h
	int 21h

	mov al, x
	add al, y
	add al, '0'

	mov dl, al
	mov ah, 2h
	int 21h

	mov ah, 4ch
	int 21h
end