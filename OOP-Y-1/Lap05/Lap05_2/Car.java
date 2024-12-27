package Lap05.Lap05_2;
public class Car extends Vehicle{
    private String typeEngine;
    public void setTypeEngine(String t){
        this.typeEngine = t;
    }
    public String getTypeEngine(){
        return this.typeEngine;
    }
    public void setCarInfo(int s,String t,String y){
        super.setFuel(s);
        super.setTopSpeed(t);
        this.typeEngine = y;
    }
    public void move(){
        if(getFuel()>=50){
            super.setFuel(super.getFuel() - 50);
            System.out.println("Move.");
        }
        else System.out.println("Please add fuel.");
    }
    public void showCarInfo(){
        System.out.println("Car engine is "+this.typeEngine+".");
        System.out.println("Fuel is "+super.getFuel()+" litre and Top Speed is "+super.getTopSpeed()+" m/s.");
    }
}
