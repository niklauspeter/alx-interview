#include <stdio.h>
int fibo(int i){
    if (i == 0){
        return i;
    }
    if (i == 1){
        return i;
    }
    
return fibo(i - 2 ) + fibo(i - 1);
}

int main(void){
    int sum;
    sum = fibo(6);
    printf(" ");
    printf("%d\n", sum);
}