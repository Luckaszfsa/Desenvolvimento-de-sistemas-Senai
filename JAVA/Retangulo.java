
import java.util.Scanner;


public class Retangulo {

    private double base;
    private double altura;

    public Retangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    public double getBase() {
        return base;
    }

    public void setBase(double base) {
        this.base = base;
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public double calcularArea() {
        return altura * base;
    }

    public double calcularPerimetro() {
        return (base + altura) * 2;
    }

    public static void main(String[] args) {
        Retangulo ret = new Retangulo(5.7, 8.9);
        ret.calcularArea();
        ret.calcularPerimetro();
        System.out.println(String.format("%.2f", ret.calcularArea()));
        System.out.println(String.format("%.2f", ret.calcularPerimetro()));
        Scanner scan = new Scanner(System.in);
        double resultado = scan.nextDouble();
        System.out.println(resultado);
    }
}
