#include <stdio.h>

int main()
{
	char op;
	float a, b;
	printf("Enter 1, 2, 3 or 4 for addition, substraction, multiplicattion or division respectively: ");
	scanf("%c", &op);
	if ((op == '1') || (op == '2') || (op == '3') || (op == '4'))
	{
		printf("Enter the first number: ");
		scanf("%f", &a);
		printf("Enter the second number: ");
		scanf("%f", &b);
		if ((b == 0.0) && (op == '4'))
		{
			printf("Division by 0 not possible.\n");
			return 0;
		}
		switch (op)
		{
			case '1':
				printf("%f\n", a + b);
				break;
			case '2':
				printf("%f\n", a - b);
				break;
			case '3':
				printf("%f\n", a * b);
				break;
			case '4':
				printf("%f\n", a / b);
				break;
		}
	}
	else
	{
		printf("Invalid option.\n");
	}
	return 0;
}
