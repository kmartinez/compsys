@ comp1203 template code
@ print stack pointer before and after pushing a register to stack
.data
        .balign  4
        fmtstring: .asciz "%u\n"
.text
        .global main
        .extern printf

main:
        @ this is the reg we'll push to the stack
        ldr r3, =9999

        @ copy stack pointer and print it
        mov r1, sp
        ldr r0, =fmtstring
        push {lr}                       @ save link register
        bl printf
        pop {lr}                        @ get original lr

        push {r3}                       @ push r3 onto stack

        @ copy stack pointer and print it again
        mov r1, sp

        ldr r0, =fmtstring
        push {lr}                       @ save link register
        bl printf

        pop {lr}                        @ get original lr

bx lr
