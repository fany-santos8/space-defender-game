package atividadesGeneration.modulo_11;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;

public class ExemploFila {
	public static void main(String[] args) {
		Queue<Integer> fila = new LinkedList<Integer>();
		
		for (int i = 0; i <= 10; i++) {
			fila.add(i);
		}
		System.out.println("Elementos da fila: " + fila);
		System.out.println("Elementos removido: " + fila.remove()); //tem parametro
		System.out.println("Elementos da fila: " + fila);
		System.out.println("Adicionar elemento: " +fila.add(1));
		System.out.println("Adicionar elemento: " +fila);
		System.out.println("Exibir o primeiro elemento da fila: " + fila.peek());
		System.out.println("Exibir o tamanho da fila: " + fila.size());
		System.out.println("Checar se o elemento existe na fila: " + fila.contains(4));
		System.out.println("Exibe e retira o 1 elementos da fila(HEAD): " + fila.poll());

		Iterator<Integer> iterator = fila.iterator();
 while(iterator.hasNext()) {
		System.out.println(iterator.next()); // percorre todos elementos de forma enxuta 

 }
 fila.clear();
	System.out.println("A fila está vazia? " + fila.isEmpty());

	}
}