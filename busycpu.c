/* simple code to do a lot of arithmetic loops
* about 11 instr per loop on an ARM Cortex A53
* when compiled with gcc -O
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
