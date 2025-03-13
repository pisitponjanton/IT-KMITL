package Lap13.Lap13_1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class Poring extends MouseAdapter{
    private JFrame jf;
    private JLabel jlb;
    private ImageIcon icon;

    public Poring(int n) {
        try {
            icon = new ImageIcon(getClass().getResource("poring.png"));
            Image img = icon.getImage().getScaledInstance(200, 200, Image.SCALE_SMOOTH);
            icon = new ImageIcon(img);
        } catch (Exception e) {
            System.out.println("Error loading image: " + e.getMessage());
        }

        jf = new JFrame("Poring");
        new Thread(()->{
            try{
                while(true){
                    Thread.sleep(50);
                    Random r = new Random();
                    if(r.nextBoolean()){
                        jf.setLocation(jf.getX()+5,jf.getY()+5);
                    }
                    else{
                        jf.setLocation(jf.getX()-5,jf.getY()-5);
                    }
                }
            }catch(InterruptedException e){
                
            }
        }).start();
        jlb = new JLabel(String.valueOf(n), icon, JLabel.CENTER);
        jlb.addMouseListener(this);
        jf.add(jlb);
        jf.pack();
        jf.setDefaultCloseOperation(0);
        jf.setResizable(false);
        jf.setLocationRelativeTo(null);
        jf.setVisible(true);
    }
    @Override
    public void mouseClicked(MouseEvent e){
        jf.dispose();
    }


}
