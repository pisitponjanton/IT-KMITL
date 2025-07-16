# include <stdio.h>

int main(){
    float number_f_1 = 123.930035;
    float number_f_2 = 124.93012345623;

    double number_d_1 = 456.123001;
    double number_d_2 = 457.123023456781234121212;

    float number_f_3 = 34.0000005;
    double number_d_3 = 34.0000005;

    printf("Float1: %f\n",number_f_1);
    printf("Float2: %f\n",number_f_2);

    printf("Double1: %lf\n",number_d_1);
    printf("Double2: %lf\n",number_d_2);

    float result_float = number_f_3 + number_f_3;
    printf("Result float: %f\n",result_float);

    double result_double = number_d_3 + number_d_3;
    printf("Result double: %lf\n",result_double);
    return 0;    
}