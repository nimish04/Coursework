#include <stdio.h>

int main()
{
	int i;
	char str[100], new[100];
	printf("Enter the string: ");
	fgets(str, 100, stdin);
	for (i = 0 ; i < 100; i++)
	{
		new[i] = str[i];
	}
	printf("%s", new);
	return 0;
}
