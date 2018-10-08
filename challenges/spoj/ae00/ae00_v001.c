#include <stdio.h>
#include <math.h>

int main(void) {
	int n, result = 0;
  scanf("%i", &n);

  for(int i = 0; i < floor(sqrt(n)); i++){
    result += n/(i + 1) - i;
  }

  printf("%i", result);

	return 0;
}
