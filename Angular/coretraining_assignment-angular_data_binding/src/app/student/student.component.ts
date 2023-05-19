import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { StudentService } from '../student.service';
import { Student } from '../model/student';


@Component({
  selector: 'app-student',
  templateUrl: './student.component.html',
  styleUrls: ['./student.component.css']
})
export class StudentComponent implements OnInit {

  studentData:Student[]=[]
  studentObj={
    "id":1,
            "name":"",
            "Dept":"",
            "location":""
  }
  
  constructor(private studentService:StudentService) { }

  ngOnInit(): void {
    this.studentService.getStudentInfo().subscribe(studentDataFromService => this.studentData=studentDataFromService)
  
  }

  outData:any=[];
  getDetailsByName(studentObj:any){
    console.log(studentObj.name)
    for(let x of this.studentData){
      console.log(x);
      if(x.name==studentObj.name){
        console.log(x.name)
        this.outData.push(x.id)
        this.outData.push(x.name)
        this.outData.push(x.Dept)
        this.outData.push(x.location)
      }
    }
    console.log("out result: "+ this.outData);


  }

  
 
}
