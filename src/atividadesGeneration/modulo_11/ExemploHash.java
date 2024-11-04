package atividadesGeneration.modulo_11;

import java.util.HashMap;

public class ExemploHash {
	public static void main(String[] args) {

		HashMap<Integer, String> produtos = new HashMap<Integer, String>();

		produtos.put(1, "Shampoo");
		produtos.put(40, "Biscoito");
		produtos.put(6, "Macarrão");

		System.out.println(produtos);

		System.out.println(produtos.get(1)); // Mostra o elemento que está relacionado ao valor
		System.out.println(produtos.remove(1)); // Remove o elemento relacionado ao valor e mostra o elemento que foi
												// removido
		System.out.println(produtos.size()); // tamanho da hash

		for (Integer key : produtos.keySet()) {
			System.out.println("Chave " + key + " valor: " + produtos.get(key)); // retorna a chave e o elemento
																					// assosciado a chave
		}
		for (String value : produtos.values()) {
			System.out.println("Valor: " + value); // exibe o nome do elemento
		}
	}
}