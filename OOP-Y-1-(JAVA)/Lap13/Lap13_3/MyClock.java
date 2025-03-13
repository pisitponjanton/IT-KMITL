/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Lap13.Lap13_3;

import java.awt.*;
import javax.swing.*;

public class MyClock extends JLabel implements Runnable {
    private int sec;
    private int min,min1;
    private int hour;
    private int timer;
    @Override
    public void run(){
        try{
            while(true){
                timer += 1;
                sec = timer%60;
                min1 = timer/60;
                min = min1%60; 
                hour = min1/60;
                String time =  (hour<10 ? "0"+hour : hour)+":"+(min<10 ? "0"+min : min)+":"+(sec<10 ? "0"+sec : sec);
                setText(time);
                setHorizontalAlignment(JLabel.CENTER);
                setFont(new Font("Arial", Font.BOLD, 24));
                Thread.sleep(1000);
            }
        }catch(InterruptedException e){
        }
    }
}
