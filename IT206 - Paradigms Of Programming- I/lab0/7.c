#include <stdio.h>

struct product
{
	int productid;
	float unit_price;
}
products[4] =
{
	{123, 10.5},
	{234, 20.5},
	{345, 30.5},
	{456, 40.5},
};

int main()
{
	struct product *ptr = products;
	float total;
	int inp, inq;
	printf("Enter the product ID: ");
	scanf("%d", &inp);
	printf("Enter the product quantity: ");
	scanf("%d", &inq);
	for (int i = 0; i < 4; i++)
	{
		if (ptr->productid == inp)
		{
			total = ptr->unit_price * inq;
			printf("Total price: %f\n", total);
			break;
		}
		ptr++;
	}
	return 0;
}
