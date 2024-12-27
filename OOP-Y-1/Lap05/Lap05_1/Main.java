
package Lap05.Lap05_1;
public class Main {
    public static void main(String[] args) {
        Player p1 = new Player();
        p1.setName("Bank");
        p1.setTeam("Gate OR");
        Player p2 = new Player();
        p2.setName("Khim");
        p2.setTeam("Gate AND");
        if(p1.isSameTeam(p2))
            System.out.println(p1.getName() +" is a same team with "+p2.getName());
        else
            System.out.println(p1.getName() +" is not a same team with "+p2.getName());
    }
}
