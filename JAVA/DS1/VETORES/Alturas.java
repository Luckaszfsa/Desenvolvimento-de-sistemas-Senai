/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package Alturas;

import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author User
 */

/*Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
bem como os nomes dessas pessoas caso houver.*/
public class Alturas {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int n, menorIdade;
        double somaAltura, mediaAltura, percentualMenor;
        
        
        System.out.print("Digite a quantidade de pessoas: ");
        n = sc.nextInt();

        String[] nome = new String[n];
        int[] idade = new int[n];
        double[] altura = new double[n];

        for (int i = 0; i < n; i++) {
            System.out.printf("Dados da %dª pessoa:\n", i + 1);
            System.out.print("Nome: ");
            nome[i] = sc.next();
            System.out.print("Idade: ");
            idade[i] = sc.nextInt();
            System.out.print("Altura: ");
            altura[i] = sc.nextDouble();
        }

        menorIdade = 0;
       somaAltura = 0;
             
        for (int i = 0; i < n; i++) {
            if (idade[i] < 16) {
                menorIdade++;
            } 
            somaAltura += altura[i];
            
        }
        
        mediaAltura = somaAltura / n;
        percentualMenor = ((double)menorIdade / n) * 100;
        
        System.out.printf("\nAltura media = %.2f\n", mediaAltura);
        System.out.printf("Pessoas com menos de 16 anos: %.1f%%\n", percentualMenor);
        
                 
        for (int i = 0; i < n; i++) {
            if (idade[i] < 16) {
                System.out.printf("%s\n", nome[i]);
            }
        }

        sc.close();
    }
}
