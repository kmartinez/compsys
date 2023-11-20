# a simple loop
# adding up the counter from 1 to 5
# comp1203 template code

.data
.balign  4
fmtstring: .asciz "%d\n"
.text
.global main
.extern printf

main:
push {lr}			@ save link register as we will re-use it here
@ our code here
    mov r1, #0       @ r1 ← 0 is our sum 
    mov r2, #1       @ r2 ← 1  our counter
loop: 
    cmp r2, #5       @ compare r2 to our limit
    bgt end          @ branch if r2 > limit to end 
    add r1, r1, r2   @ r1 ← r1 + r2 
    add r2, r2, #1   @ r2 ← r2 + 1
    b loop
end:
    mov r0, r1       @ r0 ← r1

	@ print the result that we have stored in r0
	mov r1, r0		
	ldr r0, =fmtstring
	bl printf

pop {lr}			@ get original values for return to shell
bx lr




  

