package Lap12.Lap12_2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class StudentView implements ActionListener,WindowListener{
    private JFrame jf;
    private JLabel jl[];
    private String jllist[] = {"     ID : ","     Name : ","     Money : "};
    private JTextField jtf[];
    private JButton jb[];
    private String jblist[] = {"Deposit","Withdraw"};
    private JPanel jp[];
    private Student s;
    
    public StudentView(){
        jf = new JFrame("StudentView");
        
        jp = new JPanel[4];
        for(int i = 0; i < 4;i++){
            jp[i] = new JPanel();
        }
        
        jl = new JLabel[3];
        jp[2].setLayout(new GridLayout(3,1));
        for(int i = 0;i < 3;i++){
            jl[i] = new JLabel(jllist[i]);
            jp[2].add(jl[i]);
        }
        
        jtf = new JTextField[3];
        jp[3].setLayout(new GridLayout(3,1));
        for(int i= 0;i < 3; i++){
            jtf[i] = new JTextField();
            jp[3].add(jtf[i]);
        }
        jtf[2].setText(String.valueOf(0));
        jtf[2].setEditable(false);
        
        jb = new JButton[2];
        jp[1].setLayout(new FlowLayout());
        for(int i = 0 ; i < 2 ; i++){
            jb[i] = new JButton(jblist[i]);
            jp[1].add(jb[i]);
        }
        jb[0].addActionListener(this);
        jb[1].addActionListener(this);
        
        jp[0].setLayout(new GridLayout(1,2));
        jp[0].add(jp[2]);
        jp[0].add(jp[3]);
        
        jf.setLayout(new BorderLayout());
        jf.add(jp[0],BorderLayout.CENTER);
        jf.add(jp[1],BorderLayout.SOUTH);
        
        jf.setSize(300, 200);
        jf.setDefaultCloseOperation(3);
        jf.addWindowListener(this);
        jf.setVisible(true);
    }
    
    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(jb[0])){
            s.setMoney(s.getMoney()+100);
            jtf[2].setText(String.valueOf(s.getMoney()));
        }else if(e.getSource().equals(jb[1])){
            s.setMoney(s.getMoney()-100);
            jtf[2].setText(String.valueOf(s.getMoney()));
        }
    }
    
    @Override
    public void windowOpened(WindowEvent e){
        try(FileInputStream input = new FileInputStream("StudentM.dat");
            ObjectInputStream in = new ObjectInputStream(input); ){
            s =(Student) in.readObject();
            jtf[0].setText(s.getID() == 0 ? "" : String.valueOf(s.getID()));
            jtf[1].setText(s.getName());
            jtf[2].setText(String.valueOf(s.getMoney()));
            in.close();
            input.close();
            System.out.println("อ่านแล้ว...");
        }catch (IOException | ClassNotFoundException ex) {
            s = new Student();
            System.out.println("ไม่พบข้อมูล...");
            System.out.println("Error: " + ex);
        }
    }
    @Override
    public void windowClosing(WindowEvent e){
        try(FileOutputStream output = new FileOutputStream("StudentM.dat");
            ObjectOutputStream out = new ObjectOutputStream(output); ){
            s.setName(jtf[1].getText());
            if(!jtf[0].getText().equals("")){
                s.setID(Integer.parseInt(jtf[0].getText()));
            }else{
                s.setID(0);
            }
            out.writeObject(s);
            out.close();
            output.close();
            System.out.println("บันทึกแล้วว...");
        }catch (IOException ex) {
            System.out.println("Error: " + ex);
        }
    }
    @Override
    public void windowClosed(WindowEvent e){}
    @Override
    public void windowIconified(WindowEvent e){}
    @Override
    public void windowDeiconified(WindowEvent e){}
    @Override
    public void windowActivated(WindowEvent e){}
    @Override
    public void windowDeactivated(WindowEvent e){}
}
