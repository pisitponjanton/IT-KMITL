public class Fraction {
    public int topN;
    public int btmN;
    public String toFraction(){
        return topN+"/"+btmN;
    };
    public String toFloat(){
        return ((topN+0.0)/btmN)+"";
    };
    public void addFraction(Fraction f){
        if(f.btmN == btmN){
            topN += f.topN;
        }else{
            topN = (topN*f.btmN) + (f.topN*btmN);
            btmN = btmN*f.btmN;
        }
    };
    public boolean myEquals(Fraction x){
        return topN * x.btmN == btmN * x.topN;
    };
    public void LowestTermFrac(){
        int r = btmN/topN;
        topN/=r;
        btmN/=r;
    };
}
