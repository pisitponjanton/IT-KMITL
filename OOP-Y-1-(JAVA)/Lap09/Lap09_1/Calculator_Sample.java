package Lap09.Lap09_1;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class Calculator_Sample implements ActionListener {
    private JFrame jf;
    private JPanel jp;
    private JButton[] jb;
    private JTextField jt;
    private int num;
    private String opt;
    private String[] listb = {
        "7","8","9","+",
        "4","5","6","-",
        "1","2","3","x",
        "0","c","=","/",
    };
    public Calculator_Sample(){
        jf = new JFrame("My Calculator");
        jp = new JPanel();
        jb = new JButton[16];
        jt = new JTextField();
        jp.setLayout(new GridLayout(4,4));
        for(int i = 0; i<16;i++){
            jb[i] = new JButton(listb[i]);
            jb[i].addActionListener(this);
            jp.add(jb[i]);
        }
        
        jf.setLayout(new BorderLayout());
        jf.add(jt,BorderLayout.NORTH);
        jf.add(jp);
        jf.pack();
        jf.setDefaultCloseOperation(3);
        jf.setVisible(true);
    }
    public void setNum(int num){
        this.num = num;
    }
    public int getNum(){
        return this.num;
    }
    public void setOpt(String opt){
        this.opt = opt;
    }
    public String getOpt(){
        return this.opt;
    }
    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource().equals(jb[0])){
            jt.setText(jt.getText()+"7");
        }
        else if(e.getSource().equals(jb[1])){
            jt.setText(jt.getText()+"8");
        }
        else if(e.getSource().equals(jb[2])){
            jt.setText(jt.getText()+"9");
        }
        else if(e.getSource().equals(jb[3])){
            this.setNum(Integer.parseInt(jt.getText()));
            this.setOpt("+");
            jt.setText("");
        }
        else if(e.getSource().equals(jb[4])){
            jt.setText(jt.getText()+"4");
        }
        else if(e.getSource().equals(jb[5])){
            jt.setText(jt.getText()+"5");
        }
        else if(e.getSource().equals(jb[6])){
            jt.setText(jt.getText()+"6");
        }
        else if(e.getSource().equals(jb[7])){
            this.setNum(Integer.parseInt(jt.getText()));
            this.setOpt("-");
            jt.setText("");
        }
        else if(e.getSource().equals(jb[8])){
            jt.setText(jt.getText()+"1");
        }
        else if(e.getSource().equals(jb[9])){
            jt.setText(jt.getText()+"2");
        }
        else if(e.getSource().equals(jb[10])){
            jt.setText(jt.getText()+"3");
        }
        else if(e.getSource().equals(jb[11])){
            this.setNum(Integer.parseInt(jt.getText()));
            this.setOpt("x");
            jt.setText("");
        }
        else if(e.getSource().equals(jb[12])){
            jt.setText(jt.getText()+"0");
        }
        else if(e.getSource().equals(jb[13])){
            jt.setText("");
        }
        else if(e.getSource().equals(jb[14])){
            if(this.getOpt().equals("+")){
                jt.setText(String.valueOf(this.getNum() + Integer.parseInt(jt.getText())));
                this.setNum(0);
                this.setOpt("");
            }
            else  if(this.getOpt().equals("-")){
                jt.setText(String.valueOf(this.getNum() - Integer.parseInt(jt.getText())));
                this.setNum(0);
                this.setOpt("");
            }
            else  if(this.getOpt().equals("x")){
                jt.setText(String.valueOf(this.getNum() * Integer.parseInt(jt.getText())));
                this.setNum(0);
                this.setOpt("");
            }
            else  if(this.getOpt().equals("/")){
                jt.setText(String.valueOf( (this.getNum() ) / (Integer.parseInt(jt.getText()) ) ));
                this.setNum(0);
                this.setOpt("");
            }
        }
         else if(e.getSource().equals(jb[15])){
            this.setNum(Integer.parseInt(jt.getText()));
            this.setOpt("/");
            jt.setText("");
        }
    };
}
