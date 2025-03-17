package LapP_Few.Lap2;

import java.io.*;
import java.util.*;

public class Item implements Serializable {
    private int Id;
    private String name;
    private double price;
    private Date created_on;
    
    public Item(){
        this(0,"",0.0,new Date());
    }
    public Item(int Id,String name,double price,Date created_on){
        this.Id = Id;
        this.name = name;
        this.price = price;
        this.created_on = created_on;
    }
    
    public int getId(){
        return this.Id;
    }
    
    public void setId(int Id){
        this.Id = Id;
    }
    
    public String getName(){
        return this.name;
    }
    
    public void setName(String name){
        this.name = name;
    }
    
    public double getPrice(){
        return this.price;
    }
    
    public void setPrice(double price){
        this.price = price;
    }
    
    public Date getCreated_On(){
        return this.created_on;
    }
    
    public void setCreated_On(Date created_on){
        this.created_on = created_on;
    }
}
