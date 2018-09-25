#include <stdio.h>
#include <math.h>

int main(void) {
	float g1, g2;
	while(scanf("%f %f", &g1, &g2)){
	  if(g1 == -1) {
	    break;
	  } else if(g1 == 0 & g2 == 0) {
      printf("0\n");
	  } else if(g1 > g2) {
      printf("%i\n", (int) ceil(g1 / (g2 + 1)));
	  } else {
      printf("%i\n", (int) ceil(g2 / (g1 + 1)));
	  }
	}

	return 0;
}
