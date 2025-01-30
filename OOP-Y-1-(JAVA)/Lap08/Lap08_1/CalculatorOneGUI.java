package Lap08.Lap08_1;
import javax.swing.*;
import java.awt.*;
public class CalculatorOneGUI{
    public JFrame jF;
    public JPanel jP,jpin,jpino;
    public JButton jB1,jB2,jB3,jB4;
    public JTextField jTF1,jTF2,jTF3;
    public CalculatorOneGUI(){
        jF = new JFrame();
        jP = new JPanel();
        jpin  = new JPanel();
        jpino  = new JPanel();
        jB1 = new JButton("บวก");
        jB2 = new JButton("ลบ");
        jB3 = new JButton("คูณ");
        jB4 = new JButton("หาร");
        jTF1 = new JTextField();
        jTF2 = new JTextField();
        jTF3 = new JTextField();
        
        jF.setTitle("เครื่องคิดเลข");
        jF.setSize(500,200);
        jF.setDefaultCloseOperation(3);
        
        jpin.setLayout(new FlowLayout());
        jpin.add(jB1);
        jpin.add(jB2);
        jpin.add(jB3);
        jpin.add(jB4);
        
        jpino.setLayout(new BorderLayout());
        jpino.add(jpin);
        
        jP.setLayout(new GridLayout(4,1));
        jP.add(jTF1);
        jP.add(jTF2);
        jP.add(jpino);
        jP.add(jTF3);
        
        jF.add(jP);
        jF.setVisible(true);
    }
}
