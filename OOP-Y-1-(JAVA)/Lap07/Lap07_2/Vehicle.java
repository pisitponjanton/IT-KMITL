package Lap07.Lap07_2;
public abstract class Vehicle implements Dieselable{
    protected double fuel;
    public Vehicle(){
        this(0.0);
    }
    public Vehicle(double fuel){
        setFuel(fuel);
    }
    public void addFuel(double fuel){
        if(fuel > 0 ){
            setFuel(getFuel()+fuel);
        }
        else{
            System.out.println("Fuel is empty.");
        }
    }
    public void setFuel(double fuel){
        this.fuel = fuel;
    }
    public double getFuel(){
       return this.fuel;
    }
    public abstract void honk();
}
