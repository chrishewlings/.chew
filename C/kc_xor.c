#include <stdio.h>
#include <string.h>

#define NUM_ELEM(x) sizeof (x) / sizeof (*(x))

const int cipher[] = {0x7D, 0x89, 0x52, 0x23, 0xD2, 0xBC, 0xDD, 0xEA, 0xA3, 0xB9, 0x1F};
int ciphered_text[];

/*
void xor_encode(*input, *output){
#TODO 
}
*/
int main(int argc, char const *argv[]) {

    if (argc != 2) {
        printf("This script requires a kcpasswd file as its only argument.\nTypically it is found at /etc/kcpasswd. If it does not exist, automatic login\n is most likely disabled, or you do not have permission to access the file.\n\n");
    }

    FILE *kcpasswd;
    kcpasswd = fopen(argv[1], "r");
    int a = fgetc(kcpasswd);
    printf("%d\n",a);
}
