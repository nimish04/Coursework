.model small

.data
	strmsg db "String: $"
	msg db "This is NITK$"
	inpmsg db 10, 13, "Enter a character: $"
	character db ?
	len dw 12
	occurences db 0
	newline db 10, 13, '$'

.code
	mov ax, @data
	mov ds, ax
	
	lea dx, strmsg
	mov ah, 9h
	int 21h

	lea dx, msg
	mov ah, 9h
	int 21h

	lea dx, inpmsg
	mov ah, 9h
	int 21h

	mov ah, 1h
	int 21h

	mov character, al
	mov cx, len
	mov di, cx
	sub di, 1

	A:
		mov al, msg[di]
		cmp character, al
		jne nextloop
		mov dl, occurences
		add dl, 1
		mov occurences, dl
		nextloop:
			sub di, 1
	loop A

	lea dx, newline
	mov ah, 9h
	int 21h

	mov dl, occurences
	add dl, '0'
	mov ah, 2h
	int 21h

	mov ah, 4ch
	int 21h
end