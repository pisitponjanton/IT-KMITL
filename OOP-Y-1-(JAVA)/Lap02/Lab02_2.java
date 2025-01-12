import java.util.*;
public class Lab02_2 { 
  public static void main(String[] args) { 
    Scanner sc = new Scanner(System.in);
    System.out.print("Input your money: ");
    double money = sc.nextDouble();
    sc.nextLine();
    System.out.print("Input your account type(Please type A B C or X in uppercase) : ");
    String c = sc.nextLine();
    if(c.equals("A") || c.equals("c")){
        money*=1.015;
    }else if(c.equals("B")){
        money*=1.02;
    }else if(c.equals("X")){
        money*=1.05;
    }
    System.out.println("Your total money in one year = "+money);
  }
}