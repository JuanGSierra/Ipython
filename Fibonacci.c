#include <stdio.h>

int main()
{
    long fib = 0;

    long long a = 0;
    long long b = 1;
    long long c = 0;

    while(c>=0)
    {
        a=0;
        b=1;
        c=0;
        printf("fib %d \n", fib);
        for(int i=0; i<fib-1; i++)
        {
            c = a+b;
            a = b;
            b = c;
            printf("c %lli \n",c);
        }
        fib++;
    }
    return 0;
}
//short overflows Fibonacci en 24
//int y long overflows Fibonacci en 47
//long long overflows Fibonacci en 93
