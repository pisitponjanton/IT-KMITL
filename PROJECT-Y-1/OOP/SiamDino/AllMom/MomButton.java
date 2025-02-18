package AllMom;

import java.awt.*;
import javax.swing.*;

public abstract class MomButton extends JButton {
    private Image backgroundImage;
    private String namePath;

    public MomButton(String namePath, int width, int height) {
        this.namePath = namePath;
        this.drawBackgroundImage();
        setSize(width, height);
        setOpaque(false);
        setContentAreaFilled(false);
        setCursor(new Cursor(Cursor.HAND_CURSOR));
        setBorderPainted(false);
        setFocusPainted(false);
    }

    private void drawBackgroundImage() {
        backgroundImage = new ImageIcon("img/buttonImage/" + this.namePath + ".jpg").getImage();
    }

    @Override
    protected void paintComponent(Graphics g) {
        if (backgroundImage != null) {
            g.drawImage(backgroundImage, 0, 0, getWidth(), getHeight(), this);
        }
        super.paintComponent(g);
    }
}
