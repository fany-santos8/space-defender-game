package atividadesGeneration.modulo_07.switch_case;

import java.util.Scanner;

public class Exercicio02 {

	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);

		// Entrada de dados
		System.out.print("Nome do colaborador: ");
		String nomeColaborador = leitor.nextLine();

		System.out.print("Código do Cargo (1 a 6): ");
		int codigoCargo = leitor.nextInt();

		System.out.print("Salário: R$ ");
		float salario = leitor.nextFloat();

		// Variáveis para armazenar o cargo e o percentual de reajuste
		String cargo = "";
		float percentualReajuste = 0;

		// Definindo o cargo e o percentual de reajuste baseado no código do cargo
		switch (codigoCargo) {
		case 1:
			cargo = "Gerente";
			percentualReajuste = 0.10f;
			break;
		case 2:
			cargo = "Vendedor";
			percentualReajuste = 0.07f;
			break;
		case 3:
			cargo = "Supervisor";
			percentualReajuste = 0.09f;
			break;
		case 4:
			cargo = "Motorista";
			percentualReajuste = 0.06f;
			break;
		case 5:
			cargo = "Estoquista";
			percentualReajuste = 0.05f;
			break;
		case 6:
			cargo = "Técnico de TI";
			percentualReajuste = 0.08f;
			break;
		default:
			System.out.println("Código do cargo inválido.");
			leitor.close();
			return;
		}

		// Calculando o novo salário
		float novoSalario = salario + (percentualReajuste * salario);

		// Saída dos dados
		System.out.println("\nNome do colaborador: " + nomeColaborador);
		System.out.println("Cargo: " + cargo);
		System.out.printf("Salário: R$ %.2f\n", novoSalario);

		// Fechando o leitor
		leitor.close();

	}

}
