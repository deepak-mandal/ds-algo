import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import {HttpClientModule} from '@angular/common/http';
import { HomeComponent } from './home/home.component';
import { NavigationComponent } from './navigation/navigation.component';
import { ApiService } from './api.service';
import { RegistrationComponent } from './registration/registration.component';
import { DashboardComponent } from './dashboard/dashboard.component';
<<<<<<< HEAD
import { RecommendationComponent } from './recommendation/recommendation.component';
import { RecommendService } from './recommendation/service/recommend.service';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatCardModule} from '@angular/material/card';
import {MatButtonModule} from '@angular/material/button'; 
=======
>>>>>>> d7a6b7188563d9b8c122c24bf1c061bd508bea9b

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    NavigationComponent,
    RegistrationComponent,
<<<<<<< HEAD
    DashboardComponent,
    RecommendationComponent
=======
    DashboardComponent
>>>>>>> d7a6b7188563d9b8c122c24bf1c061bd508bea9b
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatCardModule,
    MatButtonModule
  ],
  providers: [ApiService, RecommendService],
  bootstrap: [AppComponent]
})
export class AppModule { }
