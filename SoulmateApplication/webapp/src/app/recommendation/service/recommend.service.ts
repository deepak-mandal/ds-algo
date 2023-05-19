import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Userinfo } from '../model/userinfo';

@Injectable({
  providedIn: 'root'
})
export class RecommendService {

  constructor(private http: HttpClient) { }

  getRecommendations(user?: Userinfo){
    return [
      {"name":"Ria", "city":"Hyderabad", "gender":"Female", "age":24},
      {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      // {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      // {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      // {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      // {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      // {"name":"May", "city":"Hyderabad", "gender":"Female", "age":42},
      // {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32},
      // {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32},
      // {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32},
      // {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32},
      // {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32},
      // {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32},
      // {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32},
      // {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32},
      {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32},
      {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32},
      {"name":"Alexa", "city":"Bangalore", "gender":"Female", "age":32}
    ]
    // return this.http.post<Userinfo[]>("localhost:8083/recommend", user);
  }

}
