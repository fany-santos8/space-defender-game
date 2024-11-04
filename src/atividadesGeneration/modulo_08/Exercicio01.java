package atividadesGeneration.modulo_08;

import java.util.Scanner;

public class Exercicio01 {

	public static void main(String[] args) {
		int numero1, numero2, contador;
		boolean encontrouMultiplo = false;
		Scanner leia = new Scanner(System.in);

		System.out.println("Digite o primeiro número: ");
		numero1 = leia.nextInt();
		System.out.println("Digite o segundo número: ");
		numero2 = leia.nextInt();

		if (numero1 >= numero2) {
			System.out.println("Intervalo Inválido!");
			return;

		}
		System.out.println("\nNo intervalo entre " + numero1 + " e " + numero2 + ":");

		for (contador = numero1; contador <= numero2; contador++) {
			if (contador % 3 == 0 && contador % 5 == 0) {
				System.out.println(contador + " é multiplo de 3 e 5 ");
				encontrouMultiplo = true;
			}
		}
		if (!encontrouMultiplo) {
			System.out.println("Nenhum número no intervalo é múltiplo de 3 e 5.");
		}
		leia.close();
	}
}
