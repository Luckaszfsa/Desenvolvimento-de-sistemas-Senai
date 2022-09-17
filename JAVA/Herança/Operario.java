package Herança;

/**
 *
 * @author User
 */
public class Operario extends Empregado {
    private double valorProducao;
    private double comissao;

    public Operario(double valorProducao, double comissao, double salarioBase, double imposto, String nome, String endereco) {
        super(salarioBase, imposto, nome, endereco);
        this.valorProducao = valorProducao;
        this.comissao = comissao;
    }
    
    
    @Override
    public double calcularSalario(){
        return salarioBase += valorProducao * comissao/100;
    }
    
    public static void main(String[] args) {
        Operario oper = new Operario(200, 10, 1500,10,"João","Matinha");
        System.out.println(oper.calcularSalario());
        System.out.println(oper.getNome());
        
    }
    
    
    
}
