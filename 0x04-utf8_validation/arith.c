#include <stdio.h>
int sum_inc(int i){
    if (i == 1){
        return i;
    }
return i + sum_inc(i - 1);
}

int main(void){
    int sum;
    sum = sum_inc(5);
    printf("run\n");
    printf("%d\n", sum);
}