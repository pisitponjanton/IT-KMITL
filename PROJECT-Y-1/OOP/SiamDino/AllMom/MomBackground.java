package AllMom;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public abstract class MomBackground extends JPanel {
    private Image backgroundImage;
    private String namePath;

    public MomBackground(String namePath) {
        this.namePath = namePath;
        this.drawBackgroundImage();
        setOpaque(false);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(backgroundImage, 0, 0, getWidth(), getHeight(), this);
    }

    private void drawBackgroundImage() {
        backgroundImage = new ImageIcon("img/backgroundImage/" + this.namePath + ".jpg").getImage();
    }

    protected void animationY() {
        this.animationY(0);
    }

    protected void animationY(int i) {
        Timer timer = new Timer(10, new ActionListener() {
            private float y = 0;
            private int movingDown = 0;
            private Point location = getLocation();

            @Override
            public void actionPerformed(ActionEvent e) {
                switch (movingDown) {
                    case 0 -> {
                        if (y < location.y + 10) {
                            y += 1;
                        } else {
                            movingDown = 1;
                        }
                    }
                    case 1 -> {
                        if (y > location.y - 30) {
                            y -= 0.5;
                        } else {
                            movingDown = 2;
                        }
                    }
                    default -> {
                        if (y < location.y) {
                            y += 0.25;
                        } else {
                            if(i == 0){
                                ((Timer) e.getSource()).stop();
                            }else{
                                movingDown = 0;
                            }
                        }
                    }
                }
                setLocation(500, (int) y);
            }
        });

        timer.start();
    }
}
