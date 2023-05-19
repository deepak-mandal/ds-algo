import { Component, OnInit } from '@angular/core';
import { Userinfo } from './model/userinfo';
import { RecommendService } from './service/recommend.service';

@Component({
  selector: 'app-recommendation',
  templateUrl: './recommendation.component.html',
  styleUrls: ['./recommendation.component.css']
})
export class RecommendationComponent implements OnInit {

  constructor(private recommendService: RecommendService) { }

  recommendations: Userinfo[] = []

  ngOnInit(): void {
    this.recommendations = this.recommendService.getRecommendations();
  }

}
