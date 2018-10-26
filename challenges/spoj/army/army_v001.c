#include <stdio.h>

#define ARMY_1 "Godzilla\n"
#define ARMY_2 "MechaGodzilla\n"
#define NO_ANSWER "uncertain\n"


int main(void) {
  int n_test_cases, n_army_1, n_army_2, strongest_army_1, strongest_army_2, temp;

  scanf("%i", &n_test_cases);
  while(n_test_cases--) {
    scanf("\n%i %i", &n_army_1, &n_army_2);

    if (n_army_1 == 0) {
      if (n_army_2 == 0) {
        printf(NO_ANSWER);
      } else {
        printf(ARMY_2);

        // discard input
        while (n_army_2--) {
          scanf("%i", &strongest_army_2);
        }
      }
    } else if (n_army_2 == 0) {
      printf(ARMY_1);

      // discard input
      while (n_army_1--) {
        scanf("%i", &strongest_army_1);
      }
    } else {
      // get strongest in army 1
      scanf("%i", &strongest_army_1);
      n_army_1--;
      while(n_army_1--) {
        scanf("%i", &temp);

        if (temp > strongest_army_1) {
          strongest_army_1 = temp;
        }
      }

      // get strongest in army 2
      scanf("%i", &strongest_army_2);
      n_army_2--;
      while(n_army_2--) {
        scanf("%i", &temp);

        if (temp > strongest_army_2) {
          strongest_army_2 = temp;
        }
      }

      if (strongest_army_2 > strongest_army_1) {
        printf(ARMY_2);
      } else {
        printf(ARMY_1);
      }
    }
  }

	return 0;
}
