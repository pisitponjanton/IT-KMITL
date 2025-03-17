
package LapP_Few.Lap2;

import javax.swing.*;
import java.awt.*;
import java.util.*;
import java.awt.event.*;

public class AddItem implements ActionListener{
    private JFrame jf;
    private JPanel jp,jp1;
    private JLabel id,name,price;
    private JTextField id_t,name_t,price_t;
    private JButton insert_item;
    private ArrayList<Item> list;
    
    private Dashboard d;
    
    public AddItem(ArrayList<Item> list,Dashboard d){
        this.list = list;
        this.d =d;
        jf = new JFrame();
        
        jp = new JPanel();
        id = new JLabel("   ID");
        name = new JLabel("   name");
        price = new JLabel("   price");
        id_t = new JTextField();
        name_t = new JTextField();
        price_t = new JTextField();
        jp.setLayout(new GridLayout(3,3));
        jp.add(id);
        jp.add(id_t);
        jp.add(name);
        jp.add(name_t);
        jp.add(price);
        jp.add(price_t);
        
        jp1 = new JPanel();
        insert_item = new JButton("Insert Item");
        insert_item.addActionListener(this);
        jp1.add(insert_item);
        
        jf.setLayout(new BorderLayout());
        jf.add(jp);
        jf.add(jp1,BorderLayout.SOUTH);
        jf.setSize(500,300);
        jf.setDefaultCloseOperation(2);
        jf.setVisible(true);
    }
    
    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(insert_item)){
            int id_b = Integer.parseInt(id_t.getText());
            String name_b = name_t.getText();
            double price_b = Double.parseDouble(price_t.getText());
            list.add(new Item(id_b,name_b,price_b,new Date()));
            JOptionPane.showMessageDialog(jf, "Done it.");
            d.reLoad();
            jf.dispose();
        }
    }
}
