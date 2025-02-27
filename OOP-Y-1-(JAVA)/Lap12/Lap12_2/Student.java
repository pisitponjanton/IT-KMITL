package Lap12.Lap12_2;
import java.io.*;
public class Student implements Serializable{
    private String name;
    private int ID;
    private int money;
    
    public Student(){
        this("",0,0);
    }
    
    public Student(String name,int ID,int money){
        this.name = name;
        this.ID = ID;
        this.money = money;
    }
    
    public void setName(String name){
        this.name = name;
    }
    
    public String getName(){
        return this.name;
    }
    
    public void setID(int ID){
        this.ID = ID;
    }
    
    public int getID(){
        return this.ID;
    }
    
    public void setMoney(int money){
        this.money = money;
    }
    
    public int getMoney(){
        return this.money;
    }
    
}
