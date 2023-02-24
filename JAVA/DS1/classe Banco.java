public class Banco {

    private int agencia;
    private String nome;
    private double saldo;

    public Banco(int agencia, String nome, double saldo) {
        this.agencia = agencia;
        this.nome = nome;
        this.saldo = saldo;
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
    
    public static void main(String[] args) {
        Banco meuBanco;
        meuBanco = new Banco(1678, "Pedro", 1000);
        System.out.println("Hello world");
        System.out.println(meuBanco.saldo);
    }
    


}
