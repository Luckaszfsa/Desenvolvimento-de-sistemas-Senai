import java.util.Scanner;

public class Funcionario1 {
    private String nome;
    private double salarioBruto;
    private double imposto;

    public Funcionario1(String nome, double salarioBruto, double imposto) {
        this.nome = nome;
        this.salarioBruto = salarioBruto;
        this.imposto = imposto;

    }

    public double getSalarioBruto() {
        return salarioBruto;
    }
    public double salarioLiquido() {
        double salarioLiquido = salarioBruto-(salarioBruto*imposto/100);
        return salarioLiquido;
    }
    public void aumentoSalario(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Insira o percentual de aumento: ");
        double aumento = sc.nextInt();
        double novoSalario = (salarioBruto * (aumento/100)) + salarioBruto;
        sc.close();
    }
    public static void main(String[] args) {
        Funcionario1 func1 = new Funcionario1("John", 1500, 10);
        System.out.println(func1.imposto);
        System.out.println(func1.salarioLiquido());
        func1.aumentoSalario();
        System.out.println(func1.salarioLiquido());
        
    }
}
