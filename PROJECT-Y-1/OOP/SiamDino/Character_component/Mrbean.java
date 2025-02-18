package Character_component;

import AllMom.MomCharacter;
import java.awt.*;
import javax.swing.JLabel;

public class Mrbean extends MomCharacter {
    public Mrbean() {
        super(200, 200, 200, 540, "mrbean");
        super.setSpeed(2);
        super.startAnimation();
        super.startMove();
        setmoveXY(4);

        setLayout(null);
        JLabel l = new JLabel("LV.1");
        l.setFont(new Font("Arial", Font.BOLD, 12));
        l.setBounds(85, 10, 100, 50);
        add(l);
    }
}
