package Lap08.Lap08_4;
import javax.swing.*;
import java.awt.event.*;
public class MDIFromGUI {
   public JFrame jf;
   public JDesktopPane jdt;
   public JInternalFrame jid1,jid2,jid3;
   public JMenuBar menuBar;
   public JMenu menu1,menu2,menu3;
   public JMenuItem imenu1,imenu1_1,imenu1_2,imenu2,imenu3,imenu4;
   public int newWindowint = 0;
   public MDIFromGUI(){
       jf = new JFrame();
       jdt = new JDesktopPane();
       jid1 = new JInternalFrame("Ap1",true,true,true,true);
       jid2 = new JInternalFrame("Ap2",true,true,true,true);
       jid3 = new JInternalFrame("Ap3",true,true,true,true);
       
       jid1.setVisible(true);
       jid1.setSize(300,300);
       jid1.setLocation(0, 0);
       jid2.setVisible(true);
       jid2.setSize(300,300);
       jid2.setLocation(300, 300);
       jid3.setVisible(true);
       jid3.setSize(300,300);
       jid3.setLocation(600, 600);
       jdt.add(jid1);
       jdt.add(jid2);
       jdt.add(jid3);
       jf.add(jdt);
       
       menuBar = new JMenuBar();
       menu1 = new JMenu("File");
       menu2 = new JMenu("Edit");
       menu3 = new JMenu("View");
       imenu1 = new JMenu("New");
       imenu1_1 = new JMenuItem("Window");
       imenu1_2 = new JMenuItem("Message");
       imenu2 = new JMenuItem("Open");
       imenu3 = new JMenuItem("Save");
       imenu4 = new JMenuItem("Exit");
       
       menu1.add(imenu1);
       menu1.add(imenu2);
       menu1.addSeparator();
       menu1.add(imenu3);
       menu1.addSeparator();
       menu1.add(imenu4);
             
       imenu1.add(imenu1_1);
       imenu1.add(imenu1_2);
       
       menuBar.add(menu1);
       menuBar.add(menu2);
       menuBar.add(menu3);
       
       jf.setTitle("MDI");
       jf.setJMenuBar(menuBar);
       jf.setSize(1000,1000);
       jf.setDefaultCloseOperation(3);
       jf.setVisible(true);
   }
}
