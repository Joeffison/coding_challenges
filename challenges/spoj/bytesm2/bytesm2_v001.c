#include <stdio.h>

int max(long long a, long long b) {
	return a > b? a : b;
}

int main(void) {
  int n_test_cases, h, w, i, j;
  long long int result;

  scanf("%i", &n_test_cases);
  while(n_test_cases--) {
    scanf("%i%i", &h, &w);

    long long int dp[101][101] = {0};
    for(i = 1; i < h; i++) {
      for(j = 1; j <= w; j++) {
        scanf("%lli", &dp[i][j]);
        dp[i][j] += max(dp[i-1][j], max(dp[i-1][j-1], dp[i-1][j+1]));
      }
    }

    result = 0;
    for(j = 1; j <= w; j++) {
      scanf("%lli", &dp[h][j]);
      dp[i][j] += max(dp[h-1][j], max(dp[h-1][j-1], dp[h-1][j+1]));
      result = max(result, dp[h][j]);
    }

    printf("%lli\n", result);
  }

	return 0;
}
