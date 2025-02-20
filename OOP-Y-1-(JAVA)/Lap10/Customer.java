
package Lap10;

//public class Customer {
//    private String firstName;
//    private String lastName;
//    private Account acct[];
//    private int numOfAccount;
//    public Customer(){
//        this("","");
//    }
//    public Customer(String firstName ,String lastName){
//        this.firstName = firstName;
//        this.lastName = lastName;
//        acct = new Account[5];
//    }
//    public Account getAccount(int index){
//        return this.acct[index];
//    }
//    public void addAccount(Account acct){
//        this.acct[this.numOfAccount] = acct;
//        this.numOfAccount += 1;
//    }
//    public int getNumOfAccount(){
//        return this.numOfAccount;
//    }
//        @Override
//    public String toString(){
//        return this.firstName+" "+this.lastName+" has "+this.numOfAccount+" accounts.";
//    }
//}
import java.util.*;
public class Customer {
    private String firstName;
    private String lastName;
    private ArrayList<Account> acct;
    private int numOfAccount;
    public Customer(){
        this("","");
    }
    public Customer(String firstName ,String lastName){
        this.firstName = firstName;
        this.lastName = lastName;
        acct = new  ArrayList();
    }
    public Account getAccount(int index){
        return this.acct.get(index);
    }
    public void addAccount(Account acct){
        this.acct.add(acct);
        this.numOfAccount += 1;
    }
    public int getNumOfAccount(){
        return this.acct.size();
    }
        @Override
    public String toString(){
        return this.firstName+" "+this.lastName+" has "+this.getNumOfAccount()+" accounts.";
    }
}
