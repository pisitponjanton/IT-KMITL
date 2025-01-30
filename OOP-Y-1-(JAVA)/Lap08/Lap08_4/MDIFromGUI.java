package Lap08.Lap08_4;
import javax.swing.*;
import java.awt.event.*;
public class MDIFromGUI {
   public JFrame jf;
   public JMenuBar menuBar;
   public JMenu menu1,menu2,menu3;
   public JMenuItem imenu1,imenu1_1,imenu1_2,imenu2,imenu3,imenu4;
   public int newWindowint = 0;
   public MDIFromGUI(){
       jf = new JFrame();
       
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
       
       imenu1_1.addActionListener(new ActionListener(){
           public String str;
           @Override
           public void actionPerformed(ActionEvent e) {
               newWindowint++;
               str = "Application"+newWindowint;
               JFrame newWindow = new JFrame(str);
               newWindow.setSize(400, 300);
               newWindow.setDefaultCloseOperation(2);
               newWindow.setVisible(true);
               newWindow.addWindowListener(new WindowAdapter() {
                   @Override
                   public void windowClosed(WindowEvent e) {
                       newWindowint--; // ลดตัวนับเมื่อปิดหน้าต่าง
                   }
               });
           }
       });
       
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
