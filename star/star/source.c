#include <stdio.h>


int main(void)

{
	int a, b, c,i,j,k;
	for (a = 0; a < 5; a++)
	{ 
		for (b = 0; b < 5 - a; b++)
		{
			printf(" ");
		}
		for (c = 0; c < a * 2 + 1; c++)
		{
			printf("*");
		}
		printf("\n");
	}
	for (i = 4; i > 0; i--)
	{
		for(j=0; j<6-i; j++)
		{
			printf(" ");
		}
		for (j = 0; j<i*2-1; j++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}