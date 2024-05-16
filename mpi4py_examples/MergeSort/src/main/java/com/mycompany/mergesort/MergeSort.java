/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.mergesort;

/**
 *
 * @author MarcoM
 */
import java.util.Arrays;
import java.util.concurrent.RecursiveTask;

public class MergeSort extends RecursiveTask<int[]> {
    private final int[] array;

    public MergeSort(int[] array) {
        this.array = array;
    }

    @Override
    protected int[] compute() {
        if (array.length <= 1) {
            return array;
        }

        // Dividir el array en dos mitades
        int midpoint = array.length / 2;
        int[] leftArray = Arrays.copyOfRange(array, 0, midpoint);
        int[] rightArray = Arrays.copyOfRange(array, midpoint, array.length);

        // Crear dos tareas para ordenar cada mitad
        MergeSort leftTask = new MergeSort(leftArray);
        MergeSort rightTask = new MergeSort(rightArray);

        // Ejecutar las tareas en paralelo utilizando Fork/Join
        leftTask.fork();
        rightTask.fork();

        // Esperar y obtener los resultados de las tareas
        int[] leftResult = leftTask.join();
        int[] rightResult = rightTask.join();

        // Combinar las mitades ordenadas
        return merge(leftResult, rightResult);
    }

    private int[] merge(int[] left, int[] right) {
        int[] result = new int[left.length + right.length];
        int leftPointer, rightPointer, resultPointer;
        leftPointer = rightPointer = resultPointer = 0;

        // Combinar las dos mitades en una sola lista ordenada
        while (leftPointer < left.length || rightPointer < right.length) {
            if (leftPointer < left.length && (rightPointer >= right.length || left[leftPointer] < right[rightPointer])) {
                result[resultPointer++] = left[leftPointer++];
            } else {
                result[resultPointer++] = right[rightPointer++];
            }
        }

        return result;
    }
}
