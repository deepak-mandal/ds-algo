<?php
require "common.php";

?>
<!DOCTYPE html>
<!--
Final Project on E-Store website where database as ekart;
Friday 01 May 2020 09:06:53 PM IST 
-->
<html>
    <head>
        <title>E-Store</title>
        <!--latest compiled and minified CSS-->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <!--jQuery library-->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!--Latest compiled and minified javascript-->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <meta name="viewport" content=""width=device-width, initial-scale=1">
        <style>
            .top_margin{ 
                margin-top:20px;
            }
        </style>     
    </head>
    <body>
        <?php
            require "header.php";
        ?>
       
		
        <div class="container">
            <?php while($row=mysqli_fetch_array($select_query_result)){?>
            <div class="row">
                <div class="col-lg-12"><h4>User</h4></div>
            </div>
            <div class="row">
                <div class="col-xs-2">ID</div>
                <div class="col-xs-10"><?php echo $row['user_id'];?></div>
            </div>
            <div class="row">
                <div class="col-xs-2">Email</div>
                <div class="col-xs-10"><?php echo $row['email']; ?></div>
            </div>
            <div class="row">
                <div class="col-xs-2">First Name</div>
                <div class="col-xs-10"><?php echo $row['first_name']; ?></div>
            </div>
            <div class="row">
                <div class="col-xs-2">Products</div>
                <div class="col-xs-10"><?php echo number_of_products_purchesed($con, $row['user_id']); ?></div>
                
                
            </div>
            
            
            
            
            <hr/>           
            <?php } ?>
           
               
        </div>
         			
		
	
		
    </body>
</html>
<?php
function number_of_products_purchesed($con, $user_id){
  $users_products_query="select user_id from users_products where user_id=$user_id";
$users_products_result=mysqli_query($con, $users_products_query);
$number_of_products=mysqli_num_rows($users_products_result);
return $number_of_products;
    
}

?>
