package atividadesGeneration.modulo_11;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Exercicio01 {
	public static void main(String[] args) {

		Scanner leitor = new Scanner(System.in);

		Queue<String> fila = new LinkedList<String>();
		int escolha = 0;
		do {
			System.out.println("\nMenu:");
			System.out.println("\n1 - Adicionar Cliente na fila");
			System.out.println("2 - Listar todos os Clientes");
			System.out.println("3 - Retirar cliente da fila");
			System.out.println("0 - Sair");
			System.out.print("\nEntre com a opção desejada: ");
			escolha = leitor.nextInt();
			leitor.nextLine();

			switch (escolha) {

			case 1:

				System.out.println("\n1 - Digite o nome do Cliente: ");
				String nomeCliente = leitor.nextLine();
				fila.add(nomeCliente);
				System.out.println("O cliente " + nomeCliente + " foi adicionado na fila.");
				break;

			case 2:
				if (fila.isEmpty()) {
					System.out.println("\nA fila está vazia!");
				} else {
					System.out.println("\nA Clientes na fila: ");
					for (String cliente : fila) {
						System.out.println(cliente);
					}
				}
				break;

			case 3:
				if (fila.isEmpty()) {
					System.out.println("\nA fila está vazia!");
				} else {
					String clienteAtendido = fila.poll();
					System.out.println("Chamando o cliente: " + clienteAtendido);

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
