import java.util.Scanner;
public class CircleArea {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double radius = input.nextDouble();
        radius*=radius;
        System.out.println(Math.PI*(radius));
    }
}
