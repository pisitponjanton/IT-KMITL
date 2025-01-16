package Lap07.Lap07_1;

public class Customer {
    private String firstName;
    private String lastName;
    private CheckingAccount acct;
    public Customer(){
        setFirstName("");
        setLastName("");
        setAcct(null);
    }
    public Customer(String firstName,String lastName){
        setFirstName(firstName);
        setLastName(lastName);
    }
    public Customer(String firstName,String lastName, CheckingAccount acct){
        setFirstName(firstName);
        setLastName(lastName);
        setAcct(acct);
    }
    public void setFirstName(String firstName){
        this.firstName = firstName;
    }
    public String getFirstName(){
        return this.firstName;
    }
    public void setLastName(String lastName){
        this.lastName = lastName;
    }
    public String getLastName(){
        return this.lastName;
    }
    public void setAcct(CheckingAccount acct){
        this.acct = acct;
    }
    public CheckingAccount getAcct(){
        return this.acct;
    }
    @Override
    public String toString(){
        if(getAcct() == null){
            return this.firstName+" "+this.lastName+" doesn’t have account.";
        }
        else{
            return "The "+this.firstName+" account has "+acct.getBalance()+" baht and "+acct.getCredit()+" credits.";
        }
    }
    public boolean equals(Customer c){
        return c.getFirstName().equals(getFirstName()) && c.getLastName().equals(getLastName());
    } 
}
