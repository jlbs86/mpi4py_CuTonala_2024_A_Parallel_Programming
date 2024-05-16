/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ascensocolina;
import java.util.*;
/**
 *
 * @author Equipo Marco
 */

/**
 * @start S
 * @goal G
 * @output [S, A, D, E, B, F, G]
 */
public class AscensoColina {
    private static List<Character> result = new ArrayList<>();
    private static boolean found = false;

    private static void ascensoColina(HashMap<Character, List<Character>> graph, HashMap<Character, Double> heuristic, char current, char goal) {
        if (!found) {
            result.add(current);
            if (current == goal) {
                found = true;
                return;
            }

            graph.get(current).sort(Comparator.comparingDouble(heuristic::get));
            for (char neighbour : graph.get(current))
                if (heuristic.get(neighbour) < heuristic.get(current))
                    ascensoColina(graph, heuristic, neighbour, goal);
        }
    }

    public static void main(String[] args) {
        HashMap<Character, List<Character>> graph;
        graph = new HashMap() {{
            put('S', Arrays.asList('A', 'D'));
            put('A', new ArrayList<>());
            put('B', new ArrayList<>());
            put('C', new ArrayList<>());
            put('D', Arrays.asList('A', 'E'));
            put('E', Arrays.asList('B', 'F'));
            put('F', Collections.singletonList('G'));
            put('G', new ArrayList<>());
        }};

        HashMap<Character, Double> heuristic = new HashMap() {{
            put('A', 10.4);
            put('B', 6.7);
            put('C', 7.0);
            put('D', 8.9);
            put('E', 6.9);
            put('F', 3.0);
            put('S', 13.0);
            put('G', 0.0);
        }};

        ascensoColina(graph, heuristic, 'S', 'G');
        System.out.println("Ascenso de Colina: " + result.toString());
    }
}