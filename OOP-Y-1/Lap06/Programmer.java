package Lab06;
public class Programmer extends Employee{
    private int happiness;
    public void coding(String str){
        if(super.getEnergy()>=30){
            System.out.println("Your code is "+str);
        }else{
            System.out.println("Error Error Error");
        }
        super.setEnergy(super.getEnergy()-30);
        this.happiness-=30;
    }
    public void coding(char str){
        if(super.getEnergy()>=30){
            System.out.println("Your code is "+str);
        }else{
            System.out.println("Error Error Error");
        }
        super.setEnergy(super.getEnergy()-30);
        this.happiness-=30;
    }
    public int getHappiness(){
        return this.happiness;
    }
    public void setHappiness(int happiness){
        this.happiness = happiness; 
    }
}
