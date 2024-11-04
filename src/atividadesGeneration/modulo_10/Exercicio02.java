package atividadesGeneration.modulo_10;

import java.util.ArrayList;
import java.util.Scanner;

public class Exercicio02 {

	public static void main(String[] args) {
		ArrayList<Integer> numeros = new ArrayList<Integer>(); // Cria uma coleção
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

		System.out.println("Digite um número inteiro:");
		int buscarNumero = leitor.nextInt();

		if (numeros.contains(buscarNumero)) {
			System.out.println("O número " + "está localizado na posição: " + numeros.indexOf(buscarNumero));
		} else {
			System.out.println("O número " + buscarNumero + " não foi encontrado na lista! ");
		}
		leitor.close();

	}

}
