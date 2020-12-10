#include <stdio.h>

int fuelRequired(int mass) {
	return (int) (mass / 3) - 2;
}

int main() {
	FILE* pFile = fopen("input/day01.txt", "r");
	if (pFile == NULL) {
		perror("Read failure");
		return 1;
	}

	int mass;
	int sum = 0;

	while(fscanf(pFile, "%d", &mass) != EOF) {
		int fuel = fuelRequired(mass);
		sum += fuel;

		while ((fuel = fuelRequired(fuel)) > 0)
			sum += fuel;
	}

	fclose(pFile);

	printf("%d\n", sum); // 4934767

	return 0;
}