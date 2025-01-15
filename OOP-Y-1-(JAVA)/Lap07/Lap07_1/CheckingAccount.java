package Lap07.Lap07_1;

public class CheckingAccount extends Account{
    private double credit;
    public CheckingAccount(){
        super(0.0,"");
        this.credit = 0.0;
    }
    public CheckingAccount(double balance,String name,double credit){
        super(balance,name);
        this.credit = credit;
    }
    public void setCredit(double credit){
        if(credit > 0){
            this.credit = credit;   
        }
        else{
            System.out.println("Input number must be a positive integer.");
        }
    }
    public double getCredit(){
        return this.credit;
    }
    @Override
    public void withdraw(double a){
        if(a > 0 && getBalance()-a > 0){
            setBalance(getBalance()-a);
            System.out.println(a+" baht is withdrawn from "+super.getName()+" and your credit balance is "+this.credit+".");
        }
        else if(a > 0 && (getCredit()+getBalance())-a >= 0){
            setBalance(0);
            setCredit(getCredit() - a);
            System.out.println(a+" baht is withdrawn from "+super.getName()+" and your credit balance is "+this.credit+".");
        }
        else{
            System.out.println("Not enough money!");
        }
    }
    public void withdraw(String a){
        this.withdraw(Double.parseDouble(a));
    }
    public String toString(){
        return "The "+super.getName()+" account has "+super.getBalance()+" baht and "+getCredit()+" credits.";
    }
}
