package Lab06;
public class SeniorProgrammer extends Programmer {
    @Override
    public void coding(String str){
        if(super.getEnergy()>=10){
            System.out.println("I'm coding about "+str);
        }else{
            System.out.println("ZzZzZz");
        }
        super.setEnergy(super.getEnergy()-5);
        super.setHappiness(super.getHappiness()-5);
    }
    @Override
    public void coding(char str){
        String str_ = String.valueOf(str);
        this.coding(str_);
    }
    public void coding(String str,int num){
        for(int i=0;i<num;i++){
            if(super.getEnergy()>=10){
                System.out.println("I'm coding about "+str);
            }else{
                System.out.println("ZzZzZz");
            }
            super.setEnergy(super.getEnergy()-5);
            super.setHappiness(super.getHappiness()-5);
        }
    }
    public void compliment(Programmer p){
        p.setHappiness(p.getHappiness()+20);
        System.out.println(p.getName()+" in a good mood");
    }
    public void blame(Programmer p){
        p.setHappiness(p.getHappiness()-20);
        System.out.println(p.getName()+" in a bad mood");
    }
}
