package Lap08.Lap08_3;
import javax.swing.*;
import java.awt.*;
public class TellerGUI {
    public JFrame jf;
    public JPanel[] jp;
    public JButton[] jb3;
    public String[] strbt ={"Deposit","Withdraw","Exit"};
    public JLabel[] jl2;
    public String[] strlb = {"Balance","Amount"};
    public JTextField[] jt2;
    
    public TellerGUI(){
        jf = new JFrame();
        
        jp = new JPanel[4];
        for(int i = 0 ;i<4;i++){
            jp[i] = new JPanel();
        }
        
        jl2 = new JLabel[2];
        for(int i = 0 ; i< 2;i++){
            jl2[i] = new JLabel(strlb[i]);
        }
        
        jt2 = new JTextField[2];
        for(int i = 0 ; i<2 ;i++){
            jt2[i] = new JTextField();
        }
        jt2[0].setText("6000");
        jt2[0].setEditable(false);
        
        jb3 = new JButton[3];
        for(int i = 0 ; i<strbt.length; i++){
            jb3[i] = new JButton(strbt[i]);
        }
        
        jp[0].setLayout(new GridLayout(1,2));
        jp[0].add(jl2[0]);
        jp[0].add(jt2[0]);
        
        jp[1].setLayout(new GridLayout(1,2));
        jp[1].add(jl2[1]);
        jp[1].add(jt2[1]);
        
        jp[2].setLayout(new GridLayout(1,3));
        jp[2].add(jb3[0]);
        jp[2].add(jb3[1]);
        jp[2].add(jb3[2]);
        
        jf.setTitle("Teller GUI");
        jf.setLayout(new GridLayout(4,1));
        jf.add(jp[0]);
        jf.add(jp[1]);
        jf.add(jp[2]);
        jf.add(jp[3]);
        jf.setSize(300,200);
        jf.setDefaultCloseOperation(3);
        jf.setVisible(true);
    }
}
