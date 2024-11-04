package atividadesGeneration.modulo_07.if_else;

import java.util.Scanner;

public class Exercicio02 {

	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);

		System.out.println("Digite um número inteiro: ");
		int numeroInteiro = (int) leitor.nextFloat();

		if (numeroInteiro % 2 == 0 && numeroInteiro > 0) {
			System.out.println(" O Número é par e positivo!");

		} else if (numeroInteiro % 2 != 0 && numeroInteiro < 0) {
			System.out.println("O Número é ímpar e negativo!");

		} else if (numeroInteiro % 2 == 0 && numeroInteiro < 0) {
			System.out.println("O Número é par e negativo!");

		} else {
			System.out.println("O Número é ímpar e positivo!");
			leitor.close();
		}

	}

}
