import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  loginUrl="http://localhost:8082/login";


  constructor(private http:HttpClient) { }


  login(data: any):Observable<any>{
    return this.http.post(this.loginUrl, data);
  }



  }


