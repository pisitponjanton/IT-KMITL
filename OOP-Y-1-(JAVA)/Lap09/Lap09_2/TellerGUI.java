package Lap09.Lap09_2;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class TellerGUI implements ActionListener{
    private JFrame jf;
    private JPanel jp1,jp2,jp3,jp4;
    private JButton jb1,jb2,jb3;
    private JLabel jlb1,jlb2;
    private JTextField jt1,jt2;
    private int balance = 6000 ;
    public TellerGUI(){
        jf = new JFrame("Teller GUI");
        jp1 = new JPanel();
        jp2 = new JPanel();
        jp3 = new JPanel();
        jp4 = new JPanel();
        jt1 = new JTextField(String.valueOf(this.getBalance()));
        jt2 = new JTextField("");
        jlb1 = new JLabel("Balance");
        jlb2 = new JLabel("Amount");
        jb1 = new JButton("Deposit");
        jb2 = new JButton("Withdraw");
        jb3 = new JButton("Exit");
        
        jb1.addActionListener(this);
        jb2.addActionListener(this);
        jb3.addActionListener(this);
        
        
        jt1.setEditable(false);
        
        jp1.setLayout(new GridLayout(1,2));
        jp1.add(jlb1);
        jp1.add(jt1);
        
        jp2.setLayout(new GridLayout(1,2));
        jp2.add(jlb2);
        jp2.add(jt2);
        
        jp3.setLayout(new GridLayout(1,3));
        jp3.add(jb1);
        jp3.add(jb2);
        jp3.add(jb3);
        
        jf.setLayout(new GridLayout(4,1));
        jf.add(jp1);
        jf.add(jp2);
        jf.add(jp3);
        jf.add(jp4);
        jf.setSize(300,200);
        jf.setDefaultCloseOperation(3);
        jf.setVisible(true);
    }
    public void setBalance(int balance){
        this.balance = balance;
    }
    public int getBalance(){
        return this.balance;
    }
    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(jb1)){
            this.setBalance(this.getBalance()+Integer.parseInt(jt2.getText()));
            jt1.setText(String.valueOf(this.getBalance()));
            jt2.setText("");
        }
        else if(e.getSource().equals(jb2)){
            if(this.getBalance()>=Integer.parseInt(jt2.getText())){
                this.setBalance(this.getBalance()-Integer.parseInt(jt2.getText()));
                jt1.setText(String.valueOf(this.getBalance()));
            }
            jt2.setText("");
        }
        else{
            System.exit(0);
        }
    }
}
