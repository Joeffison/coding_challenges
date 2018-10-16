#include <stdio.h>

int main(void) {
	long long int n;

	int n_test_cases;
  scanf("%i", &n_test_cases);
	for(int i = 0; i < n_test_cases; i++){
    scanf("%lli", &n);
	  printf("%lli\n", ((n*(3*n + 1)/2) % 1000007));
	}

	return 0;
}
