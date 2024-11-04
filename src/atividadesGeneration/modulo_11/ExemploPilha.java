package atividadesGeneration.modulo_11;

import java.util.Iterator;
import java.util.Stack;

public class ExemploPilha {
	public static void main(String[] args) {

		Stack<String> pilha = new Stack<String>();

		pilha.push("Prato 1");
		pilha.push("Prato 2");
		pilha.push("Prato 3");
		pilha.push("Prato 4");
		pilha.push("Prato 5");

		System.out.println("Elementos da pilha: " + pilha);
		System.out.println("Elemento removido: " + pilha.pop()); // remove o ultimo colocado na pilha no caso o 5
		System.out.println("Elementos da pilha: " + pilha);
		System.out.println("Elemento removido: " + pilha.pop()); // remove o ultimo colocado na pilha no caso o 4
		System.out.println("Elementos da pilha: " + pilha);
		System.out.println("Elemento no topo da pilha: " + pilha.peek());
		System.out.println("Adiciona elementos na pilha: " + pilha.push("Prato 6"));
		System.out.println("Elementos da pilha: " + pilha);
		System.out.println("Tamanho da pilha: " + pilha.size());
		System.out.println("Elemento está na pilha? " + pilha.contains("Prato 4"));

		Iterator<String> iterator = pilha.iterator();
		while (iterator.hasNext()) {
			System.out.println(iterator.next());

		}
		pilha.clear();
		System.out.println("Existe elemento na pilha: " + pilha.isEmpty());

	}
}
