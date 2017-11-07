.model small

.data
	passwd db "abcd1234"
	msg db "Enter password: $"
	correct db 10,"Correct!$"
	incorrect db 10,"Incorrect!$"
	len dw 8

.code
	mov ax,@data
	mov ds,ax

	mov cx,len
	mov si,0

	lea dx,msg
	mov ah,9h
	int 21h

	A:
		mov ah,8h
		int 21h
		cmp al,passwd[si]
		jne wrong
		inc si
	loop A

	jmp right

	wrong:
		lea dx,incorrect
		jmp finish

	right:
		lea dx,correct
	
	finish:
		mov ah,9h
		int 21h

		mov ah,4ch
		int 21h
end