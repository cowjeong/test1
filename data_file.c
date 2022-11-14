#define _CRT_SECURE_NO_WARNINGS //���� ������ ���� ������ �����ϱ� ����
#include <stdio.h>
#include <string.h> //���ڿ��� ���� �������
#define SIZE 5  //���Ŀ� �ʿ�� ������ �����ϵ��� ������� ����, �켱 5�� ������

typedef struct _Student
{
	char name[20];  //�̸�
	int number;     //�й�
	double grade;   //����
}Student; //����ü�� ��Ī�� ����, ��������

void print_student_data(Student* student, char name[20]); //�Լ��� ���� ����

int main()
{
	Student student[SIZE] = {           //����ü �迭�� �ʱ�ȭ
		{"Kim", 2022001, 4.1},
		{"Lee", 2022002, 3.8},
		{"Park",2022003, 3.2},
		{"Choi", 2022004, 4.0},
		{"Jeong", 2022005, 4.5},
	};
	
	while(1)
	{
		printf("ã�� �л��� �̸��� �Է��ϼ��� : ");//�л� ������ ����ϱ� �� �̸��� �Է¹ޱ� ����
		char name[20];
		scanf("%s", name);                     //�̸� �Է� ����
		print_student_data(student, name);     //�л� ������ ����ϴ� �Լ� ȣ��
	}
}

void print_student_data(Student* student, char name[20]) //�л� ������ ����ϴ� �Լ�
{
	printf("--------(%s)�л��� ���� ���--------\n", name);
	for (int i = 0; i < SIZE; i++) 
	{
		if (strcmp(name, student[i].name) == 0) //�Է� ���� name�� ����ü �迭�� name��
			                                    //������ ��, ������ (�̸�, �й�, ����)���
		{
			printf("�̸�:%s  �й�:%d  ����:%.1lf \n\n",     
				student[i].name, student[i].number, student[i].grade);
			return;
		}
	}
	printf("ã�� �л��� �������� �ʽ��ϴ�.\n");  
}