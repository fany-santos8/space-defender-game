package atividadesGeneration.modulo_10;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Exercicio04 {

	public static void main(String[] args) {
		Set<Integer> numeros = new HashSet<>();
		Scanner leitor = new Scanner(System.in);

		numeros.add(2);
		numeros.add(5);
		numeros.add(1);
		numeros.add(3);
		numeros.add(4);
		numeros.add(9);
		numeros.add(7);
		numeros.add(8);
		numeros.add(10);
		numeros.add(6);

		System.out.println("\nDigite um número inteiro para buscar:");
		int buscarNumero = leitor.nextInt();

		if (numeros.contains(buscarNumero)) {
			System.out.println("O número " + buscarNumero + " foi encontrado!");
		} else {
			System.out.println("O número " + buscarNumero + " não foi encontrado! ");
		}
		leitor.close();
	}

}
