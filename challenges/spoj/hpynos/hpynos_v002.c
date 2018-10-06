#include <stdio.h>

int break_number(int n) {
    int result = 0;

    int current_digit;
    while(n) {
        current_digit = n % 10;
        result += current_digit * current_digit;
        n /= 10;
    }

    return result;
}

int main(void) {
	int n, temp;
	int steps = 0;
	int intermediate[1000] = {0};

  scanf("%i", &n);

	while(1) {
    temp = break_number(n);
    if(intermediate[temp] == 0) {
      n = temp;
      intermediate[temp] = 1;
      steps++;
    } else {
      printf("-1\n");
      break;
    }

    if(n == 1) {
      printf("%d\n", steps);
      break;
    }
	}

	return 0;
}
