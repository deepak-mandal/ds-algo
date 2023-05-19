import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { MovieReadComponent } from './movie-read/movie-read.component';
import { MovieServiceService } from './movie-service.service';
import {HttpClientModule} from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    MovieReadComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,    //To connect the JSON-server with angular server
    FormsModule     //Since we had added form in movies-create component
  ],
  providers: [MovieServiceService],   //To registered our service
  bootstrap: [AppComponent]
})
export class AppModule { }
