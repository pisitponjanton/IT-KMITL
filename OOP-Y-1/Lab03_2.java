import java.util.*;
public class Lab03_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int even = 0;
        int odd = 0;
        while(true){
            int num = sc.nextInt();
            if(num ==-1 )
                break;
            if(num%2 == 0){
                even+=1;
            }else{
                odd+=1;
            }
        }
        System.out.println("Odd number = "+odd+" and Even number = "+even);
    }
}
