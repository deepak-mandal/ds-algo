import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Movie } from './model/movie';

@Injectable({
  providedIn: 'root'
})
export class MovieServiceService {

  movieData=[];
  url:string="http://localhost:3000/movies";

  //to communicate between two URL
  constructor(private http:HttpClient) { }

  getMovieInfo():Observable<Movie[]>{
    return this.http.get<Movie[]>(this.url);
  }


  //starts

  createMovie(user:any){

    return this.http.post(this.url, user);
  }
  getAllUser(){}
  updateMovie(movie:any){
    return this.http.put(this.url+"/"+movie.id, movie); //two argument one for on which, other for 
  }
  deleteMovie(movie:any){
    return this.http.delete(this.url+"/"+movie.id);
  }
  //ends

}
