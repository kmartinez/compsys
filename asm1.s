# simple operation returning result in r0 which is the return value to shell
# so echo $? will print it afterwards (only one byte)
.arm
.text
.global main
main:
	ldr r0, =5
	mov r1, #4
	add r0, r0, r1
	bx lr
