<?php
//Connection established
$con=mysqli_connect("localhost", "root", "", "ekart") or die(mysqli_error($con));
//session_start();
//Store from value into variable
$email=mysqli_real_escape_string($con, $_POST["email"]);
$first_name=mysqli_real_escape_string($con, $_POST["first_name"]);
$last_name=mysqli_real_escape_string($con, $_POST["last_name"]);
$phone=$_POST["phone"];

//Store insert query in a variable. Use double quotes to let PHP treat variables as variables only. 
$user_registration_query="insert into users (email, first_name, last_name, phone) values ('$email', '$first_name','$last_name','$phone')";
//die($user_registration_query);

//execute the query
$user_registration_submit=mysqli_query($con, $user_registration_query) or die(mysqli_error($con));

//if the echo is executed, this mean query successfully executed otherwise, die function with mysqli_query function would have stopped the execution of the code.
echo "User Successfully Inserted";

//for session to be execute
$_SESSION['email']=$email;
$_SESSION['id']=mysqli_insert_id($con);

?>
