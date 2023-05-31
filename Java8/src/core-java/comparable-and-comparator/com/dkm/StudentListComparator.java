package com.dkm;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

import com.dkm.Student;

public class StudentListComparator {

    public static void main(String[] args){

        List<Student> studList = new ArrayList<Student>();

        Student studObj1 = new Student(101, "deepa", 25);
        Student studObj2 = new Student(102, "kumsr", 45);
        Student studObj3 = new Student(45, "mand", 23);

        studList.add(studObj1);
        studList.add(studObj2);
        studList.add(studObj3);


        Collections.sort(studList, new NameComparator());
        System.out.println(studList);

        Collections.sort(studList, new AgeAscendingComparator());
        System.out.println(studList);

        Collections.sort(studList, new AgeDescendingComparator());
        System.out.println(studList);


        


    }
    
}
