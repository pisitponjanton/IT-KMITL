
package LapP_Few.Lap2;

import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Date;
import javax.swing.*;

public class EditItem implements ActionListener{
    private JFrame jf;
    private JPanel jp,jp1,jp2,jp3;
    private JLabel id,name,price;
    private JTextField id_t,name_t,price_t;
    private JButton left,rigth,delete,update,close;
    
    private ArrayList<Item> list;
    private Dashboard d;
    private int page;
    
    public EditItem(ArrayList<Item> list,Dashboard d){
        this.list = list;
        this.d = d;
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
        left = new JButton("<<");
        rigth = new JButton(">>");
        left.addActionListener(this);
        rigth.addActionListener(this);
        jp1.setLayout(new FlowLayout());
        jp1.add(left);
        jp1.add(rigth);
        
        jp2 = new JPanel();
        delete = new JButton("Delete Item");
        update = new JButton("Update Item");
        close = new JButton("Close Item");
        jp2.setLayout(new FlowLayout());
        delete.addActionListener(this);
        update.addActionListener(this);
        close.addActionListener(this);
        jp2.add(delete);
        jp2.add(update);
        jp2.add(close);
        
        jp3 = new JPanel();
        jp3.setLayout(new GridLayout(2,1));
        jp3.add(jp1);
        jp3.add(jp2);
        
        load(0);
        
        jf.setLayout(new BorderLayout());
        jf.add(jp);
        jf.add(jp3,BorderLayout.SOUTH);
        jf.setSize(500,300);
        jf.setDefaultCloseOperation(2);
        jf.setVisible(true);
    }
    
    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(left)){
            if(!list.isEmpty()){
                if(page > 0){
                    load(page-1);
                    page--;
                }
            }
        }
        else if(e.getSource().equals(rigth)){
            if(!list.isEmpty()){
                if(page < list.size()-1){
                    load(page+1);
                    page++;
                }
            }
        }
        else if(e.getSource().equals(update)){
            if(!list.isEmpty()){
                int id_b = Integer.parseInt(id_t.getText());
                String name_b = name_t.getText();
                double price_b = Double.parseDouble(price_t.getText());
                Item it = list.set(page,new Item(id_b,name_b,price_b,new Date()));
                d.reLoad();
            }
        }
        else if(e.getSource().equals(close)){
            jf.dispose();
        }
        else if(e.getSource().equals(delete)){
            if(!list.isEmpty()){
                list.remove(page);
                page = 0;
                load(0);
                d.reLoad();
                JOptionPane.showMessageDialog(jf, "Done it.");
                jf.dispose();
            }
        }
    }
    
    public void load(int num){
        if(!list.isEmpty()){
            Item it = list.get(num);
            id_t.setText(it.getId()+"");
            name_t.setText(it.getName());
            price_t.setText(it.getPrice()+"");
        }else{
            id_t.setText("");
            name_t.setText("");
            price_t.setText("");
        }
        System.out.println(list);
    }

}
