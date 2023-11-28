# a simple loop
# adding up the counter from 1 to 5
# print takes two args: r0 (format) and r1 (the value you want to print)
# comp1203 template code

.data
.balign  4
fmtstring: .asciz "%d\n"
.text
.global main
.extern printf

main:
push {lr}			@ save link register as we use it
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
	@ print value of r1
	ldr r0, =fmtstring
	bl printf

pop {lr}			@ get original values for return to shell
bx lr




  

