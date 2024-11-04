package atividadesGeneration.modulo_11;

import java.util.Scanner;
import java.util.Stack;

public class Exercicio02 {
	public static void main(String[] args) {

		Scanner leitor = new Scanner(System.in);

		Stack<String> pilha = new Stack<String>();
		int escolha = 0;
		do {
			System.out.println("\nMenu:");
			System.out.println("\n1 - Adicionar Livro na pilha");
			System.out.println("2 - Listar todos os Livros");
			System.out.println("3 - Retirar cliente da pilha");
			System.out.println("0 - Sair");
			System.out.print("\nEntre com a opção desejada: ");
			escolha = leitor.nextInt();
			leitor.nextLine();

			switch (escolha) {

			case 1:

				System.out.println("\n1 - Digite o nome do Livro: ");
				String nomeLivro = leitor.nextLine();
				pilha.add(nomeLivro);
				System.out.println("O livro " + nomeLivro + " foi adicionado na pilha.");
				break;

			case 2:
				if (pilha.isEmpty()) {
					System.out.println("\nA pilha está vazia!");
				} else {
					System.out.println("\nLivros na pilha: ");
					for (String livro : pilha) {
						System.out.println(livro);
					}
				}
				break;

			case 3:
				if (pilha.isEmpty()) {
					System.out.println("\nA fila está vazia!");
				} else {
					String livroRetirado = pilha.pop();
					System.out.println("Um livro foi retirado da pilha!");

				}
				break;

			case 0:
				System.out.println("Programa finalizado!");
				break;

			default:
				System.out.println("Opção inválida. Tente novamente.");
				break;
			}
		} while (escolha != 0);

		leitor.close();
	}
}
