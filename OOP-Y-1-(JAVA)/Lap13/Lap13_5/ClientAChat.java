package Lap13.Lap13_5;

import java.awt.*;
import javax.swing.*;

public class ClientAChat{
    private JFrame jf;
    private JTextArea jta;
    private JTextField jtf;
    private JButton jb;
    private JPanel jp;
    private ScrollPane sp;
    
    public ClientAChat(){
        jf = new JFrame("ClientAChat");
        jta = new JTextArea();
        jtf = new JTextField();
        jb = new JButton("Send");
        jp = new JPanel();
        sp = new ScrollPane();
        
        jta.setEditable(false);
        sp.add(jta);
        
        jp.setLayout(new BorderLayout());
        jp.add(jtf);
        jp.add(jb,BorderLayout.EAST);
        
        jf.setLayout(new BorderLayout());
        jf.add(sp);
        jf.add(jp,BorderLayout.SOUTH);
        jf.setSize(500,400);
        jf.setLocation(0, 500);
        jf.setDefaultCloseOperation(3);
        jf.setVisible(true);
    }
    
    public JButton getJB(){
        return this.jb;
    }
    
    public JTextArea getJta(){
        return this.jta;
    }
    
    public JTextField getJtf(){
        return this.jtf;
    }
    
    public JFrame getJf(){
        return this.jf;
    }
}
