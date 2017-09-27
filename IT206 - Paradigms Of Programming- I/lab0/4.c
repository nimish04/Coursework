#include <stdio.h>

int main()
{
	int m, n, i, j;
	printf("Enter number of rows: ");
	scanf("%d", &m);
	printf("Enter number of columns: ");
	scanf("%d", &n);
	char op;
	float mat1[m][n], mat2[m][n];
	printf("MATRIX 1:\n");
	for (i = 0; i < m; i++)
	{
		for (j = 0; j < n; j++)
		{
			printf("Enter number in row %d and column %d: ", i + 1, j + 1);
			scanf("%f", &mat1[i][j]);
		}
	}
	printf("Enter 1, 2, 3 or 4 for adding, substracting, finding transpose or searching for an element: ");
	scanf(" %c", &op);
	if ((op == '1') || (op == '2'))
	{
		printf("MATRIX 2:\n");
		for (i = 0; i < m; i++)
		{
			for (j = 0; j < n; j++)
			{
				printf("Enter number in row %d and column %d: ", i + 1, j + 1);
				scanf("%f", &mat2[i][j]);
			}
		}
	}
	if (op == '1')
	{
		for (i = 0; i < m; i++)
		{
			for (j = 0; j < n; j++)
			{
				mat1[i][j] += mat2[i][j];
				printf("%f ", mat1[i][j]);
			}
			printf("\n");
		}
	}
	else if (op == '2')
	{
		for (i = 0; i < m; i++)
		{
			for (j = 0; j < n; j++)
			{
				mat1[i][j] -= mat2[i][j];
				printf("%f ", mat1[i][j]);
			}
			printf("\n");
		}
	}
	else if (op == '3')
	{
		printf("TRANSPOSE\n");
		float newmat[n][m];
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < m; j++)
			{
				newmat[i][j] = mat1[j][i];
				printf("%f ", newmat[i][j]);
			}
			printf("\n");
		}
	}
	else if (op == '4')
	{
		float numb;
		printf("Enter the element you want to search for: ");
		scanf("%f", &numb);
		int flag = 0;
		for (i = 0; i < m; i++)
		{
			for (j = 0; j < n; j++)
			{
				if (numb == mat1[i][j])
				{
					flag = 1;
					printf("Element in position %d %d\n", i + 1, j + 1);
				}
			}
		}
		if (flag == 0)
		{
			printf("Element not found.\n");
		}
	}
	else
	{
		printf("Incorrect option.\n");
	}
	return 0;
}
