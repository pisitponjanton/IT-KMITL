
package LapP_Few.Lap2;

import javax.swing.*;

public class Main {
    private boolean log;
    private JFrame jf;
    private Login login;
    
    
    public Main(){
        jf = new JFrame();
        login = new Login(jf);
        
        jf.setContentPane(login.getJP());
        jf.setDefaultCloseOperation(3);
        jf.setSize(600,300);
        jf.setVisible(true);
    }
    

    
    public static void main(String[] args) {
        new Main();
    }
}
