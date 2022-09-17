package Herança;

/**
 *
 * @author User
 */
public class Fornecedor extends Pessoa {
    private double valorCredito;
    private double valorDivida;

    
    public Fornecedor(double valorCredito, double valorDivida, String nome, String endereco, String telefone) {
        super(nome, endereco, telefone);
        this.valorCredito = valorCredito;
        this.valorDivida = valorDivida;
    }

    public double getValorCredito() {
        return valorCredito;
    }

    public void setValorCredito(double valorCredito) {
        this.valorCredito = valorCredito;
    }

    public double getValorDivida() {
        return valorDivida;
    }

    public void setValorDivida(double valorDivida) {
        this.valorDivida = valorDivida;
    }
    
    public double obterSaldo(){
        return valorCredito - valorDivida;
    }
    
    public static void main(String[] args) {
        Pessoa forn = new Fornecedor(1500,1000,"Julio", "Tomba", "41533551");
        Fornecedor forn2 = new Fornecedor(1500,1000,"Pedro", "Feira X", "15151515");
        System.out.println("O seu saldo é: " + forn2.obterSaldo());
        System.out.println(forn2.getNome());
        System.out.println(forn.getNome());
    }
    
}
