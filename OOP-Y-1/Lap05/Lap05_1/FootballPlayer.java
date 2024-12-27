package Lap05.Lap05_1;

public class FootballPlayer extends Player {
    private int playerNumber;
    private String position;
    public void setPlayerNumber(int n){
        this.playerNumber = n;
    }
    public void setPosition(String p){
        this.position = p;
    }
    public int getPlayerNumber(){
        return playerNumber;
    }
    public String getPosition(){
        return position;
    }
    public boolean isSamePosition(FootballPlayer p){
        return this.getTeam().equals(p.getTeam()) && this.position.equals(p.position);
    }
}
