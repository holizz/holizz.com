/* http://www.craigmurphy.com/blog/?p=1417 */
#include <stdio.h>
int main(int argc, char * argv[]) {
  if (argc != 2) return 1;
  int b=1, c, i;
  for (c = 'A'; c >= 'A'; b?c>=argv[1][0]?b=c---c:c++:c--) {
    for (i = 2*c-argv[1][0]; i < 3*c-(2*'A'); i++) {
      if (i == c) printf("%c",c);
      else printf(" ");
    }
    printf("%c\n", c);
  }
}
