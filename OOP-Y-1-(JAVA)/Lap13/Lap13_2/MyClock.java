/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Lap13.Lap13_2;

import java.awt.*;
import java.util.*;
import javax.swing.*;

public class MyClock extends JLabel implements Runnable {
    @Override
    public void run(){
        try{
            while(true){
                Calendar d = Calendar.getInstance();
                int sec = d.get(Calendar.SECOND);
                int min = d.get(Calendar.MINUTE);
                int hour = d.get(Calendar.HOUR_OF_DAY);
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
