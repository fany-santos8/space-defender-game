package atividadesGeneration.modulo_07.if_else;

import java.util.Scanner;

public class Exercicio01 {

	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);

		System.out.print("Digite o primeiro valor: ");
		float valorA = leitor.nextFloat();

		System.out.print("Digite o segundo valor: ");
		float valorB = leitor.nextFloat();

		System.out.print("Digite o terceiro valor: ");
		float valorC = leitor.nextFloat();

		float soma = (valorA + valorB);

		if (soma > valorC) {
			System.out.println(" A Soma de A + B é Maior do que C!");
		} else if (soma < valorC) {
			System.out.println("A Soma de A + B é Menor do que C!");
		} else {
			System.out.println("A Soma de A + B é Igual a C!");
		}

		leitor.close();

	}

}
