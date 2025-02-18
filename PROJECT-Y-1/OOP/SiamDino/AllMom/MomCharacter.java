package AllMom;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import javax.imageio.ImageIO;
import javax.swing.*;

import Character_component.Move;

public abstract class MomCharacter extends JPanel implements Move {
    private final ArrayList<Image> frames = new ArrayList<>();
    private int currentFrame = 0;
    private int move;
    private final String namePath;

    private float xOffset;
    private float yOffset;
    private float speed;

    private int moveXY;

    public MomCharacter(int width, int height, int x, int y, String namePath) {
        setOpaque(false);
        setSize(width, height);
        setLocation(x,y);
        this.namePath = namePath;
        this.xOffset = x;
        this.yOffset = y;
        this.moveXY = 0;
        this.speed = 2.5f;
        loadFrames();
    }

    protected void setxOffset(float xOffset) {
        this.xOffset = xOffset;
    }

    protected float getxOffset() {
        return this.xOffset;
    }

    protected void setSpeed(int speed) {
        this.speed = speed;
    }

    protected float getSpeed() {
        return this.speed;
    }

    protected void setmoveXY(int b) {
        this.moveXY = b;
    }

    protected int getmoveXY() {
        return this.moveXY;
    }

    @Override
    public void characterMoveR() {
        xOffset += speed;
        setLocation((int) xOffset, (int) this.yOffset);
    }

    @Override
    public void characterMoveL() {
        xOffset -= speed;
        setLocation((int) xOffset, (int) this.yOffset);
    }

    @Override
    public void characterMoveU() {
        yOffset -= speed;
        setLocation((int) xOffset, (int) this.yOffset);
    }

    @Override
    public void characterMoveD() {
        yOffset += speed;
        setLocation((int) xOffset, (int) this.yOffset);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (!frames.isEmpty()) {
            g.drawImage(frames.get(currentFrame), 0, 0, getWidth(), getHeight(), this);
        }
    }

    private void loadFrames() {
        for (int i = 1; i <= 9; i++) {
            try {
                Image img = ImageIO.read(new File("img/Character/" + namePath + "/Character" + i + ".png"));
                frames.add(img);
            } catch (IOException e) {
            }
        }
    }

    protected void startAnimation() {
        Timer timer = new Timer(100, _ -> {
            this.howMove();
            repaint();
        });
        timer.start();
    }

    protected void howMove() {
        if (this.move == 0) {
            currentFrame = (currentFrame == 0) ? 0 : 0;
        } else if (this.move == 1) {
            currentFrame = (currentFrame == 1) ? 2 : 1;
        } else if(this.move == 2){
            currentFrame = (currentFrame == 3) ? 4 : 3;
        }else if(this.move == 3){
            currentFrame = (currentFrame == 5) ? 6 : 5;
        }else{
            currentFrame = (currentFrame == 7) ? 8 : 7;
        }
    }

    @Override
    public void startMove() {
        Timer timer = new Timer(50, _ -> {
            switch (this.moveXY) {
                case 0 -> {
                    this.move = 1;
                    this.characterMoveR();
                }
                case 1 -> {
                    this.move = 2;
                    this.characterMoveL();
                }
                case 2 -> {
                    this.move = 3;
                    this.characterMoveD();
                }
                case 3->{
                    this.move = 0;//4
                    this.characterMoveU();
                }
                default -> {
                    this.move = 0;
                }
            }
            checkBoundary();
        });
        timer.start();
    }


    // เดินรอบจอ เป็นวงกลม //ยังไม่เสร็จ
    private void checkBoundary() {
        int minX = 0;
        int minY = 0;
        int maxX = 1100;
        int maxY = 545;
    
        Point location = getLocation();
        if(location.x >= maxX && this.move == 1){
            this.setmoveXY(3);
        }else if(location.y <= minY && this.move == 0) {
            this.setmoveXY(1);
        }else if(location.x <= minX && this.move == 2){
            this.setmoveXY(2);
        }else if(location.y >= maxY && this.move == 3){
            this.setmoveXY(0);
        }
    }
    
}
