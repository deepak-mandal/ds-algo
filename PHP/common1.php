<?php       
    $con=mysqli_connect("localhost", "root", "", "ekart") or die(mysqli_error($con));
    $select_query="select user_id, email, first_name from users";
    $select_query_result=mysqli_query($con, $select_query) or die(mysqli_error($con));
    
    session_start();
?>
