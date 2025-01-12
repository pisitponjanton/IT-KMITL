import java.util.*;
public class Lab02_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Please insert your name : ");
        String name = sc.nextLine();
        
        System.out.print("Please insert your age : ");
        int age = sc.nextInt();
        
        System.out.print("Please insert number of working days : ");
        int working = sc.nextInt();
        
        System.out.print("Please insert number of absent days : ");
        int absent = sc.nextInt();
        
        System.out.print("Please insert your body weight : ");
        double weight = sc.nextDouble();
        
        System.out.println("Hi, "+name);
        
        int salary = 0;
        double bonus = 0;
        
        if((age>=21) && (age<=30)){
            salary = (working*300)-(absent*50);
        }else if((age>=31) && (age<=40)){
            salary = (working*500)-(absent*50);
        }else if((age>=41) && (age<=50)){
            salary = (working*1000)-(absent*25);
        }else if((age>=51) && (age<=60)){
            salary = (working*3000);
        }
        
        if((weight>=10)&&(weight<=60)){
            bonus = 5000;
        }else if((weight>=61)&&(weight<=90)){
            bonus = 5000 - ((weight-60)*10);
        }
        
        System.out.println("Your salary is "+salary+" Baht");
        System.out.println("Your salary and bonus is "+(salary+bonus)+" Baht");
    }
}
