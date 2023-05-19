<?php
$con=mysqli_connect("localhost","root", "", "ekart") or die(mysqli_error($con));
session_start();
$first_name=$_GET["first_name"];
$user_id=$_SESSION["user_id"];
$update_name_query="update users set first_name='first_name' where user_id='$user_id'";
$update_name_result=mysqli_query($con, $update_name_query) or die(mysqli_error($con));
echo "Name Updated";


?>
