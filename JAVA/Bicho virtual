public class BichoVirtual {

    private String nome;
    private int fome;
    private int saude;
    private int idade;

    public BichoVirtual(String nome, int idade, int fome, int saude) {
        this.fome = fome;
        this.idade = idade;
        this.nome = nome;
        this.saude = saude;
       
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getFome() {
        return fome;
    }
    public void setFome(int fome) {
        this.fome = fome;
    }
    public int getSaude() {
        return saude;
    }
    public void setSaude(int saude) {
        this.saude = saude;
    }
    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }

    public float humor() {
        return getFome() * getSaude();
    }
    
    public static void main(String[] args) {
        BichoVirtual tama = new BichoVirtual("joão", 5,5,5);
        System.out.println(tama.humor());
    }
}
