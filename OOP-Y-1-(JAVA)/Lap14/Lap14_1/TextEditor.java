
package Lap14.Lap14_1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.nio.file.Path;

public class TextEditor implements ActionListener{
    private JFrame jf;
    private JPanel jp;
    private JMenuBar menuBar;
    private JMenu menu1;
    private JMenuItem menuItem1,menuItem2,menuItem3,menuItem4;
    private JTextArea jta;
    
    public TextEditor(){
        jf = new JFrame("My Text Editor");
        jta = new JTextArea();
        menuBar = new JMenuBar();
        menu1 = new JMenu("File");
        menuItem1 = new JMenuItem("New");
        menuItem2 = new JMenuItem("Open");
        menuItem3 = new JMenuItem("Save");
        menuItem4 = new JMenuItem("Close");
  
        menuItem1.addActionListener(this);
        menuItem2.addActionListener(this);
        menuItem3.addActionListener(this);
        menuItem4.addActionListener(this);
        
        menu1.add(menuItem1);
        menu1.add(menuItem2);
        menu1.add(menuItem3);
        menu1.addSeparator();
        menu1.add(menuItem4);
        menuBar.add(menu1);
        
        jf.setLayout(new BorderLayout());
        jf.add(jta);
        jf.setJMenuBar(menuBar);
        jf.setSize(400,300);
        jf.setDefaultCloseOperation(3);
        jf.setVisible(true);
    }
    
     public void actionPerformed(ActionEvent e){
         if(e.getSource().equals(menuItem1)){
             jta.setText("");
         }
         else if(e.getSource().equals(menuItem2)){
             JFileChooser fc = new JFileChooser();
             fc.showOpenDialog(fc);
             File f = fc.getSelectedFile();
             loadData(f.toString());
         }
        else if(e.getSource().equals(menuItem3)){
             JFileChooser fc = new JFileChooser();
             fc.showSaveDialog(fc);
             File f = fc.getSelectedFile();
             saveData(f.toString());
         }
         else if(e.getSource().equals(menuItem4)){
             System.exit(0);
         }
     }
     
    private void loadData(String path){
        try(FileInputStream input = new FileInputStream(path)){
            int i = input.read();
            String text = "";
            while(i!=-1){
                text = text + String.valueOf((char) i);
                i = input.read();
            }
            jta.setText(text);
            input.close();
        }catch(Exception e){
        }
    }
    
    private void saveData(String path){
        try(FileOutputStream output = new FileOutputStream(path)){
            String text = jta.getText();
            for(int i = 0; i<text.length(); i++){
                output.write(text.charAt(i));
            }
            jta.setText("");
            output.close();
        }catch(Exception e){
        }
    }
    
    public static void main(String[] args) {
        new TextEditor();
    }
    
}
