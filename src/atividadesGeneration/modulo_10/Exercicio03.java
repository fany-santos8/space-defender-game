package atividadesGeneration.modulo_10;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;

public class Exercicio03 {

	public static void main(String[] args) {
		Set<Integer> setNumeros = new HashSet<Integer>();
		Scanner leitor = new Scanner(System.in);

        //Exibir os números com o laço For:
		for (int i = 0; i < 10; i++) {
			System.out.println("Escreva 10 números inteiros: ");
			int numero = leitor.nextInt();
			setNumeros.add(numero); // O número é adicionado ao HashSet
			System.out.println("Números inseridos: " + setNumeros);
		}

        //Exibir os números com Interface Iterator:
		System.out.println("\nNúmeros inseridos - Interface Iterator");

		Iterator<Integer> iNumero = setNumeros.iterator();

		while (iNumero.hasNext()) {
			System.out.println(iNumero.next());
		}
		leitor.close();

	}

}
