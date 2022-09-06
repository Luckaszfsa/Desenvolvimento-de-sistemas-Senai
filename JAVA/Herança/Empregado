package Herança;

/**
 *
 * @author User
 */
public class Empregado extends Pessoa {
    private int codigoSetor;
    protected double salarioBase;
    protected double imposto;

    public Empregado(double salarioBase, double imposto, String nome, String endereco) {
        super(nome, endereco);
        this.salarioBase = salarioBase;
        this.imposto = imposto;
    }

    

    
    public int getCodigoSetor() {
        return codigoSetor;
    }

    public void setCodigoSetor(int codigoSetor) {
        this.codigoSetor = codigoSetor;
    }

    public double getSalarioBase() {
        return salarioBase;
    }

    public void setSalarioBase(double salarioBase) {
        this.salarioBase = salarioBase;
    }

    public double getImposto() {
        return imposto;
    }

    public void setImposto(double imposto) {
        this.imposto = imposto;
    }
    
    public double calcularSalario(){
        return salarioBase -= salarioBase * imposto/100;
    }
    
    public static void main(String[] args) {
        Empregado func1 = new Empregado(1500,10,"Joel", "Queimadinha");
        System.out.println("Seu salário líquido é: " + func1.calcularSalario());
        System.out.println(func1.getNome());
    }
}
