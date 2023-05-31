package com.dkm;

import com.dkm.Student;

import java.util.Comparator;


public class NameComparator implements Comparator<Student> {

    public int compare(Student emp1Obj1, Student emp1Obj2){
        return emp1Obj1.getName().compareTo(emp1Obj2.getName());
    }
    
}
