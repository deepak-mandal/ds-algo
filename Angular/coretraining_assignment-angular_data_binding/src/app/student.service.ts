import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Student } from './model/student';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class StudentService {
  studentData=[];
  url:string="http://localhost:3000/students";

  constructor(private http:HttpClient) { }

  getStudentInfo(): Observable<Student[]>{
    return this.http.get<Student[]>(this.url);
  }
}
