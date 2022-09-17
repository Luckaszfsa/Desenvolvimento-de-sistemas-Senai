package Herança;

/**
 *
 * @author User
 */
public class Administrador extends Empregado {
    private double ajudaDeCusto;

    public Administrador(double ajudaDeCusto, double salarioBase, double imposto, String nome, String endereco) {
        super(salarioBase, imposto, nome, endereco);
        this.ajudaDeCusto = ajudaDeCusto;
    }
    
    
    @Override
    public double calcularSalario(){
        return salarioBase += ajudaDeCusto - (salarioBase *imposto/100);
    }
    
    public static void main(String[] args) {
        Administrador adm = new Administrador(500,1500,10,"João","Cidade nova");
        System.out.println(adm.calcularSalario());
        System.out.println(adm.getNome());
    }
    
}
