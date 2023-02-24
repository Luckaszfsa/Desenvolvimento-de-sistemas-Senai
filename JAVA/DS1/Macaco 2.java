
import java.util.Arrays;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author ALUNO
 */
public class Macaco {

    private String nome;
    private String[] estomago;

    public Macaco(String nome) {
        this.nome = nome;
        estomago = new String[5];
    }

    public void comer(String comida) {
        boolean cheio = true;
        for (int i = 0; i < estomago.length; i++) {
            if (estomago[i] == null) {
                estomago[i] = comida;
                cheio = false;
                break;
            }
        }
        if (cheio) {
            System.out.println("Estomago cheio");
        }
    }

    public void verEstomago() {
        System.out.println(Arrays.toString(estomago));
    }

    public void digerir() {
        boolean vazio = true;
        for(int i=0;i < estomago.length; i++) {
            if(estomago[i] != null) {
                estomago[i] = null;
                vazio = false;
                break;
            }
        }
        
        if(vazio) {
            System.out.println("O estomago já está vazio");
        }
        for(int i=0; i < estomago.length;i++){
            if(i+1 < 5){
        estomago[i] = estomago[i+1];
        estomago[i+1] = null;
    }
    }
    }   
    public static void main(String[] args) {
        Macaco cezar = new Macaco("Cezar");
        cezar.comer("Banana");
        cezar.verEstomago();
        cezar.digerir();
        cezar.verEstomago();
        cezar.digerir();
       
    }

}
