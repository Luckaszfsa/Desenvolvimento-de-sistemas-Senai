
import java.util.ArrayList;
import java.util.List;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author ALUNO
 */
public class MacacoPrime {
    private String nome;
    private List<String> estomago;
    
    public MacacoPrime(String nome){
        this.nome = nome;
        estomago = new ArrayList<String>();
    }
    
    public void comer(String comida){
        estomago.add(comida);
    }
    
    public void verEstomago(){
        System.out.println(estomago.toString());
    }
    
    public void digerir() {
        estomago.remove(0);
    }
    
    public static void main(String[] args) {
        MacacoPrime grood = new MacacoPrime("Grood");
        grood.comer("Banana");
        grood.verEstomago();
        grood.digerir();
        grood.verEstomago();
    }
}
