import java.util.Arrays;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author ALUNO
 */
public class Agenda {
    private Pessoa[] pessoas;

    public Agenda(){
        pessoas = new Pessoa[10];
    }
    
    public void armazenaPessoa(String nome, int idade, float altura) {
        Pessoa fulano = new Pessoa(nome, idade, altura);
        boolean cheio = true;
        for(int i=0; i<pessoas.length;i++){
            if(pessoas[i] == null){
                pessoas[i] = fulano;
                cheio = false;
                break;
            }
        }if(cheio) {
            System.out.println("Agenda cheia");
        }
    }
    
    public void removePessoa(String nome){
        boolean achei =false;
        for(int i=0; i< pessoas.length;i++){
            if(pessoas[i].getNome().equals(nome)){
                pessoas[i] = null;
                achei = true;
            }
        }if(!achei){
            System.out.println("Pessoa não encontrada");
        }
    }
    
    public int buscaPessoa(String nome){
   boolean achei =false;
        for(int i=0; i< pessoas.length;i++){
            if(pessoas[i].getNome().equals(nome)){
                return i;
            }
        }return 11;
        }
    public void imprimeAgenda() {
        System.out.println(Arrays.toString(pessoas));
        
    }
    
    public void imprimePessoa(int index){
    boolean achei =false;
        for(int i=0; i< pessoas.length;i++){
            if(i == index){
                System.out.println(pessoas[i].toString());
                achei = true;
                }
        }if(!achei){
            System.out.println("Pessoa não encontrada");
        }
    }
    
    public static void main(String[] args) {
        Agenda a = new Agenda();
        for(int i=0;i<10;i++){
            a.armazenaPessoa("John", 26, (float) 1.90);
            a.armazenaPessoa("pepe", 26, (float) 1.90);
            a.armazenaPessoa("nenem", 26, (float) 1.90);
            a.armazenaPessoa("Vidal", 26, (float) 1.90);
            a.armazenaPessoa("Alex", 26, (float) 1.90);
            a.armazenaPessoa("Celta", 26, (float) 1.90);
            a.armazenaPessoa("Joao", 26, (float) 1.90);
            a.armazenaPessoa("Vic", 26, (float) 1.90);
            a.armazenaPessoa("Pedro", 26, (float) 1.90);
            a.armazenaPessoa("Roger", 26, (float) 1.90);
            System.out.println(a.buscaPessoa("John"));
            a.removePessoa("Celta");
            a.imprimeAgenda();
            a.imprimePessoa(7);
            
        }
    }
    }
