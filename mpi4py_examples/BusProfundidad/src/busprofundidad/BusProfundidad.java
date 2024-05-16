/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package busprofundidad;

/**
 *
 * @author Equipo Marco
 */

import java.util.Stack;
 
public class BusProfundidad {
    /**
     * @param args the command line arguments
     */
 
    // Información del nodo de almacenamiento
    private char[] vertices;
 
         // Almacenar información lateral (matriz de adyacencia)
    private  int[][] arcs;  
 
         // El número de nodos en el gráfico
    private int vexnum;
 
         // Registrar si el nodo ha sido atravesado
    private boolean[] visited;
 
         // Inicializar
    public BusProfundidad(int n) {
          vexnum = n;
          vertices = new char[n];
          arcs = new int[n][n];
          visited = new boolean[n];
          for (int i = 0; i < vexnum; i++) {
             for (int j = 0; j < vexnum; j++) {
                 arcs[i][j] = 0;
             }
          }
    }
 
         // Agregar bordes (gráfico no dirigido)
    public void addEdge(int i, int j) {
                     // La cabeza y la cola del borde no pueden ser el mismo nodo
          if (i == j)return;
 
          arcs[i][j] = 1;
          arcs[j][i] = 1;
    }
 
         // establecer el conjunto de nodos
    public void setVertices(char[] vertices) {
        this.vertices = vertices;
    }
 
         // Establecer bandera de acceso al nodo
    public void setVisited(boolean[] visited) {
        this.visited = visited;
    }
 
         // imprimir nodos transversales
    public void visit(int i){
        System.out.print(vertices[i] + " ");
    }
 
         // Travesía en profundidad desde el i-ésimo nodo
    private void traverse(int i){
                 // marca que el i-ésimo nodo ha sido atravesado
        visited[i] = true;
                 // Imprime el nodo actualmente atravesado
        visit(i);
 
                 // Atraviesa la relación de conexión directa del i-ésimo nodo en la matriz de adyacencia
        for(int j=0;j<vexnum;j++){
                         // El nodo de destino está conectado directamente con el nodo actual y el nodo no ha sido visitado, recursivo
            if(arcs[i][j]==1 && visited[j]==false){
                traverse(j);
            }
        }
    }
 
         // Recorrido en profundidad del gráfo (recursivo)
    public void DFSTraverse(){
                 // Inicializar la marca transversal del nodo
        for (int i = 0; i < vexnum; i++) {
            visited[i] = false;
        }
 
                 // Iniciar un recorrido profundo desde nodos que no se han recorrido
        for(int i=0;i<vexnum;i++){
            if(visited[i]==false){
                                 // Si es un grafo conectado, solo se ejecutará una vez
                traverse(i);
            }
        }
    }
 
         // Recorrido en profundidad del gráfo (no recursivo)
    public void DFSTraverse2(){
                 // Inicializar la marca transversal del nodo
        for (int i = 0; i < vexnum; i++) {
            visited[i] = false;
        }
 
        Stack<Integer> s = new Stack<Integer>();
        for(int i=0;i<vexnum;i++){
            if(!visited[i]){
                                 // Nodo inicial del subgrafo conectado
                s.add(i);
                do{ 
                                         // Pop
                    int curr = s.pop();
 
                                         // Si no se ha atravesado el nodo, atravesar el nodo y empujar los nodos secundarios a la pila
                    if(visited[curr]==false){
                                                 // atravesar e imprimir
                        visit(curr);
                        visited[curr] = true;
 
                                                 // Los nodos secundarios no cruzados se insertan en la pila
                        for(int j=vexnum-1; j>=0 ; j-- ){
                            if(arcs[curr][j]==1 && visited[j]==false){
                                s.add(j);
                            }
                        }
                    }
                }while(!s.isEmpty());
            }
        }
    }
 
    public static void main(String[] args) {
          // TODO code application logic here
          
        BusProfundidad g = new BusProfundidad(8);
        char[] vertices = {'S','A','B','C','D','E','F','G'};
        g.setVertices(vertices);
 
        g.addEdge(0, 1);
        g.addEdge(0, 3);
        g.addEdge(1, 0);
        g.addEdge(1, 2);
        g.addEdge(1, 4);
        g.addEdge(2, 1);
        g.addEdge(2, 3);
        g.addEdge(2, 5);
        g.addEdge(5, 2);
        g.addEdge(5, 4);
        g.addEdge(5, 6);
        g.addEdge(6, 5);
        g.addEdge(6, 7);
        g.addEdge(4, 1);
        g.addEdge(4, 5);
        g.addEdge(5, 4);
        g.addEdge(5, 2);
        g.addEdge(5, 6);
        g.addEdge(2, 5);
        g.addEdge(2, 3);
        g.addEdge(6, 5);
        g.addEdge(6, 7);
        /*g.addEdge(4, 0);
        g.addEdge(4, 1);
        g.addEdge(4, 5);
        g.addEdge(5, 4);
        g.addEdge(1, 4);
        g.addEdge(1, 2);
        g.addEdge(2, 1);
        //g.addEdge(2, 4);
        //g.addEdge(2, 5);
        //g.addEdge(5, 2);
        g.addEdge(5, 6);
        g.addEdge(6, 5);
        g.addEdge(6, 7);
        g.addEdge(5, 4);
        g.addEdge(5, 2);
        g.addEdge(5, 6);
        g.addEdge(2, 5);
        g.addEdge(2, 1);
        g.addEdge(2, 3);
        g.addEdge(6, 5);
        g.addEdge(6, 7);*/
 
                 System.out.print ("primer recorrido en profundidad (recursivo):");
        g.DFSTraverse();
 
        System.out.println();
 
                 System.out.print ("Recorrido en profundidad primero con pila (no recursivo):");
        g.DFSTraverse2();
    }
 
}
