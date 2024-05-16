/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.mergesort;

/**
 *
 * @author MarcoM
 */
import java.util.Arrays;
import java.util.concurrent.ForkJoinPool;

public class ParallelMergeSort {
    private final ForkJoinPool pool;

    public ParallelMergeSort(int parallelism) {
        pool = new ForkJoinPool(parallelism);
    }

    public int[] sort(int[] array) {
        return pool.invoke(new MergeSort(array));
    }

    public static void main(String[] args) {
        int[] array = { 12, 7, 3, 9, 5, 6, 8, 1 };

        ParallelMergeSort sorter = new ParallelMergeSort(4); // Número de hilos
        int[] sortedArray = sorter.sort(array);

        System.out.println(Arrays.toString(sortedArray));
    }
}

