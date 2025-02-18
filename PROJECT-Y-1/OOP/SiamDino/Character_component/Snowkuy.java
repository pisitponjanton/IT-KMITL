package Character_component;

import AllMom.MomCharacter;
import java.awt.*;
import javax.swing.JLabel;

public class Snowkuy extends MomCharacter {
    public Snowkuy() {
        super(200, 200, 500, 540, "snowkuy");
        super.startAnimation();
        super.startMove();
        super.setSpeed(2);

        setLayout(null);
        JLabel l = new JLabel("LV.2");
        l.setFont(new Font("Arial", Font.BOLD, 12));
        l.setBounds(85, 10, 100, 50);
        add(l);
    }
}
