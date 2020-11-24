<?php
require "common.php";
?>
<!DOCTYPE html>
<!--
Final Project on E-Store website where database as ekart;
Friday 01 May 2020 09:06:53 PM IST 

It include following files :-
common.php
style.css
header.php
signup.php


-->
<html>
    <head>
        <title>E-Store</title>
        <meta name="viewport" content=""width=device-width, initial-scale=1">
        
        
        <!--latest compiled and minified CSS-->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <!--jQuery library-->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!--Latest compiled and minified javascript-->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="style.css" > <!--must be after bootstrap.min.css link-->
    </head>
    <body>
        
        <?php
            require "header.php";
        ?>
             
        <div class="container column_style">
            <h1>12column</h1>
            <div class="row">
                <div class="col-xs-6 column_style">
                   column11
                </div>
                <div class="col-xs-6 column_style">
                    column12
                </div>
            </div>
        </div>
       
    
        
        
        <div class="container">
            <div class="row row_style">
                <div class="col-xs-6">
                    <div class="panel panel-primary">
                        <div class="panel-heading">
                            <h4>Panel Heading</h4>
                        </div>
                        <div class="panel-body">
                            <p>Basic panel example</p>
                            <button class="btn btn-primary">Demo</button>
                        </div>
                        <div class="panel-footer">Panel Footer</div>
                    </div>
                </div>
            </div>
        </div>
        
        
       
    </body>
</html>
