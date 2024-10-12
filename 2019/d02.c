#include <stdio.h>

int main() {
	FILE* pFile = fopen("input.txt", "r");
	if (pFile == NULL) {
		perror("Read failure");
		return 1;
	}

	while(fscanf(pFile, "") != EOF) {
		
	}

	fclose(pFile);

	printf("%d\n", 0); // 

	return 0;
}