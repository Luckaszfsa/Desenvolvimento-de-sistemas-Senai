/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Produto;

/**
 *
 * @author User
 */
public class ProdutoImportado extends Produto{
    private Double impostoAlfandega;

    public ProdutoImportado(String nome, Double preco,Double impostoAlfandega) {
        super(nome, preco);
        this.impostoAlfandega = impostoAlfandega;
    }

    

    public Double getImpostoAlfandega() {
        return impostoAlfandega;
    }

    public void setImpostoAlfandega(Double impostoAlfandega) {
        this.impostoAlfandega = impostoAlfandega;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Double getPreco() {
        return preco;
    }

    public void setPreco(Double preco) {
        this.preco = preco;
    }
    
    @Override
    public String precoTag(){
       return ("O produto é:"+ nome+"\nPreço: " + preco + "\nImposto alfandega: " + impostoAlfandega
               + "\nPreço final: " + precoFinal());
            }
    
    public Double precoFinal(){
        return preco += preco* impostoAlfandega/100; 
    }
}
