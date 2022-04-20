#include<stdio.h>

int main(void) {
	int num, cnt=0, sum=0;
	scanf("%d", &num);
	for (int i = 1; i <= num; i++) {
		int j = i;
		sum = 0;
		while (j / 10 > 0) {
			sum = sum + j % 10;
			j = j / 10;
		}
		if (j / 10 == 0) {
			sum = sum + j;
		}
		if (i % sum == 0) cnt++;
	}
	printf("%d",cnt);

	return 0;
}