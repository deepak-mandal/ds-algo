import { Component, OnInit } from '@angular/core';
import { Movie } from '../model/movie';
import { MovieServiceService } from '../movie-service.service';

@Component({
  selector: 'app-movie-read',
  templateUrl: './movie-read.component.html',
  styleUrls: ['./movie-read.component.css']
})
export class MovieReadComponent implements OnInit {

  //for two way data binding
  movieObj={
    id:0,
    name:"",
    language:"",
    rating:""
  }

  isEdit:boolean=false;

  movieData:Movie[]=[];

  constructor(private movieService:MovieServiceService) { }
  
  //for Read operation
  ngOnInit(): void {
    this.movieService.getMovieInfo().subscribe(moviesDataFromService => this.movieData=moviesDataFromService);
  }

  //for Create operation
  addMovie(formObj:Movie){
    console.log(formObj);
    this.movieService.createMovie(formObj).subscribe((response) => {
      alert("Movie details added successfully!");
      window.location.reload();
    })
  }

  //for Update operation
  editMovie(movie:Movie){
    this.isEdit=true
    this.movieObj=movie
  }

  updateMovie(movie:Movie){
    this.isEdit=!this.isEdit;
    this.movieService.updateMovie(this.movieObj).subscribe(() =>{
      this.movieData
    })
    alert("Movie details updated successfully!");
    window.location.reload();
  }

  //for delete operation
  deleteMovie(movie:Movie){
    this.movieService.deleteMovie(movie).subscribe(()=>{this.movieData})
    alert("Movie details deleted successfully!");
    window.location.reload();
  }



}
