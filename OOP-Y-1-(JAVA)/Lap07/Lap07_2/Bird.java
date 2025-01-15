package Lap07.Lap07_2;
public abstract class Bird implements Flyable{
    private double wingSize,weight,height;
    public Bird(){
        this(0.0,0.0,0.0);
    }
    public Bird(double wingSize,double weight,double height){
        setWingSize(wingSize);
        setWeight(weight);
        setHeight(height);
    }
    public void eat(double food){
        if(food > 0){
            setWeight(getWeight()+food);
        }
        else{
            System.out.println("Input cannot be negative number.");
        }
    }
    public void setWingSize(double wingSize){
        this.wingSize = wingSize;
    }
    public double getWingSize(){
        return this.wingSize;
    }
    public void setWeight(double weight){
        this.weight = weight;
    }
    public double getWeight(){
        return this.weight;
    }
    public void setHeight(double height){
        this.height = height;
    }
    public double getHeight(){
        return this.height;
    }
}
