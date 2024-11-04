package atividadesGeneration.modulo_06;

import java.util.Scanner;

public class Exercicio03 {

	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);

		System.out.print("Digite o Salário Bruto: ");
		float salario = leitor.nextFloat();

		System.out.print("Digite o Adicional Noturno: ");
		float adicionalNoturno = leitor.nextFloat();

		System.out.print("Digite as Horas Extras: ");
		float horasExtras = leitor.nextFloat();

		System.out.print("Digite os Descontos: ");
		float descontos = leitor.nextFloat();

		float salarioLiquido = salario + adicionalNoturno + (horasExtras * 5) - descontos;

		System.out.println("Salário Líquido:" + salarioLiquido);
		leitor.close();

	}

}
