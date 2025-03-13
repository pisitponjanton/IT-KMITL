package Lap13.Lap13_5;

import java.awt.event.*;
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.io.*;

public class Chatbox implements ActionListener,WindowListener{
    private String text;
    private ClientAChat a;
    private ClientBChat b;
    private DateTimeFormatter dtf;
    
    public Chatbox(){
        dtf = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
        a = new ClientAChat();
        b = new ClientBChat();
        this.loadData();
        
        a.getJB().addActionListener(this);
        b.getJB().addActionListener(this);
        a.getJf().addWindowListener(this);
        b.getJf().addWindowListener(this);
    }
    
    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(a.getJB())){
            String t = a.getJtf().getText();
            text = text + "\n" + "["+dtf.format(LocalDateTime.now())+"] "+"A: " + t;
            a.getJta().setText(text.replace("] A: ", "] A (You): "));
            b.getJta().setText(text.replace("] B: ", "] B (You): "));
        }else if(e.getSource().equals(b.getJB())){
            String t = b.getJtf().getText();
            text = text + "\n" + "["+dtf.format(LocalDateTime.now())+"] "+"B: " + t;
            a.getJta().setText(text.replace("] A: ", "] A (You): "));
            b.getJta().setText(text.replace("] B: ", "] B (You): "));
        }
    }
    @Override
    public void windowClosing(WindowEvent e){
        this.saveData();
    }
    @Override
    public void windowOpened(WindowEvent e){}
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
    
    private void loadData(){
        try(FileInputStream input = new FileInputStream("chat_history.dat");){
            int i = input.read();
            if(text == null)text="";
            while(i != -1){
                text = text + String.valueOf((char) i);
                i = input.read();
            }
            input.close();
            System.out.println("LoadData");
        }catch(IOException ex){
            System.out.println("NO Data");
            text = "";
        }finally{
            a.getJta().setText(text.replace("] A: ", "] A (You): "));
            b.getJta().setText(text.replace("] B: ", "] B (You): "));
        }
    }
    
    private void saveData(){
        try(FileOutputStream output = new FileOutputStream("chat_history.dat");){
            for(int i=0; i< text.length();i++){
                output.write(text.charAt(i));
            }
            output.close();
            System.out.println("SaveData");
        }catch(IOException ex){
            System.out.println("No Save Data");
        }
    }
    
    public static void main(String[] args) {
        new Chatbox();
    }
}
