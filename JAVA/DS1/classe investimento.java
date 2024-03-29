public class contaInvestimento {

    private int agencia;
    private String nome;
    private double saldo;
    private double taxaJuros;

    public contaInvestimento(int agencia, String nome, double saldo,double taxaJuros) {
        this.agencia = agencia;
        this.nome = nome;
        this.saldo = saldo;
        this.taxaJuros = taxaJuros;
    }

    public int getAgencia() {
        return agencia;
    }
    public String getNome() {
        return nome;
    }
    public double getSaldo() {
        return saldo;
    }
    public void setAgencia(int agencia) {
        this.agencia = agencia;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public double getTaxaJuros() {
        return taxaJuros;
    }
    public void setTaxaJuros(double taxaJuros) {
        this.taxaJuros = taxaJuros;
    }

    public void calcularJuros(){
        this.saldo += (this.saldo * this.taxaJuros/100);
    }
    
    public static void main(String[] args) {
        contaInvestimento minhaConta = new contaInvestimento(1678, "Pedro", 1000,10);
        System.out.println(minhaConta.saldo);
        minhaConta.calcularJuros();
        minhaConta.calcularJuros();
        minhaConta.calcularJuros();
        minhaConta.calcularJuros();
        minhaConta.calcularJuros();
        System.out.println(minhaConta.saldo);

    }
    


}
