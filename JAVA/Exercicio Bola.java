public class Bola {

    private String cor;

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public Bola(String cor) {
        this.cor = cor;
    }

    public static void main(String[] args) {
        Bola bola1 = new Bola("laranja");
        bola1.setCor("verde");
        System.out.println(bola1.cor);
    }

}
