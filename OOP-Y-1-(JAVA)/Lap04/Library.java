public class Library {
    public String libraryName;
    public Book book1,book2,book3;
    public void addBook(Book book, int slot){
        if(slot == 1)book1 = book;
        else if(slot == 2)book2 = book;
        else if(slot == 3)book3 = book;
    }
    public void removeBook(int slot){
        if(slot == 1)book1 = null;
        else if(slot == 2)book2 = null;
        else if(slot == 3)book3 = null;
    }
    public void printLibraryDetails() {
        Book book = null;
        System.out.println("Library: "+libraryName+"\n");
        for(int i = 0; i<3 ;i++){
            if(i==0) book = book1;
            else if(i==1) book = book2;
            else if(i==2) book = book3;
            if(book!=null){
                System.out.println("Title: "+ book.title);
                System.out.println("Author: "+book.author);
                System.out.println("Publisher: "+ book.publisher);
                System.out.println("Year Published: "+ book.yearPublished);
                System.out.println("Price: $"+ book.price);
                System.out.println("Available: "+(book.isAvailable ? "Yes\n" : "No\n"));
            }else
                System.out.println("No book in this slot.\n");
        }
    }
    public void checkBookAvailability(int slot){
        Book book = null;
        if(slot == 1)book = book1;
        else if(slot == 2)book = book2;
        else if(slot == 3)book = book3;
        if(book == null)
            System.out.println("Book in slot "+slot+" is not available.");
        else
            System.out.println(book.title + " is available.");
    }
    public void updateBookPrice(int slot, double newPrice){
        Book book = null;
        if(slot == 1)book = book1;
        else if(slot == 2)book = book2;
        else if(slot == 3)book = book3;
        if(book == null)
            System.out.println("No book in this slot.");
        else{
            System.out.println("Updated price of "+book.title+" to $"+newPrice+".");
            book.price = newPrice;
        }
    }
    public void printBookDetails(Book book){
        if(book == null)
            System.out.println("No book in this slot.");
        else
            System.out.println("Title: "+ book.title);
            System.out.println("Author: "+book.author);
            System.out.println("Publisher: "+ book.publisher);
            System.out.println("Year Published: "+ book.yearPublished);
            System.out.println("Price: $"+ book.price);
            System.out.println("Available: "+(book.isAvailable ? "Yes" : "No"));
    }
}