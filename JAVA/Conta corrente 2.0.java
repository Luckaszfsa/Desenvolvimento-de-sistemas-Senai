
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author SENAI
 */
public class ContaCorrente {
    private int nConta;
    private String nome;
    private double saldo;

    public ContaCorrente(int nConta, String nome) {
        this.nConta = nConta;
        this.nome = nome;
        this.saldo = 0;
    }

    public int getnConta() {
        return nConta;
    }

    public String getNome() {
        return nome;
    }

    public double getSaldo() {
        return saldo;
    }
    
    public void depositar(double valor){
        saldo += valor;
    }
    
    public void sacar(double valor){
        if(saldo >= valor){
            saldo -= valor;
        } else {
            System.out.println("Lhe falta money");
        }
    }
    
    public static void main(String[] args) {
        List<ContaCorrente> banco = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        while(true){
            System.out.println("Digite 1 para abrir um conta ou "
                    + "2 para acessar sua conta");
            int resposta = sc.nextInt();
            if(resposta == 1){
                System.out.println("Digite seu nome");
                String nome = sc.nextLine();
                Random r = new Random();
                int min = 100000;
                int max = 999999;
                int nConta = (int)Math.floor(Math.random()*(max-min+1)+min);
                ContaCorrente c1 = new ContaCorrente(nConta, nome);
                System.out.println("Conta criada, seu numero é:" + c1.getnConta());
                banco.add(c1);
            } else if (resposta == 2){
                System.out.println("Digite seu nome:");
                String nome = sc.nextLine();
                System.out.println("Digite o numero da sua conta:");
                int nConta = sc.nextInt();
                for(ContaCorrente c: banco){
                    if(c.getnConta() == nConta && c.getNome().equals(nome)){
                        System.out.println("Digite 1 para depositar e 2 para sacar");
                        resposta = sc.nextInt();
                        if (resposta == 1){
                            System.out.println("Quanto deseja depositar?");
                            double valor = sc.nextDouble();
                            c.depositar(valor);
                        } else if (resposta == 2){
                            System.out.println("Quanto deseja sacar?");
                            double valor = sc.nextDouble();
                            c.sacar(valor);
                        } else {
                            System.out.println("Opção Inválida");
                        }
                    }
                }
                
            } else {
                System.out.println("Opção invalida");
            }
        }
        //Crie um programa que permita criar uma conta ou acessar
        //ao acessar deve permitir depositar ou sacar
     
    }
}
