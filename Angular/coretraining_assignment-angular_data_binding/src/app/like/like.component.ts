import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-like',
  templateUrl: './like.component.html',
  styleUrls: ['./like.component.css']
})
export class LikeComponent implements OnInit {

  countOfLike:number=0;
  constructor() { }

  ngOnInit(): void {
  }

  //function to count up for like
  likeButtonCount(){
    this.countOfLike++;
  }
   //function to count down for dislike
  disLikeButtonCount(){
    if(this.countOfLike>0){
      this.countOfLike--;
    }
  }

}
