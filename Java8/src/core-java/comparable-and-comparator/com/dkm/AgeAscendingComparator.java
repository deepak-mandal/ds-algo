package com.dkm;

import java.util.Comparator;

import com.dkm.Student;

public class AgeAscendingComparator implements Comparator<Student> {

    public int compare(Student emp1Obj1, Student emp1Obj2){
        return emp1Obj1.getAge() - emp1Obj2.getAge();
    }
    
}
