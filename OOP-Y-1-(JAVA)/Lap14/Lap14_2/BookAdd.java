
package Lap14.Lap14_2;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

public class BookAdd {
    private JFrame jf;
    private JPanel jp1,jp2,jp3,jp4;
    private JTextField jtf_name,jtf_price;
    private JComboBox jcb;
    private JLabel name,price,type;
    private JButton jb;
    private ArrayList<Book> list;
    private BookView b;
    
    public BookAdd(ArrayList<Book> list,BookView b){
        this.list = list;
        this.b = b;
        jf = new JFrame("Book Add");
        jp1 = new JPanel();
        jp1.setLayout(new GridLayout(3,1));
        name = new JLabel("  Name");
        price = new JLabel(" Price");
        type = new JLabel("  Type");
        jp1.add(name);
        jp1.add(price);
        jp1.add(type);
        
        jp2 = new JPanel();
        jp2.setLayout(new GridLayout(3,1));
        jtf_name = new JTextField();
        jtf_price = new JTextField();
        jcb = new JComboBox();
        jcb.addItem("Genera");
        jcb.addItem("Computer");
        jcb.addItem("Math&Sci");
        jcb.addItem("Photo");
        jp2.add(jtf_name);
        jp2.add(jtf_price);
        jp2.add(jcb);
        
        jp3 = new JPanel();
        jp3.setLayout(new GridLayout(1,2));
        jp3.add(jp1);
        jp3.add(jp2);
        
        jp4 = new JPanel();
        jb = new JButton("Insert");
        jb.addActionListener(_->{
            String name = jtf_name.getText();
            double price = Double.parseDouble(jtf_price.getText());
            String type = jcb.getSelectedItem().toString();
            this.list.add(new Book(name,price,type));
            b.showList(list.size()-1);
            JOptionPane.showMessageDialog(jf,"Done it.");
            jf.dispose();
        });
        jp4.add(jb);
        
        jf.setLayout(new BorderLayout());
        jf.add(jp3);
        jf.add(jp4,BorderLayout.SOUTH);
        jf.setSize(300,200);
        jf.setDefaultCloseOperation(2);
        jf.setVisible(true);
    }
}
