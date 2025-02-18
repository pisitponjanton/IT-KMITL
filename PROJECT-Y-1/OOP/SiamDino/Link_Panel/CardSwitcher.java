package Link_Panel;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class CardSwitcher implements ActionListener {
    private CardLayout cardLayout;
    private JPanel panel;
    private String name;

    public CardSwitcher(CardLayout cardLayout, JPanel panel,String  name) {
        this.cardLayout = cardLayout;
        this.panel = panel;
        this.name = name;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        cardLayout.show(panel,name);
    }
}
