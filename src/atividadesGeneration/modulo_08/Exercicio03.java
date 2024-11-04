package atividadesGeneration.modulo_08;

import java.util.Scanner;

public class Exercicio03 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int idade;
		int totalMenores21 = 0;
		int totalMaiores50 = 0;

		while (true) {
			System.out.print("Digite uma idade: ");
			idade = scanner.nextInt();

			if (idade < 0) {
				break;
			}

			if (idade < 21) {
				totalMenores21++;
			} else if (idade > 50) {
				totalMaiores50++;
			}
		}

		System.out.println("\nTotal de pessoas menores de 21 anos: " + totalMenores21);
		System.out.println("Total de pessoas maiores de 50 anos: " + totalMaiores50);

		scanner.close();

	}

}
