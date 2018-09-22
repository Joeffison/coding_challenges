#include <stdio.h>

int main(void) {
	int dp_feynman[101];
	dp_feynman[0] = 1;
	dp_feynman[1] = 5;
	int tail = 1;

	int n;
	while(1){
		scanf("%i", &n);
	  if(n-- == 0) {
      break;
	  }
	  for(int i = tail; i < n; i++){
      dp_feynman[++tail] = (i + 2)*(i + 2) + dp_feynman[i];
	  }
	  printf("%i\n", dp_feynman[n]);
	}

	return 0;
}
