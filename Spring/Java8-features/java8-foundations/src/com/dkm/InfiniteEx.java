package com.dkm;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class InfiniteEx {
    public static void main(String[] args){

        List<Integer> randNumbers = Stream.generate(() -> new Random().nextInt(100))
        .limit(10)
        .collect(Collectors.toList());
    System.out.println(randNumbers + " " );

    }
}
