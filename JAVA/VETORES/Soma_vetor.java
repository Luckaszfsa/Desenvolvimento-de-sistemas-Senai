/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package Vetores;

import java.util.Scanner;

/**
 *
 * @author User
 */

/*Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
- Imprimir todos os elementos do vetor
- Mostrar na tela a soma e a média dos elementos do vetor*/

public class Vetores {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite quantos números deseja colocar no vetor: ");
        int n = sc.nextInt();
        
        int[] vetor = new int[n];
        
        
        for (int i=0; i<n; i++) {
            System.out.print("Digite um número: ");
            vetor[i] = sc.nextInt();     
        }
        
        int soma = 0;
        for (int i=0; i<n; i++) {
            soma += vetor[i];
        }
        
        int media = soma/n;
        
        
        System.out.println("Elementos do vetor: ");
        for (int i=0; i<n; i++) {
        System.out.printf("%s\n",vetor[i]);
        }
        
        System.out.print("Soma dos elementos do vetor: ");
        System.out.printf("%s", soma);
        
        System.out.print("\nMédia dos elementos do vetor: ");
        System.out.printf("%s", media);
        
        sc.close();
    }
}
