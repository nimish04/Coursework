#include <stdio.h>

int main()
{
	int n, track_beg, track_mid1, track_mid2, i, j, k, l;
	printf("Enter n: ");
	scanf("%d", &n);
	track_beg = 0;
	track_mid1 = n - 1;
	track_mid2 = n - 2;
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= track_beg; j++)
		{
			printf(" ");
		}
		printf("%d", i);
		for (k = 1; k <= track_mid1; k++)
		{
			printf(" ");
		}
		for (l = 1; l <= track_mid2; l++)
		{
			printf(" ");
		}
		if (i != n)
		{
			printf("%d", i);
		}
		printf("\n");
		track_beg++;
		track_mid1--;
		track_mid2--;
	}
	track_beg = n - 2;
	track_mid1 = 1;
	track_mid2 = 0;
	for (i = n - 1; i >= 1; i--)
	{
		for (j = 1; j <= track_beg; j++)
		{
			printf(" ");
		}
		printf("%d", i);
		for (k = 1; k <= track_mid1; k++)
		{
			printf(" ");
		}
		for (l = 1; l <= track_mid2; l++)
		{
			printf(" ");
		}
		if (i != n)
		{
			printf("%d", i);
		}
		printf("\n");
		track_beg--;
		track_mid1++;
		track_mid2++;
	}
	return 0;
}