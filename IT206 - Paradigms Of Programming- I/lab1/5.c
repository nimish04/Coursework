#include <stdio.h>

int main()
{
	int n1, n2, track1, track2, trackf, temp, element, i, j;
	printf("Enter the length of the first array: ");
	scanf("%d", &n1);
	printf("Enter the length of the second array: ");
	scanf("%d", &n2);
	int a1[n1], a2[n2], final[n1 + n2], FINAL[n1 + n2];
	for (i = 0; i < n1; i++)
	{
		printf("Enter element %d of array 1: ", i + 1);
		scanf("%d", &element);
		a1[i] = element;
	}
	for (i = 0; i < n2; i++)
	{
		printf("Enter element %d of array 2: ", i + 1);
		scanf("%d", &element);
		a2[i] = element;
	}
	for (i = 0; i < n1; i++)
	{
		for (j = 0; j < n1 - i - 1; j++)
		{
			if (a1[j] > a1[j + 1])
			{
				temp = a1[j];
				a1[j] = a1[j + 1];
				a1[j + 1] = temp;
			}
		}
	}
	for (i = 0; i < n2; i++)
	{
		for (j = 0; j < n2 - i - 1; j++)
		{
			if (a2[j] > a2[j + 1])
			{
				temp = a2[j];
				a2[j] = a2[j + 1];
				a2[j + 1] = temp;
			}
		}
	}
	track1 = 0;
	track2 = 0;
	trackf = 0;
	while (1)
	{
		if ((track1 < n1) && (a1[track1] <= a2[track2]))
		{
			final[trackf] = a1[track1];
			track1++;
			trackf++;
		}
		else if (track2 < n2)
		{
			final[trackf] = a2[track2];
			track2++;
			trackf++;
		}
		else
		{
			break;
		}
	}
	printf("ARRAY\n");
	for (i = 0; i < n1 + n2; i++)
	{
		printf("%d ", final[i]);
	}
	printf("\n");
	return 0;
}