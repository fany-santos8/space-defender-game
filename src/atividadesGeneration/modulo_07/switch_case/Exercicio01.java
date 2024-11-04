package atividadesGeneration.modulo_07.switch_case;

import java.util.Scanner;

public class Exercicio01 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
while (true) {
		System.out.println(" ************************ MENU PRINCIPAL ********************** ");
		System.out.println(" **Código do produto -      Produto -           Preço Unitário R$** ");
		System.out.println("\n   1                        Cachorro Quente     10.00 ");
		System.out.println("   2                        X-Salada            15.00 ");
		System.out.println("   3                        X-Bacon             18.00  ");
		System.out.println("   4                        Bauru               12.00 ");
		System.out.println("   5                        Refrigerante        8.00 ");
		System.out.println("   6                        Suco de Laranja     13.00 ");
		System.out.println("0 - Sair");
            
		System.out.print("\nCódigo do produto: ");
		int codigoProduto = scanner.nextInt();
		
		System.out.print("Quantidade: ");
		int quantidade = scanner.nextInt();

		double precoCachorroQuente = 10.00;
		double precoXSalada = 15.00;
		double xBacon = 18.00;
		double bauru = 12.00;
		double refrigerante = 8.00;
		double sucoDeLaranja = 13.00;

		double valorTotal = 0;
		

		if (codigoProduto == 0) {
            System.out.println("Pedido Finalizado!");
            System.out.println("Valor total do pedido: R$ " + valorTotal);
            break;
		}

		String nomeProduto = "";

		switch (codigoProduto) {
		case 1:
			valorTotal = quantidade * precoCachorroQuente;
			nomeProduto = "Cachorro Quente";
			break;
		case 2:
			valorTotal = quantidade * precoXSalada;
			nomeProduto = "X-Salada";
			break;
		case 3:
			valorTotal = quantidade * xBacon;
			nomeProduto = "X-Bacon";
			break;
		case 4:
			valorTotal = quantidade * bauru;
			nomeProduto = "Bauru";
			break;
		case 5:
			valorTotal = quantidade * refrigerante;
			nomeProduto = "Refrigerante";
			break;
		case 6:
			valorTotal = quantidade * sucoDeLaranja;
			nomeProduto = "Suco de Laranja";
			break;

		default:
			System.out.println("Código de produto inválido.");
			return;
		}

		System.out.println("Produto: " + nomeProduto);
		System.out.println("Valor total: R$" + valorTotal);

		} 
		scanner.close();
	}
}
