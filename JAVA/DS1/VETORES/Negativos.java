/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package Negativos;

import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author User
 */

/*Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos.*/

public class Negativos {

    public static void main(String[] args) {
        
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        System.out.println("Quantos números você vai digitar?");
        int n = sc.nextInt();
        
        int[] vetor = new int[n];
        
        for (int i=0; i < n; i++){
            System.out.println("Digite um número: ");
            vetor[i] = sc.nextInt();
        }
        
        System.out.println("Números negativos: ");
        
        for (int i=0; i<n; i++) {
            if (vetor[i] < 0) {
                System.out.printf("%d\n", vetor[i]);
            }
        }
        
        
        
        sc.close();
    }
    
    
}
