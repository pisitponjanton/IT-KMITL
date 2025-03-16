
package LapP_Few;

import java.awt.event.*;
import java.io.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Chatbox implements ActionListener,WindowListener{
    private Client_Chat a;
    private Client_Chat b;
    private String text = "";
    
    public Chatbox(){
        a = new Client_Chat("A");
        b = new Client_Chat("B");
        b.getJF().setLocation(a.getJF().getX()+720,a.getJF().getY());
        a.getSend().addActionListener(this);
        b.getSend().addActionListener(this);
        a.getJF().setVisible(true);
        b.getJF().setVisible(true);
        a.getJF().addWindowListener(this);
        b.getJF().addWindowListener(this);
    }
    
    @Override
    public void actionPerformed(ActionEvent e){
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
        if(e.getSource().equals(a.getSend())){
            text = text+ "\n" +"[" + dtf.format(LocalDateTime.now()) + "] A: "+ a.getJTF().getText();
            a.getJTA().setText(text.replace("] A: ","] A (You): "));
            b.getJTA().setText(text.replace("] B: ","] B (You): "));
        }else if(e.getSource().equals(b.getSend())){
            text = text+ "\n" +"[" + dtf.format(LocalDateTime.now()) + "] B: "+ b.getJTF().getText();
            a.getJTA().setText(text.replace("] A: ","] A (You): "));
            b.getJTA().setText(text.replace("] B: ","] B (You): "));
        }
    }
    
    @Override
    public void windowOpened(WindowEvent e){
        if(e.getSource().equals(a.getJF())){
            try(FileInputStream inp = new FileInputStream("chat_history.dat");){
                int i = inp.read();
                while(i!=-1){
                    text = text + (char) i;
                    i = inp.read();
                }
                a.getJTA().setText(text.replace("] A: ","] A (You): "));
                b.getJTA().setText(text.replace("] B: ","] B (You): "));
            }catch(Exception ex){
            }
        }
    }
    @Override
    public void windowClosing(WindowEvent e){
        try(FileOutputStream inp = new FileOutputStream("chat_history.dat");){
            for(int i = 0; i<text.length();i++){
                inp.write(text.charAt(i));
            }
        }catch(Exception ex){
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
    
    public static void main(String[] args) {
        new Chatbox();
    }
}
