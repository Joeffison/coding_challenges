#include <stdio.h>

int main(void) {
	long long int n_test_cases, k;
	scanf("%lli", &n_test_cases);

	for(int i = 0; i < n_test_cases; i++){
		scanf("%lli", &k);
		printf("%lli\n", (192 + ((k - 1) * 250)));
	}

	return 0;
}
