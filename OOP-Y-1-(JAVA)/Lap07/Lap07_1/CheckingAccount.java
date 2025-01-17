package Lap07.Lap07_1;


public class CheckingAccount extends Account {

    private double credit;

    public CheckingAccount() {
        super(0, "");
        this.credit = 0;
    }

    public CheckingAccount(double balance, String name, double credit) {
        super(balance, name);
        this.credit = credit;
    }

    public void setCredit(double credit) {
        if (credit >= 0) {
            this.credit = credit;
        } else {
            System.out.println("Input number must be a positive integer.");
        }
    }

    public double getCredit() {
        return this.credit;
    }

    @Override
    public void withdraw(double a) {
        if (a <= 0) {
            System.out.println("Input number must be a positive integer.");
            return;
        }

        if (balance - a >= 0) {
            this.setBalance(getBalance() - a);
            System.out.println(a + " baht is withdrawn from " + name + " and your credit balance is " + credit + ".");
        } else if ((balance - a < 0) && (balance - a + credit >= 0)) {
            setCredit(credit + (balance - a));
            this.setBalance(0);
            System.out.println(a + " baht is withdrawn from " + name + " and your credit balance is " + credit + ".");
        } else if ((balance - a < 0) && (balance - a + credit < 0)) {
            System.out.println("Not enough money!");
        }
    }

    public void withdraw(String a) {
        double doubleValue = Double.parseDouble(a);
        this.withdraw(doubleValue);
    }

    @Override
    public String toString() {
        return "The " + name + " account has " + balance + " baht and " + credit + " credits.";
    }
}