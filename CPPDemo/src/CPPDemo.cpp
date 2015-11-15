#include<stdio.h>
#define ap(m,n) m ## n
#define s(x) x

int main(){
    int m=14,n=4;
    do{
        printf("%d",ap(m,n));
    }while(s(90),4);

    return 0;
}

