#include <stdio.h>
#include <ctype.h>

double celciusToFahrenheit(double c);
void printFahrenheit(double f);
double fahrenheitToCelcius(double f);
void printCelcius(double c);

int main()
{
    double n;
    char o;
    scanf("%lf %c", &n, &o);
    if(tolower(o) == 'c'){
        printFahrenheit(celciusToFahrenheit(n));
    }
    else{
        printCelcius(fahrenheitToCelcius(n));
    }
    return 0;
}

double celciusToFahrenheit(double c)
{
    return 32 + c * (180.0 / 100.0);
}

void printFahrenheit(double f)
{
    printf("%.2lf f", f);
}

double fahrenheitToCelcius(double f)
{
    return (f - 32) * 100.0/180.0;
}

void printCelcius(double c)
{
    printf("%.2lf c", c);
}