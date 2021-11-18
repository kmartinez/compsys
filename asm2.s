# a simple loop
# adding up the counter from 1 to 5
# return value to shell for printing with echo $?
.text
.global main
main:
    mov r1, #0       /* r1 ← 0 is our sum */
    mov r2, #1       /* r2 ← 1  our counter */
loop: 
    cmp r2, #5      /* compare r2 to our limit*/
    bgt end          /* branch if r2 > limit to end */
    add r1, r1, r2   /* r1 ← r1 + r2 */
    add r2, r2, #1   /* r2 ← r2 + 1 */
    b loop
end:
    mov r0, r1       /* r0 ← r1 */
    bx lr

