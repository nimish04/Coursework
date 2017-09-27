#include <stdio.h>
int main()
{
	int n;
	printf("Enter length of the array: ");
	scanf("%d", &n);
	int ar[n], i, j, k;
	for (i = 0; i < n; i++)
	{
		scanf("%d", &ar[i]);
	}
	for (j = 0; j < n; j++)
	{
		if ((ar[j] % 2) == 0)
		{
			ar[j] = 0;
		}
		else
		{
			ar[j] = 1;
		}
	}
	printf("New array:\n");
	for (k = 0; k < n; k++)
	{
		printf("%d\n", ar[k]);
	}
	return 0;
}
