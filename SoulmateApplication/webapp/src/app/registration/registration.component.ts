import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
<<<<<<< HEAD
import { User } from '../model/user';
=======
>>>>>>> d7a6b7188563d9b8c122c24bf1c061bd508bea9b
import { RegistrationService } from '../registration.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  //constructor() { }
<<<<<<< HEAD
  E:string="";
  P:string="";
=======
>>>>>>> d7a6b7188563d9b8c122c24bf1c061bd508bea9b

  ngOnInit(): void {
  }


//Implementation for reactive form
regForm = new FormGroup({
  email: new FormControl('', [Validators.required, Validators.minLength(6)]),
  name: new FormControl('', [Validators.required, Validators.minLength(3)]),
  age: new FormControl('', [Validators.required]),
  city: new FormControl('', [Validators.required, Validators.minLength(2)]),
  gender: new FormControl('', [Validators.required, Validators.minLength(1)]),
  password: new FormControl('', [Validators.required, Validators.minLength(6)]),
});

constructor(private regService: RegistrationService, private router: Router) {}

submitForm() {

  console.log(this.regForm.value);
  console.log(this.regForm.status);

  if (this.regForm.invalid) {
    return;
  }

  this.regService
    .login(this.regForm.value)
    .subscribe((response) => {
      console.log(response);
      alert("Registered successfully!");
<<<<<<< HEAD
      //console.log("Registered successfully!");
      this.E=response.email;
      this.P=response.password;
      alert("Please Login with the registered credientials! \n"+this.E+"            "+ this.P);
      

      this.router.navigate(['/login']);
    });



    //for rabbitmq
/*
    var user = { 
      email:this.E, 
      password:this.P 
   };
    

   alert(user.email);
   alert(user.email);
*/
    
    this.regService
    .sendDataToUserService(this.regForm.value)
    .subscribe((result) => {
      console.log(result);
      alert(result.email);
    });

   


=======
      this.router.navigate(['/home']);
    });
>>>>>>> d7a6b7188563d9b8c122c24bf1c061bd508bea9b
}




}
