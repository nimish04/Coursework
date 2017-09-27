#include <stdio.h>

int main()
{
	int n, i;
	printf("Enter size of the array: ");
	scanf("%d", &n);
	float ar[n];
	for (i = 0; i < n; i++)
	{
		printf("Enter element %d: ", i);
		scanf("%f", &ar[i]);
	}
	for (i = n - 1; i > -1; i--)
	{
		printf("%f\n", ar[i]);
	}
	return 0;
}
