package Link_Panel;
import java.awt.*;
import javax.swing.*;

public class GamePanel extends JPanel {
    private JButton backButton;
    private Image backgroundImage;

    public GamePanel(CardLayout cardLayout, JPanel mainPanel) {
        backgroundImage = new ImageIcon("test.jpeg").getImage();
        backButton = new JButton("Back Game");
        backButton.addActionListener(new CardSwitcher(cardLayout, mainPanel, "MenuPanel"));
        add(backButton);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(backgroundImage, 0, 0, getWidth(), getHeight(), this);
    }
}
