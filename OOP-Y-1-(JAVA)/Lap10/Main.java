/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Lap10;

/**
 *
 * @author mba135816
 */
public class Main {
    public static void main(String[] args) {
 Customer cust = new Customer("Somsri", "Boonjing");
 Account acct1 = new Account(5000, "Somsri01");
 Account acct2 = new Account(3000, "Somsri02");
 cust.addAccount(acct1);
 cust.addAccount(acct2);
 // ทดลองฝากเงิน ถอนเงินในบัญชีต่างๆ
 cust.getAccount(0).withdraw(3000);
 cust.getAccount(1).deposit(3000);
 // แสดงข้อมูลของลูกค้า เช่น Somsri Boonjing has 2 accounts.
 System.out.println(cust);
 // ทดลองสร้างบัญชีและเพิEมบัญชีนัFนๆ ให้กับลูกค้า มากกว่า 5 บัญชี
 for (int i = 0; i < cust.getNumOfAccount(); i++) {
 cust.getAccount(i).showAccount();
 }
}
}
