#include <stdio.h>

struct student
{
	int roll;
	char name[100];
};

int main()
{
	int n, i, rollnumber;
	printf("Enter number of records: ");
	scanf("%d", &n);
	struct student records[n];
	for (i = 0; i < n; i++)
	{
		printf("Student %d\n", i + 1);
		printf("Enter roll number: ");
		scanf("%d", &records[i].roll);
		printf("Enter name: ");
		scanf("%s", records[i].name);
	}
	printf("Enter roll number of the student you want to search for: ");
	scanf("%d", &rollnumber);
	int flag = 0;
	for (i = 0; i < n; i++)
	{
		if (rollnumber == records[i].roll)
		{
			flag = 1;
			printf("Name of the student is %s\n", records[i].name);
			break;
		}
	}
	if (flag == 0)
	{
		printf("Not found.\n");
	}
	return 0;
}
