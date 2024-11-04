package atividadesGeneration.modulo_06;

import java.util.Scanner;

public class Exercicio01 {
	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);

		System.out.print("Digite o sálario: ");
		float salario = leitor.nextFloat();

		System.out.print("Digite o abono:");
		float abono = leitor.nextFloat();

		float novoSalario = salario + abono;

		System.out.println("Novo salário:" + novoSalario);
		leitor.close();
	}
}
