package Lap11.Lap11_2;

import Lap07.Lap07_1.*;

public class Account {
    protected double balance;
    protected String name;
    public Account(double balance, String name){
        setBalance(balance);
        setName(name);
    }
    public void deposit(double a){
        if(a > 0){
            setBalance(getBalance()+a);
            System.out.println(a+" baht is deposited to "+this.name+".");
        }
        else{
            System.out.println("Input number must be a positive integer.");
        }
    }
    public void withdraw(double a) throws WithdrawException{
        if(a > 0 && getBalance()-a > 0){
            setBalance(getBalance()-a);
            System.out.println(a+" baht is withdrawn from "+this.name+".");
        }
        else if(a < 0){
            System.out.println("Input number must be a positive integer.");
        }
        else{
            throw new WithdrawException("Account "+this.name+" has not enough money.");
        }
    }
    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return this.name;
    }
    public void setBalance(double balance){
        this.balance = balance;
    }
    public double getBalance(){
        return this.balance;
    }
    public void showAccount(){
        System.out.println(this.name+" account has "+this.balance+" baht.");
    }

    void setCredit(double d) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
}
