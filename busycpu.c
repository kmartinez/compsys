/* simple code to do one billion arithmetic/logic loops
* about 11 instructions per loop on an ARM Cortex A53/72
* when compiled with gcc -O -o busycpu busycpu.c
* you can look at the assembler with gcc -S -O busycpu.c which makes busycpu.s
* time your run and calculate billions of Instructions Per Second
*/
#include <stdio.h>
#define NUM 1000000000
void main()
{
	int a,b,c;
	b = 0;
	for(a = 0; a < NUM; a++)
	{
		b += a & 0x01;
		b -= (a & 0x02);
		b += (a & 0x04);
		b -= (a & 0x08);
	}
	printf("%d\n",b);
}
