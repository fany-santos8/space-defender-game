package atividadesGeneration.modulo_10;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Exercicio01 {

	public static void main(String[] args) {
		ArrayList<String> cores = new ArrayList<String>();

		Scanner leitor = new Scanner(System.in);

		for (int i = 0; i < 5; i++) {
			System.out.println("Escreva as 5 cores: ");
			cores.add(leitor.nextLine());
		}

		System.out.println("\nCores cadastradas: " + cores);

		Collections.sort(cores);
		System.out.println("Cores cadastradas em ordem crescente: " + cores);
		leitor.close();

	}

}
