/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Lab06;

/**
 *
 * @author mba135816
 */
public class Main {
    public static void main(String[] args) {
 Wallet w1 = new Wallet();
 Wallet w2 = new Wallet();
 w1.setBalance(200);
 w2.setBalance(100);

 Programmer p1 = new Programmer();
 p1.setName("Boy");
 p1.setEnergy(100);
 p1.setWallet(w1);
 p1.setHappiness(100);

 SeniorProgrammer sp1 = new SeniorProgrammer();
 sp1.setName("Ploy");
 sp1.setEnergy(100);
 sp1.setWallet(w2);
 sp1.setHappiness(100);

 System.out.println(sp1 + "\nHappiness : " +sp1.getHappiness());
 sp1.coding('A');
 sp1.coding("Bugggggg");
 sp1.coding("Bugggggg",2);
 System.out.println(sp1 + "\nHappiness : " +sp1.getHappiness());
 System.out.println("---------------------------------");
 System.out.println(p1 + "\nHappiness : " +p1.getHappiness());
 p1.coding('B');
 p1.coding("Deathhhhhhhh");
 System.out.println(p1 + "\nHappiness : " +p1.getHappiness());
 }
}
