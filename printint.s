@ comp1203 template code
@ shows how to print an integer with printf

.data
        .balign  4
	fmtstring: .asciz "%d\n"
.text
        .global main
	.extern printf

main:
push {lr}			@ save link register as we will re-use it here
	@ our code here
	ldr r1, =1000000
	mov r0, #2
        mul     r0, r0, r1

	@ print the result that we have stored in r0
	mov r1, r0		
	ldr r0, =fmtstring
	bl printf

pop {lr}			@ get original values for return to shell
bx lr
