public abstract class Spell {
    private final String name;
    private int damage;
    public Spell(){
        this.name = "";
    }
    public Spell(String name){
        this.name = name;
    }
    public String getName(){
        return this.name;
    }
    public int getDamage(){
        return this.damage;
    }
    public void setDamage(int damage){
        this.damage = damage;
    }
}