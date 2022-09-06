package Herança;

/**
 *
 * @author User
 */
public class Vendedor extends Empregado{
    private double valorVendas;
    private double comissao;

    public Vendedor(double valorVendas, double comissao, double salarioBase, double imposto, String nome, String endereco) {
        super(salarioBase, imposto, nome, endereco);
        this.valorVendas = valorVendas;
        this.comissao = comissao;
    }
    
    @Override
    public double calcularSalario(){
        return salarioBase += valorVendas * comissao/100 - (salarioBase * imposto/100);
    }
    
    public static void main(String[] args) {
        Vendedor vend = new Vendedor(10000,10,1500,5,"Lucas","Tomba");
        System.out.println(vend.calcularSalario());
        System.out.println(vend.getNome());
    }
}
