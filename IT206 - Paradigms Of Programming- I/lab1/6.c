#include <stdio.h>

int main()
{
	int n, smallest, largest, s_pos, l_pos, temp, element, i;
	printf("Enter the length of the array: ");
	scanf("%d", &n);
	int ar[n];
	for (i = 0; i < n; i++)
	{
		printf("Enter element %d: ", i + 1);
		scanf("%d", &element);
		ar[i] = element;
	}
	printf("Original array:\n");
	for (i = 0; i < n; i++)
	{
		printf("%d ", ar[i]);
	}
	printf("\n");
	smallest = ar[0];
	largest = ar[0];
	s_pos = 0;
	l_pos = 0;
	for (i = 1; i < n; i++)
	{
		if (ar[i] < smallest)
		{
			smallest = ar[i];
			s_pos = i;
		}
		if (ar[i] > largest)
		{
			largest = ar[i];
			l_pos = i;
		}
	}
	temp = ar[s_pos];
	ar[s_pos] = ar[l_pos];
	ar[l_pos] = temp;
	printf("Modified array:\n");
	for (i = 0; i < n; i++)
	{
		printf("%d ", ar[i]);
	}
	printf("\n");
	return 0;
}