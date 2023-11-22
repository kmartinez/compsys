@ comp1203 template code
@ shows how to print an integer with printf
@ which uses r0 for its format string and r1 as the parameter we're printing
@ note we stash link register lr with push
@ as printf will reuse lr to get back to our code after our 
.data
        .balign  4
	fmtstring: .asciz "%d\n"
.text
        .global main
	.extern printf

main:
push {lr}			@ save link register as we will re-use it here
	@ our code here
	ldr r3, =1000000
	mov r2, #2
        mul r1, r2, r3
	
	@ print the result that we have stored in r1 - don't change any code below	
	ldr r0, =fmtstring
	bl printf

pop {lr}			@ get original values for return to shell
bx lr
