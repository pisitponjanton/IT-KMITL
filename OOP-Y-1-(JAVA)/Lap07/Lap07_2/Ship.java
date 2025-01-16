package Lap07.Lap07_2;
public class Ship extends Vehicle implements Floatable{
    public Ship(){
        this(0.0);
    }
    public Ship(double fuel){
        super(fuel);
    }
    @Override
    public void fl0at(){
        if(super.getFuel() >= 50){
            super.setFuel(super.getFuel()-50);
            System.out.println("Ship moves");
        }
        else if(super.getFuel() < 50){
            System.out.println("Fuel is not enough.");
        }
    }
    @Override
    public void startEngine(){
        if(super.getFuel() >= 10){
            super.setFuel(super.getFuel()-10);
            System.out.println("Engine starts");
        }
        else if(super.getFuel() < 10){
            System.out.println("Fuel is not enough.");
        }
    }
    @Override
    public void stopEngine(){
        System.out.println("Engine stops");
    }
    @Override
    public void honk(){
        System.out.println("Shhhhh");
    }
    public void move(){
        fl0at();
    }
    public void move(int distance){
        for(int i = 0;i<distance;i++){
            if(super.getFuel()<50){
                System.out.println("Fuel is not enough.");
                break;
            }
            fl0at();
        }
    }
}
