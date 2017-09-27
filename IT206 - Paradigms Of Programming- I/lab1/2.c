#include <stdio.h>

struct Bank
{
	int account_no;
	int pan_no;
	float balance;
	char name[100];
	int mobile;
};

void withdraw(struct Bank r)
{
	printf("Enter the amount you want to withdraw: ");
	int amount;
	scanf("%d", &amount);
	if (amount > r.balance)
	{
		printf("Insufficient funds.\n");
	}
	else
	{
		r.balance -= amount;
		printf("Successfully withdrawn.\n")
	}
}

void deposit(struct Bank r)
{
	printf("Enter the amount you want to deposit: ");
	int amount;
	scanf("%d", &amount);
	r.balance += amount;
	printf("Successfully deposited.\n");
}

int main()
{
	struct Bank record;
	printf("Enter bank account number: ");
	scanf("%d", &record.account_no);
	printf("Enter PAN card number: ");
	scanf("%d", &record.pan_no);
	printf("Enter bank balance: ");
	scanf("%f", &record.balance);
	int op;
	while (1)
	{
		printf("Enter 1 to withdraw, 2 to deposit, 3 to check balance and 4 to exit:\n");
		scanf("%d", &op);
		if (op == 4)
		{
			break;
		}
		switch (op)
		{
			case 1:
				withdraw(record);
				break;
			case 2:
				deposit(record);
				break;
			case 3:
				printf("Your balance is %f.\n", record.balance);
				break;
			default:
				printf("Please enter the correct option.\n");
		}
	}
	return 0;
}