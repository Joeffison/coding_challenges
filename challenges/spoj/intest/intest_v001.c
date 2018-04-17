#include <stdio.h>
#include <stdlib.h>

int main(void) {
	long int n, k, input, i = 0, count = 0;
	scanf("%li%li", &n, &k);
	for(; i<n; i++) {
		scanf("%li", &input);
		count += (input%k == 0) ? 1 : 0;
	}
	printf("%li", count);
	return EXIT_SUCCESS;
}
