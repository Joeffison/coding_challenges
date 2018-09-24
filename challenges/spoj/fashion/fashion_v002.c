#include <stdio.h>
#include <stdlib.h>

int MAX_N = 1000;

int compare_int(const void * a, const void * b) {
   return (*(int*)a - *(int*)b);
}


int main(void) {
	int n_test_cases, n_participants, result;
	scanf("%i", &n_test_cases);
	int group1[MAX_N], group2[MAX_N];

	for(int i = 0; i < n_test_cases; i++){
    scanf("%i", &n_participants);

    for(int j = 0; j < n_participants; j++){
      scanf("%i", &group1[j]);
    }

    for(int j = 0; j < n_participants; j++){
      scanf("%i", &group2[j]);
    }

    qsort(group1, n_participants, sizeof(int), compare_int);
    qsort(group2, n_participants, sizeof(int), compare_int);

    result = 0;
    for(int j = 0; j < n_participants; j++){
      result += group1[j] * group2[j];
    }
    printf("%i\n", result);
	}

	return 0;
}
