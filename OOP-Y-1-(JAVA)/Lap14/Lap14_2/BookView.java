
package Lap14.Lap14_2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;

public class BookView implements ActionListener,WindowListener{
    private JFrame jf;
    private JPanel jp1,jp2,jp3,jp4,jp5,jp6;
    private JLabel name,price,type;
    private JTextField name_t,price_t,num;
    private JComboBox type_t;
    private JButton left,rigth,add,update,delete;
    
    private ArrayList<Book> list;
    
    public BookView(){
        jf = new JFrame();
        
        jp1 = new JPanel();
        name = new JLabel("   Name");
        price = new JLabel("   Price");
        type = new JLabel("   Type");
        jp1.setLayout(new GridLayout(3,1));
        jp1.add(name);
        jp1.add(price);
        jp1.add(type);
        
        jp2 = new JPanel();
        name_t = new JTextField();
        price_t = new JTextField();
        type_t = new JComboBox();
        type_t.addItem("General");
        type_t.addItem("Computer");
        type_t.addItem("Math&Sci");
        type_t.addItem(" Photo3");
        jp2.setLayout(new GridLayout(3,1));
        jp2.add(name_t);
        jp2.add(price_t);
        jp2.add(type_t);
        
        jp3 = new JPanel();
        jp3.setLayout(new GridLayout(1,2));
        jp3.add(jp1);
        jp3.add(jp2);
        
        jp4 = new JPanel();
        left = new JButton("<<<");
        rigth = new JButton(">>>");
        num = new JTextField("0",2);
        num.setEditable(false);
        jp4.setLayout(new FlowLayout());
        left.addActionListener(this);
        rigth.addActionListener(this);
        jp4.add(left);
        jp4.add(num);
        jp4.add(rigth);
        
        jp5 = new JPanel();
        add = new JButton("Add");
        update = new JButton("Update");
        delete = new JButton("Delete");
        jp5.setLayout(new FlowLayout());
        add.addActionListener(this);
        update.addActionListener(this);
        delete.addActionListener(this);
        jp5.add(add);
        jp5.add(update);
        jp5.add(delete);
        
        jp6 = new JPanel();
        jp6.setLayout(new GridLayout(2,1));
        jp6.add(jp4);
        jp6.add(jp5);
        
        jf.setLayout(new BorderLayout());
        jf.add(jp3);
        jf.add(jp6,BorderLayout.SOUTH);
        
        jf.addWindowListener(this);
        jf.setSize(400,300);
        jf.setDefaultCloseOperation(3);
        jf.setVisible(true);
    }
    
    public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(add)){
            new BookAdd(list,this);
        }
        else if(e.getSource().equals(left)){
            int num_int = Integer.parseInt(num.getText());
            if(num_int > 0){
                setNum(num_int-1);
            }
        }
        else if(e.getSource().equals(rigth)){
            int num_int = Integer.parseInt(num.getText());
            if(num_int < list.size()-1){
                setNum(num_int+1);
            }
        }else if(e.getSource().equals(update)){
            int num_int = Integer.parseInt(num.getText());
            if(!list.isEmpty()){
                String name_b = name_t.getText();
                double price_b;
                String type_b = (type_t.getSelectedItem()).toString();
                try{
                    price_b = Double.parseDouble(price_t.getText());
                }catch(NumberFormatException ex){
                    price_b  = 0.0;
                }
                list.set(num_int,new Book(name_b,price_b,type_b));
                JOptionPane.showMessageDialog(jf,"Done it.");
            }
        }
        else if(e.getSource().equals(delete)){
            int num_int = Integer.parseInt(num.getText());
            if(!list.isEmpty()){
                list.remove(num_int);
                JOptionPane.showMessageDialog(jf,"Done it.");
            }
            setNum(0);
        }
    }
    
    public void setNum(int n){
        if(!list.isEmpty()){
            String name_b = list.get(n).getName();
            double price_b = list.get(n).getPrice();
            String type_b = list.get(n).getType();
            name_t.setText(name_b);
            price_t.setText(price_b+"");
            type_t.setSelectedItem(type_b);
            num.setText(n+"");
        }
        else{
            name_t.setText("");
            price_t.setText("");
            type_t.setSelectedItem("General");
            num.setText(n+"");
        }
    }
    
    @Override
    public void windowOpened(WindowEvent e){
        try(FileInputStream inp = new FileInputStream("Book.data");
            ObjectInputStream oinp = new ObjectInputStream(inp);){
            list = (ArrayList<Book>) oinp.readObject();
        }catch(Exception ex){
            list = new ArrayList();
        }
        setNum(0);
    }
    @Override
    public void windowClosing(WindowEvent e){
        try(FileOutputStream out = new FileOutputStream("Book.data");
            ObjectOutputStream oout = new ObjectOutputStream(out);){
            oout.writeObject(list);
        }catch(IOException ex){
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
    public static void main(String[] args) {
        new BookView();
    }
}
