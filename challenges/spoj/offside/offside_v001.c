#include <stdio.h>
#include <string.h>

int MAX_DISTANCE = 10000;


int main(void) {
  int n_attack, n_defense, i;
  int attack[11], defense[11];
  int min_attack, min_attack2, min_defense, min_defense2;

  scanf("%i %i", &n_attack, &n_defense);
  while(n_attack != 0 && n_defense != 0) {
    min_attack = min_defense = min_defense2 = MAX_DISTANCE + 1;

    for(i = 0; i < n_attack; i++) {
      scanf("%i", &attack[i]);

      if(min_attack > attack[i]) {
        min_attack = attack[i];
      }
    }

    for(i = 0; i < n_defense; i++) {
      scanf("%i", &defense[i]);

      if(min_defense > defense[i]) {
        min_defense2 = min_defense;
        min_defense = defense[i];
      } else if(min_defense2 > defense[i]) {
        min_defense2 = defense[i];
      }
    }

    if(min_attack < min_defense2) {
      printf("Y\n");
    } else {
      printf("N\n");
    }

    scanf("%i %i", &n_attack, &n_defense);
  }

	return 0;
}
