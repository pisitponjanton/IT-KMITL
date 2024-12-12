import java.util.*; 
public class Lab02_1 { 
  public static void main(String[] args) { 
      Scanner sc = new Scanner(System.in);
      double money = sc.nextDouble();
      if(money>50000){
        money*=0.1;
      }else{
        money*=0.05;
      }
      System.out.println(money);
  }
}