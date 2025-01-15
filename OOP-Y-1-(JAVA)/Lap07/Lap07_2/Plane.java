package Lap07.Lap07_2;
public class Plane extends Vehicle{
    private String airline,boeing;
    private static final int MAX_FLYER = 2;
    public Plane(){
        this(0.0,"","");
    }
    public Plane(double fuel,String airline,String  boeing){
        setAirline(airline);
        setBoeing(boeing);
        super.setFuel(fuel);
    }
    public void setAirline(String airline){
        this.airline = airline;
    }
    public String getAirline(){
        return this.airline;
    }
    public void setBoeing(String boeing){
        this.boeing = boeing;
    }
    public String getBoeing(){
        return this.boeing;
    }
    @Override
    public void startEngine(){
        if(super.getFuel() >= 20){
            super.setFuel(super.getFuel()-20);
            System.out.println("Plane’s Engine starts");
        }
        else if(super.getFuel() < 20){
            System.out.println("Fuel is not enough.");
        }
    }
    @Override
    public void stopEngine(){
        System.out.println("Plane’s Engine stops");
    }
    @Override
    public void honk(){
        System.out.println("Weeeeeee");
    }
    public void fly(){
        if(super.getFuel() >= 20){
            super.setFuel(super.getFuel()-20);
            System.out.println("Plane Fly");
        }
        else if(super.getFuel() < 20){
            System.out.println("Fuel is nearly empty.");
        }
    }
    public void takeOff(){
        if(super.getFuel() >= 10){
            super.setFuel(super.getFuel()-10);
            System.out.println("Plane Already to Take Off");
        }
        else if(super.getFuel() < 10){
            System.out.println("Fuel is nearly empty.");
        }
    }
    public void landing(){
        if(super.getFuel() >= 10){
            super.setFuel(super.getFuel()-10);
            System.out.println("Plane Already to Landing");
        }
        else if(super.getFuel() < 10){
            System.out.println("Fuel is nearly empty.");
        }
    }
}
