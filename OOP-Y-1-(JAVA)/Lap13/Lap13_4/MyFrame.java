package Lap13.Lap13_4;

import javax.swing.*;
import java.awt.event.*;

public class MyFrame extends MouseAdapter {
    private MyClock clock;

    public MyFrame() {
        JFrame jf = new JFrame("Time");
        clock = new MyClock();
        clock.addMouseListener(this);
        Thread t = new Thread(clock);
        t.start();
        jf.add(clock);
        jf.setSize(200, 100);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setVisible(true);
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        if (!clock.getRunning()) {
            clock.stopping();
        } else {
            clock.running();
        }
    }

    public static void main(String[] args) {
        new MyFrame();
    }
}
