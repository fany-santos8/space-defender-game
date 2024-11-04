package atividadesGeneration.modulo_09;

import java.util.Arrays;
import java.util.Scanner;

public class Exercicio01 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int numero;

		int vetorInt[] = { 2, 5, 1, 3, 4, 9, 7, 8, 10, 6 };

		System.out.println("Escolha um número:");
		numero = scanner.nextInt();

		// Busca o número no vetor usando Arrays.binarySearch()
		int indice = Arrays.binarySearch(vetorInt, numero);

		boolean encontrado = false;

		for (indice = 0; indice < vetorInt.length; indice++) {
			if (vetorInt[indice] == numero) {
				System.out.println("O número " + numero + " está localizado na posição: " + indice);
				encontrado = true;
				break;
			}
		}
		if (!encontrado) {
			System.out.println("O número " + numero + " não foi encontrado! ");

		}
		scanner.close();

	}

}
