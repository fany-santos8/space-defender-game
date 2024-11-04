package atividadesGeneration.modulo_06;

import java.util.Scanner;

public class Exercicio04 {

	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);

		System.out.print("Digite a primeiro produto: ");
		float n1 = leitor.nextFloat();

		System.out.print("Digite a segundo produto: ");
		float n2 = leitor.nextFloat();

		System.out.print("Digite a terceiro produto: ");
		float n3 = leitor.nextFloat();

		System.out.print("Digite a quarto produto: ");
		float n4 = leitor.nextFloat();

		float calculo = (n1 * n2) - (n3 * n4);

		System.out.println("Diferença:" + calculo);
		leitor.close();

	}

}
