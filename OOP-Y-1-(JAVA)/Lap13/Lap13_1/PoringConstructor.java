/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Lap13.Lap13_1;

import java.awt.event.*;
import javax.swing.*;

/**
 *
 * @author mba135816
 */
public class PoringConstructor implements ActionListener{
    private JFrame jf;
    private JButton jb;
    private int n;
    public PoringConstructor(){
        jf = new JFrame("PoringConstructor");
        jb = new JButton("Add");
        jb.addActionListener(this);
        jf.add(jb);
        jf.setSize(200,100);
        jf.setDefaultCloseOperation(3);
        jf.setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e){
        n+=1;
        Poring poring = new Poring(n);
    }
}
