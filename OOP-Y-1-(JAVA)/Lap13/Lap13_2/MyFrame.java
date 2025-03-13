package Lap13.Lap13_2;

import javax.swing.*;

public class MyFrame {
    public static void main(String[] args) {
        JFrame jf = new JFrame("Time");
        MyClock clock = new MyClock();
        Thread t = new Thread(clock);
        t.start();
        jf.add(clock);
        jf.setSize(200,100);
        jf.setDefaultCloseOperation(3);
        jf.setVisible(true);
    }
}
