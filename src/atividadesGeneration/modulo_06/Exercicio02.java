package atividadesGeneration.modulo_06;

import java.util.Scanner;

public class Exercicio02 {

	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);

		System.out.print("Digite a primeira nota: ");
		float nota1 = leitor.nextFloat();

		System.out.print("Digite a segunda nota: ");
		float nota2 = leitor.nextFloat();

		System.out.print("Digite a terceira nota: ");
		float nota3 = leitor.nextFloat();

		System.out.print("Digite a quarta nota: ");
		float nota4 = leitor.nextFloat();

		float media = (nota1 + nota2 + nota3 + nota4) / 4;

		System.out.println("Média:" + media);
		leitor.close();

	}

}
