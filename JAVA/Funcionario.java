import java.util.Scanner;

public class Funcionario {
    private String nome;
    private float salario;

    public Funcionario(String nome, float salario){
        this.nome = nome;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }
    public float getSalario() {
        return salario;
    }
    
    public void aumentarSalario(float aumento) {
        this.salario += this.salario * (aumento)/100;

    }
    public static void main(String[] args) {
            Scanner input = new Scanner(System.in);
            float aumento;
            Funcionario func1 = new Funcionario("Pedro", 1500);
            System.out.println(func1.nome);
            System.out.println(func1.salario);  
            System.out.println("Insira o percentual de aumento: ");
            aumento = input.nextFloat();   
            func1.aumentarSalario(aumento);
            System.out.println(func1.getSalario());
            input.close();
        }        
}
