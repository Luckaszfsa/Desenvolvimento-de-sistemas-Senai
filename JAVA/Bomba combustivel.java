public class BombaCombustivel {
    private float valorLitro;
    private float quantidadeCombustivel;


public BombaCombustivel(String tipoCombustivel, float valorLitro, float quantidadeCombustivel) {
this.valorLitro = valorLitro;
this.quantidadeCombustivel = quantidadeCombustivel;
}

public void alterarValor(float valorLitro) {
    this.valorLitro = valorLitro;
}
public void alterarCombustivel(String tipoCombustivel) {
}
public void alterarQuantidadeCombustivel(float quantidadeCombustivel) {
    this.quantidadeCombustivel = quantidadeCombustivel;
}


public float abastecerPorValor(float valor) {
    float temp = valor/ valorLitro;
    alterarQuantidadeCombustivel(this.quantidadeCombustivel - temp);
    return temp;
}
public float abastecerPorLitro(float quantidade) {
    float temp2 = quantidade * valorLitro;
    alterarQuantidadeCombustivel(this.quantidadeCombustivel-quantidade);
    return temp2;
}



public static void main(String[] args) {
    BombaCombustivel bomba1 = new BombaCombustivel("Gasolina", 5,500);
    System.out.println("R$ " + bomba1.abastecerPorLitro(150));
    System.out.println(bomba1.abastecerPorValor(200) + " L");
    System.out.println(bomba1.quantidadeCombustivel);
    System.out.println(bomba1.valorLitro);
}


}
