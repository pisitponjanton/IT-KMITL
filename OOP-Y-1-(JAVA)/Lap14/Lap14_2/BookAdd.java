
package Lap14.Lap14_2;

import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;


public class BookAdd implements ActionListener{
    private JFrame jf;
    private JPanel jp1,jp2,jp3,jp4;
    private JLabel name,price,type;
    private JTextField name_t,price_t;
    private JComboBox type_t;
    private JButton insert;
    
    private ArrayList<Book> list;
    private BookView j;
    
    public BookAdd(ArrayList<Book> list,BookView j){
        jf = new JFrame();
        this.j = j;
        this.list = list;
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
        insert = new JButton("Insert");
        jp4.setLayout(new FlowLayout());
        insert.addActionListener(this);
        jp4.add(insert);
        
        jf.setLayout(new BorderLayout());
        jf.add(jp3);
        jf.add(jp4,BorderLayout.SOUTH);
        jf.setSize(300,200);
        jf.setDefaultCloseOperation(2);
        jf.setVisible(true);
    }
    
    @Override
       public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(insert)){
            String name_b = name_t.getText();
            double price_b;
            String type_b = (type_t.getSelectedItem()).toString();
            try{
                price_b = Double.parseDouble(price_t.getText());
            }catch(NumberFormatException ex){
                price_b  = 0.0;
            }
            list.add(new Book(name_b,price_b,type_b));
            j.setNum(list.size()-1);
            JOptionPane.showMessageDialog(jf,"Done it.");
            jf.dispose();
        }
    }
}
