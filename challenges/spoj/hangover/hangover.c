#include <stdio.h>

int main(void) {
  // max input is 5.20
	double dp[276];
	dp[0] = 0.5;
	dp[1] = 0.5 + 1.0/3.0;

	int last_index_computed = 1;

	float n;
  scanf("%f", &n);
	while(n){
	  if(n < 0.001){
	    break;
	  }

    int result = -1;
    double new_value;
	  while(dp[last_index_computed] < n) {
	    new_value = dp[last_index_computed] + 1.0/(3.0 + last_index_computed);
	    dp[++last_index_computed] = new_value;
      result = last_index_computed;
	  }
	  if(result == -1) {
	    for(result = 0; dp[result] < n; result++) {}
	  }
    result++;
    printf("%d card(s)\n", result);

		scanf("%f", &n);
	}

	return 0;
}
