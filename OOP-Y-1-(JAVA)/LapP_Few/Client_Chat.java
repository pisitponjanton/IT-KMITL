package LapP_Few;

import javax.swing.*;
import java.awt.*;

public class Client_Chat{
    private JFrame jf;
    private JScrollPane sc;
    private JPanel jp;
    private JTextArea jta;
    private JTextField jtf;
    private JButton send;
    
    public Client_Chat(String name){
        jf = new JFrame("Client "+name);
        jta = new JTextArea();
        jtf = new JTextField();
        send = new JButton("Send");
        
        jta.setEditable(false);
        
        jp = new JPanel();
        jp.setLayout(new BorderLayout());
        jp.add(jtf);
        jp.add(send,BorderLayout.EAST);
        
        sc = new JScrollPane(jta);
        jf.setLayout(new BorderLayout());
        jf.add(sc);
        jf.add(jp,BorderLayout.SOUTH);
        
        jf.setSize(500,400);
        jf.setDefaultCloseOperation(3);
    }
    
    public JFrame getJF(){
        return this.jf;
    }
    
    public JTextArea getJTA(){
        return this.jta;
    }
    
    public JTextField getJTF(){
        return this.jtf;
    }
    
    public JButton getSend(){
        return this.send;
    }
}
