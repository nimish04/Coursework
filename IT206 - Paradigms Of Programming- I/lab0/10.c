#include <stdio.h>

int main()
{
	FILE *fp = fopen("sample.txt", "r");
	int counter = 0;
	char ch = fgetc(fp);
	while (ch != EOF)
	{
		if (ch == '\n')
		{
			counter++;
		}
		ch = fgetc(fp);
	}
	fclose(fp);
	printf("Number of lines: %d\n", counter + 1);
	return 0;
}
