#include <stdio.h>
#include <string.h>

int main(void) {
  long long int n_test_cases, third, third_last, sum;
  long long int n, factor, last_computed;
  scanf("%lli", &n_test_cases);

	for(long long int i = 0; i < n_test_cases; i++) {
    scanf("%lli %lli %lli", &third, &third_last, &sum);

    n = (2 * sum) / (third + third_last);
    factor = (third_last - third) / (n - 5);

    printf("%lli\n", n);

    last_computed = third - (2 * factor);
    for(long long int j = 1; j < n; j++) {
      printf("%lli ", last_computed);
      last_computed += factor;
    }
    printf("%lli\n", last_computed);
	}

	return 0;
}
