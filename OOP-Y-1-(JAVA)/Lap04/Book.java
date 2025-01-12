public class Book {
    public String title,author,publisher;
    public int yearPublished;
    public double price;
    public boolean isAvailable;
    public void printDetails(){
        System.out.println("Title: "+title);
        System.out.println("Author: "+author);
        System.out.println("Publisher: "+publisher);
        System.out.println("Year Published: "+yearPublished);
        System.out.println("Price: $"+price);
        System.out.println("Available: "+(isAvailable ? "Yes" : "No"));
    }
    public void updatePrice(double newPrice){
        price = newPrice;
    }
    public void markAsUnavailable(){
        isAvailable = false;
    }
    public void markAsAvailable(){
        isAvailable = true;
    }
    public boolean isPublishedAfter(int year){
        if(year < yearPublished)
            return true;
        else
            return false;
    }
}
