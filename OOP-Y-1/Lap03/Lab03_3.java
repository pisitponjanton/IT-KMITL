import java.util.*;

public class Lab03_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Please insert a number : ");
        int num = sc.nextInt();
        for(int i = 1;i<=num;i++){
            if(i%5 == 0)
                System.out.print("/");
            else
                System.out.print("|");
        }
        System.out.println();
    }
}
