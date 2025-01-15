package Lap07.Lap07_1;

public class Customer {
    private String firstname;
    private String lastname;
    private CheckingAccount acct;
    public Customer(){
        setFirstName("");
        setLastName("");
        setAcct(null);
    }
    public Customer(String firstname,String lastname){
        setFirstName(firstname);
        setLastName(lastname);
    }
    public Customer(String firstname,String lastname, CheckingAccount acct){
        setFirstName(firstname);
        setLastName(lastname);
        setAcct(acct);
    }
    public void setFirstName(String firstname){
        this.firstname = firstname;
    }
    public String getFirstName(){
        return this.firstname;
    }
    public void setLastName(String lastname){
        this.lastname = lastname;
    }
    public String getLastName(){
        return this.lastname;
    }
    public void setAcct(CheckingAccount acct){
        this.acct = acct;
    }
    public CheckingAccount getAcct(){
        return this.acct;
    }
    public String toString(){
        if(getAcct() == null){
            return this.firstname+" "+this.lastname+" doesn’t have account.";
        }
        else{
            return "The "+this.firstname+" account has "+acct.getBalance()+" baht and "+acct.getCredit()+" credits.";
        }
    }
    public boolean equals(Customer c){
        return c.getFirstName().equals(getFirstName()) && c.getLastName().equals(getLastName());
    } 
}
