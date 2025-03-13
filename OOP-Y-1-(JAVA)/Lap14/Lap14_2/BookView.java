package Lap14.Lap14_2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;

public class BookView implements WindowListener,Serializable{
    private ArrayList<Book> list;
    private JFrame jf;
    private JComboBox jcb;
    private JPanel[] jp;
    private JTextField[] jtf;
    private JTextField jtf_num;
    private JLabel[] jlb;
    private String[] textjlb = {"  Name","  Price","  Type"};
    private JButton[] jb;
    private String[] textjb = {"<<<",">>>","Add","Update","Delete"};
    public BookView(){
        jf = new JFrame("Book View");
        jtf_num = new JTextField("0");
        jtf_num.setPreferredSize(new Dimension(50, 30));
        jtf_num.setEditable(false);
        jcb = new JComboBox();
        jcb.addItem("Genera");
        jcb.addItem("Computer");
        jcb.addItem("Math&Sci");
        jcb.addItem("Photo");
        jp = new JPanel[6];
        for(int i = 0;i< jp.length;i++){
            jp[i] = new JPanel();
        }
        
        jp[0].setLayout(new GridLayout(3,1));
        jlb = new JLabel[3];
        for(int i = 0;i< textjlb.length;i++){
            jlb[i] = new JLabel(textjlb[i]);
            jp[0].add(jlb[i]);
        }
        
        jp[1].setLayout(new GridLayout(3,1));
        jtf = new JTextField[2];
        for(int i = 0; i<jtf.length;i++){
            jtf[i] = new JTextField();
            jp[1].add(jtf[i]);
        }
        jp[1].add(jcb);
        
        jb = new JButton[5];
        for(int i = 0;i<textjb.length;i++){
            jb[i] = new JButton(textjb[i]);
        }
        jp[4].setLayout(new FlowLayout());
        jb[0].addActionListener(_->{
            showList(Integer.parseInt(jtf_num.getText())-1);
        });
        jb[1].addActionListener(_->{
            showList(Integer.parseInt(jtf_num.getText())+1);
        });
        jp[4].add(jb[0]);
        jp[4].add(jtf_num);
        jp[4].add(jb[1]);
        
        jp[2].setLayout(new GridLayout(1,2));
        jp[2].add(jp[0]);
        jp[2].add(jp[1]);
        
        jp[3].setLayout(new BorderLayout());
        jp[3].add(jp[2]);
        jp[3].add(jp[4],BorderLayout.SOUTH);
        
        jp[5].setLayout(new FlowLayout());
        jb[2].addActionListener(_->{
            BookAdd bookadd = new BookAdd(list,this);
        });
        jb[3].addActionListener(_->{
            int index = Integer.parseInt(jtf_num.getText());
            try{
                String name = jtf[0].getText();
                double price = Double.parseDouble(jtf[1].getText());
                String type = jcb.getSelectedItem().toString();
                this.list.set(index,new Book(name,price,type));
                showList(index);
                JOptionPane.showMessageDialog(jf, "Done it.");
            }catch(Exception e){
                
            }
        });
        jb[4].addActionListener(_->{
            int index = Integer.parseInt(jtf_num.getText());
            try{
                list.remove(index);
                jtf[0].setText("");
                jtf[1].setText("");
                jcb.setSelectedItem("Genera");
                JOptionPane.showMessageDialog(jf, "Done it.");
            }catch(HeadlessException e){
                
            }
        });
        jp[5].add(jb[2]);
        jp[5].add(jb[3]);
        jp[5].add(jb[4]);
        
        jf.addWindowListener(this);
        jf.setLayout(new BorderLayout());
        jf.add(jp[3]);
        jf.add(jp[5],BorderLayout.SOUTH);
        jf.setSize(400,300);
        jf.setDefaultCloseOperation(3);
        jf.setVisible(true);
    }
    public void showList(int index){
        try{
            Book book = list.get(index);
            jtf[0].setText(book.getName());
            jtf[1].setText(book.getPrice()+"");
            jcb.setSelectedItem(book.getType());
            jtf_num.setText(index+"");
        }catch(Exception e){
            
        }
    }
    @Override
    public void windowOpened(WindowEvent e){
        try(FileInputStream input = new FileInputStream("Book.data");
            ObjectInputStream oinput = new ObjectInputStream(input);){
            list = (ArrayList<Book>) oinput.readObject();
            showList(0);
            System.out.println("Load...");
        }catch(Exception ex){
            list = new ArrayList<>();
            System.out.println("Null");
        }
    }
    @Override
    public void windowClosing(WindowEvent e){
        try(FileOutputStream output = new FileOutputStream("Book.data");
            ObjectOutputStream ooutput = new ObjectOutputStream(output);){
            ooutput.writeObject(list);
            System.out.println("Save...");
        }catch(Exception ex){
            System.out.println("Not Save");
        }}
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
