package Lap08.Lap08_2;
import javax.swing.*;
import java.awt.*;
public class CalculatorTwoGUI {
    public JFrame jf;
    public JPanel jp;
    public JTextField jt;
    public JButton[] buttons;
    public String[] strBT = 
    {
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","x",
    "0","c","=","/",
    };
    public CalculatorTwoGUI(){
        jf = new JFrame();
        jp = new JPanel();
        jt = new JTextField();
        
        jp.setLayout(new GridLayout(4,4));
        buttons = new JButton[16];
        for(int i = 0 ; i < strBT.length; i++){
            buttons[i] = new JButton(strBT[i]);
            jp.add(buttons[i]);
        }
        
        jf.setTitle("My Calculator");
        jf.setLayout(new BorderLayout());
        jf.add(jt,BorderLayout.NORTH);
        jf.add(jp);
        jf.setSize(500,500);
        jf.setDefaultCloseOperation(3);
        jf.setVisible(true);
    }
}
