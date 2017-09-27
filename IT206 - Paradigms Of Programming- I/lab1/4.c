#include <stdio.h>

int main()
{
	int m1, n1, m2, n2, element, i, j, k;
	printf("Enter the number of rows for matrice 1: ");
	scanf("%d", &m1);
	printf("Enter the number of columns for matrice 1: ");
	scanf("%d", &n1);
	printf("Enter the number of rows for matrice 2: ");
	scanf("%d", &m2);
	printf("Enter the number of columns for matrice 2: ");
	scanf("%d", &n2);
	if (n1 != m2)
	{
		printf("Cannot multiply the two matrices of the given order");
		return 0;
	}
	int first[m1][n1], second[m2][n2], final[m1][n2];
	for (i = 0; i < m1; i++)
	{
		for (j = 0; j < n1; j++)
		{
			printf("Enter element in row %d and col %d for matrix 1: ", i + 1, j + 1);
			scanf("%d", &element);
			first[i][j] = element;
		}
	}
	for (i = 0; i < m2; i++)
	{
		for (j = 0; j < n2; j++)
		{
			printf("Enter element in row %d and col %d for matrix 2: ", i + 1, j + 1);
			scanf("%d", &element);
			second[i][j] = element;
		}
	}
	printf("MATRIX 1\n");
	for (i = 0; i < m1; i++)
	{
		for (j = 0; j < n1; j++)
		{
			printf("%d ", first[i][j]);
		}
		printf("\n");
	}
	printf("MATRIX 2\n");
	for (i = 0; i < m2; i++)
	{
		for (j = 0; j < n2; j++)
		{
			printf("%d ", second[i][j]);
		}
		printf("\n");
	}
	for (i = 0; i < m1; i++)
	{
		for (j = 0; j < n2; j++)
		{
			final[i][j] = 0;
			for (k = 0; k < n1; k++)
			{
				final[i][j] += first[i][k] * second[k][j];
			}
		}
	}
	printf("MULTIPLIED MATRIX\n");
	for (i = 0; i < m1; i++)
	{
		for (j = 0; j < n2; j++)
		{
			printf("%d ", final[i][j]);
		}
		printf("\n");
	}
	return 0;
}