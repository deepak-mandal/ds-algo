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
            <center><h4>Front end validation</h4></center>
            <div class="row">
                <div class="col-xs-4 col-xs-offset-4">
                    <div class="panel panel-primary">
                        <div class="panel-heading"><h4>Login</h4></div>
                        <div class="panel-body">
                            <form action="login_script.php" method="POST">
                                <div class="form-group">
                                    <input type="email" class="form-control" placeholder="Email" name="email" required="true" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$">
                                    
                                </div>
                                <div class="form-group">
                                    <input type="password" class="form-control" placeholder="password" name="password" required="true" pattern=".{6,}">
                                    
                                </div>   
                                <button type="submit" name="submit" class="btn btn-primary">Login</button>
                            </form><br>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
         
        
		
    </body>
</html>
