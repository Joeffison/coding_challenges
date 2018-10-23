#include <stdio.h>
#include <string.h>

#define MAX_N 10000001

long int x[MAX_N];
long int y[MAX_N];

int main(void) {
  long int n_test_cases, n;
  x[0] = 1;
  y[0] = 1;

  x[1] = 1;
  y[1] = 2;

  x[2] = 2;
  y[2] = 1;

  x[3] = 3;
  y[3] = 1;

  x[4] = 2;
  y[4] = 2;

  long int processed = 5;
  long int direction = 1;
  long long int last_computed, factor;

  scanf("%li", &n_test_cases);
	while(n_test_cases--) {
    scanf("%li", &n);

    while(n > processed) {
      x[processed] = x[processed - 1] - direction;
      y[processed] = y[processed - 1] + direction;
      processed++;

      if(x[processed - 1] == 1) {
        x[processed] = 1;
        y[processed] = y[processed - 1] + 1;
        direction = -1;
        processed++;
      } else if(y[processed - 1] == 1) {
        x[processed] = x[processed - 1] + 1;
        y[processed] = 1;
        direction = 1;
        processed++;
      }
    }

    printf("TERM %li IS %li/%li\n", n, x[n - 1], y[n - 1]);
	}

	return 0;
}
