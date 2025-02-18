package Link_Panel;

import AllMom.MomBackground;
import Background_component.NameGame;
import Character_component.Mrbean;
import Character_component.Snowkuy;
import java.awt.*;
import javax.swing.*;

public class MenuPanel extends MomBackground {
    private JButton startButton;
    private Mrbean mrbean;
    private Snowkuy snowkuy;
    private NameGame namegame;

    public MenuPanel(CardLayout cardLayout, JPanel mainPanel) {
        super("bg");

        setLayout(null);

        startButton = new JButton("Start");
        styleButton(startButton);
        startButton.addActionListener(new CardSwitcher(cardLayout, mainPanel, "GamePanel"));
        add(startButton);

        namegame = new NameGame();
        add(namegame);

        snowkuy = new Snowkuy();
        mrbean = new Mrbean();

        add(snowkuy);
        add(mrbean);
    }

    private void styleButton(JButton button) {
        button.setFont(new Font("Arial", Font.BOLD, 50));
        button.setForeground(Color.WHITE);
        button.setBorderPainted(false);
        button.setFocusPainted(false);
        button.setBounds(600,400, 200, 50);
        button.setCursor(new Cursor(Cursor.HAND_CURSOR));
    }
}
