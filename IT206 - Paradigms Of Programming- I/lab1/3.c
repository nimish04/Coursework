#include <stdio.h>

int main()
{
	int numbers[5];
	int *ptr = numbers;
	for (int i = 0; i < 5; i++)
	{
		printf("Enter element %d: ", i + 1);
		scanf("%d", ptr);
		ptr++;
	}
	for (int j = 0; j < 5; j++)
	{
		printf("%d\n", numbers[j]);
	}
	return 0;
}