package Lap12.Lap12_1;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import javax.swing.*;
public class ChatDemo implements WindowListener,ActionListener{
    private JFrame jf;
    private JPanel jp1,jp2;
    private JButton jb1,jb2;
    private JTextField jtf1;
    private JTextArea jta1;
    private String textfromfile = "";
    
    public ChatDemo(){
        jf = new JFrame("ChatDemo1");
        jp1 = new JPanel();
        jp2 = new JPanel();
        jta1 = new JTextArea();
        jtf1 = new JTextField();
        jb1 = new JButton("Submit");
        jb2 = new JButton("Reset");
        JScrollPane scrollPane = new JScrollPane(jta1);
        
        jb1.addActionListener(this);
        jb2.addActionListener(this);
        
        jp2.setLayout(new FlowLayout());
        jp2.add(jb1);
        jp2.add(jb2);
        
        jp1.setLayout(new GridLayout(2,1));
        jp1.add(jtf1);
        jp1.add(jp2);
       

        jta1.setEditable(false);
      
        jf.setLayout(new BorderLayout());
        jf.add(scrollPane,BorderLayout.CENTER);
        jf.add(jp1,BorderLayout.SOUTH);
        
        jf.setSize(600, 500);
        jf.setDefaultCloseOperation(3);
        jf.addWindowListener(this);
        jf.setVisible(true);
    }
    @Override
    public void windowOpened(WindowEvent e){
       if(e.getSource().equals(jf)){
            try(FileInputStream readfile = new FileInputStream("ChatDemo.dat");){
                int i = readfile.read();
                while(i != -1){
                    this.textfromfile = this.textfromfile+String.valueOf((char) i);
                    i = readfile.read();
                }
                readfile.close();
            } catch(IOException ex){
                System.out.println(ex);
                System.out.println("Error read");
            }finally{
                jta1.setText(textfromfile);
                System.out.println("อ่านแล้วว....");
            }   
       }
    }
    @Override
    public void windowClosing(WindowEvent e) {
        try(FileOutputStream fin = new FileOutputStream("ChatDemo.dat");){
            String te = jta1.getText();
            for(int i = 0; i < te.length(); i++ ){
                fin.write(te.charAt(i));
            }
            fin.close();
        } catch(IOException ex){
            System.out.println(ex);
            System.out.println("Error write");
        }finally{
            System.out.println("บันทึกแล้ว");
        }

        System.exit(0);
    }    
    @Override
    public void actionPerformed(ActionEvent e){
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
        if(e.getSource().equals(jb1)){
            jta1.setText(jta1.getText()+"\n"+dtf.format(LocalDateTime.now())+": "+jtf1.getText());
        } else if(e.getSource().equals(jb2)){
            jta1.setText("");
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
