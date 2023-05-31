package com.dkm;

import java.util.TreeSet;

public class TreeSetComparable {
    public static void main(String[] args){

        TreeSet<Employee> empList = new TreeSet<Employee>();

        empList.add(new Employee(107, "George", 41));
        empList.add(new Employee(105, "deepa", 45));
        empList.add(new Employee(103, "toim", 66));

        for (Employee empObj: empList){
            System.out.println(empObj);
        }


        




    }
}
