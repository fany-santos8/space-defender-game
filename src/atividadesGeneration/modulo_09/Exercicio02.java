package atividadesGeneration.modulo_09;

import java.util.Scanner;

public class Exercicio02 {

	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);

		int vetorInt[] = new int[10];
		int soma = 0;
		double media;
		int quantidadeElementos = vetorInt.length;

		System.out.println("Escreva 10 números inteiros:");
		int numeros = leitor.nextInt();
		// Elementos ímpares
		if (numeros % 2 != 0) {
			System.out.println("Elementos nos índices ímpares: " + numeros);
		}
		// Elementos pares
		if (numeros % 2 == 0) {
			System.out.println("Elementos nos índices pares: " + numeros);
		}
		media = (double) soma / vetorInt.length;
		System.out.println("\n\nSoma: " + soma);
		System.out.printf("Média: %.2f\n", media);
		leitor.close();
	}

}
