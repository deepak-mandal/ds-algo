<?php       
    $con=mysqli_connect("localhost", "root", "", "crsi") or die(mysqli_error($con));
    $select_query="select id, name, title, talk_title, link, img from speakers";
    $select_query_result=mysqli_query($con, $select_query) or die(mysqli_error($con));  
  #  $row=mysqli_fetch_array($select_query_result);
    
    
    
   # $row=mysqli_fetch_array($select_query_result);
    
  
    
   # session_start();
?>