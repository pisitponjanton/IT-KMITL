public abstract class Houses {
    private String name;
    private String color;
    public Houses(){
        setName("");
        setColor("");
    }
    public Houses(String name,String color){
        setName(name);
        setColor(color);
    }
    public String getColor(){
        return this.color;
    }
    public String getName(){
        return this.name;
    }
    public void setColor(String color){
        this.color = color;
    }
    public void setName(String name){
        this.name = name;
    }
    @Override
    public String toString(){
        return "[House] : "+this.name+" , Color : "+this.color;
    }
    public abstract void attackSpell(Player player, Player target, Spell spell);
    public abstract void defense(Player player, Player damager);
}
