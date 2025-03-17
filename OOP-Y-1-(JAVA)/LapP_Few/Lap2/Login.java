
package LapP_Few.Lap2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Login implements ActionListener{
    private JPanel jp,jp1,jp2,jp3,jp4;
    private JTextField name_t,password_t;
    private JLabel name,password;
    private JButton login;
    private JFrame m;
    
    
    public Login(JFrame m){
        jp = new JPanel();
        this.m = m;
        jp1 = new JPanel();
        jp1.setLayout(new GridLayout(2,1));
        name = new JLabel("   Login");
        password = new JLabel("   Password");
        jp1.add(name);
        jp1.add(password);
        
        jp2 = new JPanel();
        jp2.setLayout(new GridLayout(2,1));
        name_t = new JTextField();
        password_t = new JTextField();
        jp2.add(name_t);
        jp2.add(password_t);
        
        jp3 = new JPanel();
        jp3.setLayout(new GridLayout(1,2));
        jp3.add(jp1);
        jp3.add(jp2);
        
        jp4 = new JPanel();
        jp4.setLayout(new GridLayout(3,1));
        login = new JButton("Login");
        login.addActionListener(this);
        jp4.add(new JPanel());
        jp4.add(login);
        jp4.add(new JPanel());
        
        jp.setLayout(new GridLayout(3,1));
        jp.add(new JPanel());
        jp.add(jp3);
        jp.add(jp4);
        
    }
    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(login)){
            if(name_t.getText().equals("jisoo") && password_t.getText().equals("flower_me")){
                m.setContentPane(new Dashboard(m).getJP());
                m.revalidate();
                m.repaint();
                System.out.println("Login");
            }
        }
    }
    public JPanel getJP(){
        return this.jp;
    }
}
