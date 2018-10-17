#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MACHULA "machula"
#define MAX_FACTOR_LENGTH = 18

#define has_machula(x) strstr(x, MACHULA) != NULL
#define to_int(x) ((int) strtol(x, (char **)NULL, 10))

int main(void) {
	char a[1024];
	char b[1024];
	char c[1024];

	int n;
  scanf("%i", &n);

	for(int i = 0; i < n; i++){
    scanf("\n%1023s + %1023s = %1023s", a, b, c);

    if(has_machula(a)) {
      printf("%i + %s = %s\n", (to_int(c) - to_int(b)), b, c);
    } else if(has_machula(b)) {
      printf("%s + %i = %s\n", a, (to_int(c) - to_int(a)), c);
    } else {
      printf("%s + %s = %i\n", a, b, (to_int(a) + to_int(b)));
    }
	}

	return 0;
}
