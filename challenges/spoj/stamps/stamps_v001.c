#include <stdio.h>
#define MAX_FRIENDS 1000
#define NO_ANSWER "impossible"


int main(void) {
  long n_test_cases, n_stamps, n_friends;
  long friends[MAX_FRIENDS];
  long sum_result, i, j, k, swap;

  scanf("%li", &n_test_cases);
  for(i = 1; i <= n_test_cases; i++) {
    scanf("%li %li", &n_stamps, &n_friends);

    if (n_stamps == 0 || n_friends == 0) {
      j = sum_result = 0;

      // discard input
      while (n_friends--) {
        scanf("%li", &friends[j]);
      }
    } else {
      scanf("%li", &friends[0]);
      for (j = 1; j < n_friends; j++) {
        scanf("%li", &friends[j]);

        // sorting number of stamps (descending)
        // in order to borrow the stamps from those who have more
        for (k = j - 1; k >= 0 && friends[k + 1] > friends[k]; k--) {
          swap = friends[k];
          friends[k] = friends[k + 1];
          friends[k + 1] = swap;
        }
      }

      sum_result = 0;

      // as the stamp counts are ordered in descending order,
      // j will be the minimum number of friends from whom Lucy can borrow stamps
      for (j = 0; j < n_friends && sum_result < n_stamps; j++) {
        sum_result += friends[j];
      }
    }

    if (sum_result < n_stamps) {
      printf("Scenario #%li:\n%s\n\n", i, NO_ANSWER);
    } else {
      printf("Scenario #%li:\n%li\n\n", i, j);
    }
  }

	return 0;
}
