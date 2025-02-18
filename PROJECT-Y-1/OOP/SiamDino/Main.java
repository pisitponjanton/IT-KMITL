import Link_Panel.GamePanel;
import Link_Panel.MenuPanel;
import java.awt.*;
import javax.swing.*;

public class Main {
    private JFrame frame;
    private JPanel mainPanel;
    private CardLayout cardLayout;

    public Main() {
        frame = new JFrame("Game Launcher");
        cardLayout = new CardLayout();
        mainPanel = new JPanel(cardLayout);

        MenuPanel startMenu = new MenuPanel(cardLayout, mainPanel);
        GamePanel gamePanel = new GamePanel(cardLayout, mainPanel);
        
        mainPanel.add(startMenu, "MenuPanel");
        mainPanel.add(gamePanel, "GamePanel");

        frame.add(mainPanel);
        frame.setResizable(false);
        frame.setSize(1350, 800);
        frame.setDefaultCloseOperation(3);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        new Main();
    }
}
