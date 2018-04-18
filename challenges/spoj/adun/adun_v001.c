#include <stdio.h>
#include <stdlib.h>

int main(void) {
	long int a, b;
	scanf("%li%li", &a, &b);
	a += b;
	printf("%li", a);
	return EXIT_SUCCESS;
}
