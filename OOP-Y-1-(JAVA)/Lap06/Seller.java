package Lab06;
public class Seller extends Employee{
    public Food sell(Employee e){
        Food food = new Food();
        Wallet wallet = e.getWallet();
        Wallet seller = super.getWallet();
        if(food.getPrice() <= wallet.getBalance()){
            wallet.setBalance(wallet.getBalance()-food.getPrice());
            seller.setBalance(seller.getBalance()+food.getPrice());
            e.setWallet(wallet);
            return food;
        }else{
            System.out.println("Your money is not enough.");
            return null;
        }
    }
}
