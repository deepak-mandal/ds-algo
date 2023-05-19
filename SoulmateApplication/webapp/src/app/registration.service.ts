import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RegistrationService {

  regUrl="http://localhost:8080/api/vi/mvi";

<<<<<<< HEAD
  rebbitmqUrl="http://localhost:8080/register";
=======
>>>>>>> d7a6b7188563d9b8c122c24bf1c061bd508bea9b

  constructor(private http:HttpClient) { }


  login(data: any):Observable<any>{
    return this.http.post(this.regUrl, data);
  }
<<<<<<< HEAD

  
  //for rabbit mq
  sendDataToUserService(data:any):Observable<any>{
    return this.http.post(this.rebbitmqUrl, data);
  }


  
=======
>>>>>>> d7a6b7188563d9b8c122c24bf1c061bd508bea9b
}
