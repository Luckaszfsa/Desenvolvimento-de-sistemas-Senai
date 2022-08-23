/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author ALUNO
 */
import java.util.Scanner;

public class Controle {
    
    
    private int canal;
    private int volume;

    public Controle(int canal, int volume) {
        this.canal = canal;
        this.volume = volume;
    }

    public int getCanal() {
        return canal;
    }

    public void setCanal(int canal) {
        if (canal >=0 && canal<= 100){
        this.canal = canal;
    }
    }
        

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }
    
    public void aumentarVolume() {
        if (this.volume < 100){
            this.volume+= 1;
        }
    
}
    public void diminuirVolume() {
        if (this.volume >0){
            this.volume -= 1;
    }
    }
    
    public static void main(String[] args) {
        Controle c1 = new Controle(10,15);
        Scanner scan = new Scanner(System.in);
        while(true) {
        
        System.out.println("Digite 1 para alterar o canal ou 2 para alterar o volume");
        int resposta = scan.nextInt();
        if (resposta ==1) {
            System.out.println("Digite o canal para o qual deseja ir");
            int canal = scan.nextInt();
            c1.setCanal(canal);
            System.out.println("Atualmente está no canal " + c1.getCanal());
        } else if (resposta ==2) {
            System.out.println("Digite 1 para aumentar e 2 para diminuir");
            
            resposta = scan.nextInt();
            
            if (resposta==1) {
                c1.aumentarVolume();
                System.out.println("Atualmente está no volume " + c1.getVolume());
            } else if (resposta ==2){
                c1.diminuirVolume();
                System.out.println("Atualmente está no volume " + c1.getVolume());
            } else{
                System.out.println("opção inválida");
            }
        } else {
            System.out.println("Opção inválida");
        }
        
        
      
        
        //criar um objeto do tipo controle
        //Usando print e scanner perguntar ao usuario se ele deseja alterar o canal
        //volume aumentar ou diminuir
        
    }
}}
