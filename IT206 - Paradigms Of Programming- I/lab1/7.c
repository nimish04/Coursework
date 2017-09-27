#include <stdio.h>

int main()
{
	char string[100], ch;
	printf("Enter the string: ");
	fgets(string, 100, stdin);
	printf("Enter the character you want to search for: ");
	scanf("%c", &ch);
	int positions[100], count, i, track = 0;
	while (string[track] != '\n')
	{
		if (string[track] == ch)
		{
			positions[count] = track;
			count++;
		}
		track++;
	}
	printf("Number of occurences: %d\n", count);
	printf("Positions: ");
	for (i = 0; i < count; i++)
	{
		printf("%d ", positions[i]);
	}
	printf("\n");
	return 0;
}