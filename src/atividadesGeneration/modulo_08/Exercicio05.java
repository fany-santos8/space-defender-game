package atividadesGeneration.modulo_08;

import java.util.Scanner;

public class Exercicio05 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int numero;
		int somaPositivos = 0;

		do {
			System.out.print("Digite um número: ");
			numero = scanner.nextInt();

			if (numero > 0) {
				somaPositivos += numero;
			}

		} while (numero != 0);

		System.out.println("\nA soma dos números positivos é: " + somaPositivos);

		scanner.close();

	}

}
