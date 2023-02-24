/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Produto;

/**
 *
 * @author User
 */
import Produto.Produto;
import Produto.ProdutoImportado;
import Produto.ProdutoUsado;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Programa {

    public static void main(String[] args) throws ParseException {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        List<Produto> list = new ArrayList<>();

        System.out.print("Digite o número de produtos: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            System.out.println("Produto #" + i + " dados:");
            System.out.print("Produto comum, usado ou importado (c/u/i) ? ");
            char p = sc.next().charAt(0);
            System.out.print("Digite o nome do produto: ");
            sc.nextLine();
            String nome = sc.nextLine();
            System.out.print("Digite o preço do produto: ");
            double preco = sc.nextDouble();
            if (p == 'c') {

                list.add(new Produto(nome, preco));
            } else if (p == 'u') {
                System.out.print("Digite a data de fabricação (DD/MM/YYYY): ");
                Date dataFabricacao = sdf.parse(sc.next());
                list.add(new ProdutoUsado(nome, preco, dataFabricacao));
            } else {
                System.out.print("Imposto da alfandêga: ");
                double impostoAlfandega = sc.nextDouble();
                list.add(new ProdutoImportado(nome, preco, impostoAlfandega));
            }

        }
        System.out.println();
        System.out.println("Etiquetas de preço: ");
        for (Produto prod : list) {
            System.out.println(prod.precoTag());
            System.out.println();;
        }

        sc.close();

    }
}
