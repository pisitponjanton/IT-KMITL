public class Student {
    public String name;
    public double mScore;
    public double fScore;
    public void showGrade(){
        String grade;
        double s;
        s = (mScore*0.4) + (fScore*0.4) +20;
        if(s>=80)
            grade = "A";
        else if(s>=70 && s<80)
            grade = "B";
        else if(s>=60 && s<70)
            grade = "C";
        else if(s>=50 && s<60)
            grade = "D";
        else
            grade = "F";
        System.out.println("Your grade is "+grade);
    }
}
