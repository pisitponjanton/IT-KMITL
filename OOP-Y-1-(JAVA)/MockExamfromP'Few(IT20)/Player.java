public class Player {
    private final String name;
    private final int attackDamage = 2;
    private Houses houses;
    private int hp = 20;
    private int mana = 50;
    public Player(){
        this.name = "";
    }
    public Player(String name){
        this.name = name;
    }
    public Player(String name,int hp){
        this.name = name;
        setHP(hp);
    }
    public String getName(){
        return this.name;
    }
    public int getHP(){
        return this.hp;
    }
    public void setHP(int hp){
        if(hp <= 0){
            this.hp = 0;
        }
        else if(hp >= 20){
            this.hp = 20;
        }
        else{
            this.hp = hp;
        }
    }
    public int getAttackDamage(){
        return this.attackDamage;
    }
    public int getMana(){
        return this.mana;
    }
    public void setMana(int mana){
        if(mana <= 0){
            this.mana = 0;
        }
        else if(mana >= 50){
            this.mana = 50;
        }
        else{
            this.mana = mana;
        }
    }
    public Houses getHouses(){
        return this.houses;
    }
    public void setHouses(Houses houses){
        this.houses = houses;
    }
    @Override
    public String toString(){
        return "[Player] : "+this.name+" HP: "+this.hp+" Mana: "+this.mana+" || "+this.houses;
    }
    public boolean equals(Player player){
        return player.name.equals(this.name) && player.houses.equals(this.houses);
    }
    public void attack(Player target,Spell spell){
        getHouses().attackSpell(this, target, spell);
        if(target.getHP() == 0){
            System.out.println("[DEAD]: "+target.getName()+" was killed  by "+this.name);
        }
    }
    public void protectFromPlayer(Player target){
        getHouses().defense(this,target);
    }
}
