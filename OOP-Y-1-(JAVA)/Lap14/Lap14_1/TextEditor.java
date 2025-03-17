
package Lap14.Lap14_1;

import javax.swing.*;
import java.awt.event.*;
import java.io.*;

public class TextEditor implements ActionListener{
    private JFrame jf;
    private JMenuBar menubar;
    private JMenu menu;
    private JMenuItem menu_new,menu_open,menu_save,menu_close;
    private JTextArea jta;
    
    public TextEditor(){
        jf = new JFrame("My Text Editor");
        jta = new JTextArea();
        menubar = new JMenuBar();
        menu = new JMenu("File");
        menu_new = new JMenuItem("New");
        menu_new.addActionListener(this);
        menu_open = new JMenuItem("Open");
        menu_open.addActionListener(this);
        menu_save = new JMenuItem("Save");
        menu_save.addActionListener(this);
        menu_close = new JMenuItem("Close");
        menu_close.addActionListener(this);
        
        menu.add(menu_new);
        menu.add(menu_open);
        menu.add(menu_save);
        menu.addSeparator();
        menu.add(menu_close);
        
        menubar.add(menu);
        JScrollPane sc = new JScrollPane(jta);
        jf.add(sc);
        jf.setJMenuBar(menubar);
        jf.setDefaultCloseOperation(3);
        jf.setSize(400,300);
        jf.setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(menu_new)){
            jta.setText("");
        }
        else if(e.getSource().equals(menu_open)){
            JFileChooser fc = new JFileChooser();
            fc.showOpenDialog(jf); 
            File f = fc.getSelectedFile();
            loadData(f.toString());
        }
        else if(e.getSource().equals(menu_save)){
            JFileChooser fc = new JFileChooser();
            fc.showSaveDialog(jf);
            File f = fc.getSelectedFile();
            saveData(f.toString());
            jta.setText("");
        }else if(e.getSource().equals(menu_close)){
            System.exit(0);
        }
    }
    
    private void loadData(String path){
        try(FileInputStream inp = new FileInputStream(path);){
            int i = inp.read();
            while(i!=-1){
                jta.setText(jta.getText() + ((char) i));
                i = inp.read();
            }
        }catch(Exception e){
        }
    }
    
    private void saveData(String path){
        try(FileOutputStream op = new FileOutputStream(path);){
            String str = jta.getText();
            for(int i = 0;i < str.length();i++){
                op.write(str.charAt(i));
            }
        }catch(Exception e){
        }
    }
    
    public static void main(String[] args) {
        new TextEditor();
    }
}
