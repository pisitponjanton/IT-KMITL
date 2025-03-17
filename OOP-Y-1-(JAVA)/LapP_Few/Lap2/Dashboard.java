
package LapP_Few.Lap2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.*;
import javax.swing.table.DefaultTableModel;

public class Dashboard implements ActionListener{
    private JPanel jp,jp1,jp2;
    private JLabel text;
    private JButton add_item, edit_item, logout;
    private JTable table;
    private DefaultTableModel model;
    private ArrayList<Item> list;
    
    private Main m;
    private JFrame jf;
    
    public Dashboard(JFrame jf){
        loadData();
        this.jf = jf;
        jp = new JPanel();
        
        jp1 =new JPanel();
        text = new JLabel("Welcome to Jisoo Marketplace",JLabel.CENTER);
        jp1.setLayout(new GridLayout(2,1));
        
        jp2 = new JPanel();
        jp2.setLayout(new FlowLayout());
        add_item = new JButton("Add Item");
        edit_item = new JButton("Edit Item");
        logout = new JButton("Logout");
        add_item.addActionListener(this);
        edit_item.addActionListener(this);
        logout.addActionListener(this);
        jp2.add(add_item);
        jp2.add(edit_item);
        jp2.add(logout);
        
        jp1.add(text);
        jp1.add(jp2);
        
        table = new JTable();
        model = (DefaultTableModel) table.getModel();
        model.addColumn("ID");
        model.addColumn("Name");
        model.addColumn("Price");
        model.addColumn("Created_On");
        
        JScrollPane sc = new JScrollPane(table);
        jp.setLayout(new GridLayout(2,1));
        jp.add(jp1);
        jp.add(sc);
        reLoad();
    }
    
    public DefaultTableModel getModel(){
        return this.model;
    }
    
    public void reLoad(){
        Iterator<Item> it = list.iterator();
        model.setRowCount(0);
        while(it.hasNext()){
            Item itt = it.next();
            model.addRow(new Object[]{itt.getId(), itt.getName(), itt.getPrice(), itt.getCreated_On()});
        }
    }
    
     public void loadData(){
        try(FileInputStream inp = new FileInputStream("jisso_shop.dat");
            ObjectInputStream oinp = new ObjectInputStream(inp);){
            list = (ArrayList<Item>) oinp.readObject();
        }catch(Exception e){
            list = new ArrayList<>();
            System.out.println("null");
        }
    }
    
    public void saveData(){
        try(FileOutputStream onp = new FileOutputStream("jisso_shop.dat");
            ObjectOutputStream oonp = new ObjectOutputStream(onp);){
            oonp.writeObject(list);
            System.out.println("Save");
        }catch(Exception e){
        }
    }
    
    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(add_item)){
            new AddItem(list,this);
        }else if(e.getSource().equals(logout)){
            jf.setContentPane(new Login(jf).getJP());
            jf.revalidate();
            jf.repaint();
            saveData();
            System.out.println("Logout");
        }else if(e.getSource().equals(edit_item)){
            new EditItem(list,this);
        }
            
    }
    
    public JPanel getJP(){
        return this.jp;
    }
}
