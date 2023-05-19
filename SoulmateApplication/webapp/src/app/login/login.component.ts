import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
 
  ngOnInit(): void {
  }

//Implementation for reactive form
  form = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.minLength(6)]),
    password: new FormControl('', [Validators.required, Validators.minLength(6)]),
  });

  constructor(private authService: AuthService, private router: Router) {}

  submitForm() {

    console.log(this.form.value);
    console.log(this.form.status);

    if (this.form.invalid) {
      return;
    }

    this.authService
      .login(this.form.value)
      .subscribe((response) => {
        console.log(response);
        this.router.navigate(['/home']);
      });
  }



}
