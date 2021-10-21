#include <stdio.h>
#define NUM 1000000000
void main()
{
	int a,b,c;
	b = 0;
	for(a = 0; a < NUM; a++)
	{
		b += a & 0x01;
	}
	printf("%d\n",b);
}
