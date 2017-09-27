#include <stdio.h>

int main()
{
	char sentence[100];
	int i, counter = 0, count = 0;
	printf("Enter a sentence: ");
	fgets(sentence, 100, stdin);
	printf("%s", sentence);
	for (i = 0; i < 100; i++)
	{
		if (sentence[i] == '.')
		{
			counter++;
			printf("Length of word %d is %d\n", counter, count);
			break;
		}
		else if (sentence[i] == ' ')
		{
			counter++;
			printf("Length of word %d is %d\n", counter, count);
			count = 0;
		}
		else if (sentence[i] == '\0')
		{
			break;
		}
		else
		{
			count++;
		}
	}
}
