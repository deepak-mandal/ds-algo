<!DOCTYPE html>
<!--
Final Project of Internshala...

Friday 01 May 2020 09:06:53 PM IST 
-->
<html>
	<head>
		<!--latest compiled and minified CSS-->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
		<!--jQuery library-->
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
		<!--Latest compiled and minified javascript-->
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		<title>E-Store</title>
	</head>
	<body>
		<nav class="navbar navbar-default">
			<div class="container">
				<div class="navbar-header">
					<a href="#" class="navbar-brand">E-Store</a>	
				</div>
				<div>
					<ul class="nav navbar-nav navbar-right">
						<li><a href="#">Sign Up</a></li>
						<li><a href="#">Login</a></li>
						<li><a href="#">About Us</a></li>
						<li><a href="#">Contact Us</a></li>
					</ul>
				</div>
			</div>
		</nav>
            
            <div class="container">
                <?php
                // this is single line comment
                echo'<h1> I am the batman!</h1>';
                /*This is multi line comment 
hence it is used to write comment in two or more lines
                */
                
                 echo 18+12;
                 $var1=18.0;
                 $var2=12;
                 echo"<br>";
                 echo gettype($var1);
                 echo '<br>';
                 $sum=$var1+$var2;
                 echo "$sum<br>";
                 $var3='Hello';
                 $var4='Internshala';
                 echo "$var3.$var4<br>";
                 echo "The value of first varible is $var1 and the vallue of second ariable is $var2 <br>";
                 
                 $sum2=sum($var1,$var2);
                 echo"Sum of two variable = $sum2 <br>";
                 $number=array(18,12);
                 $sum1=$number[0]+$number[1];
                 echo "sum of two variable is" .$sum1. "<br>";
                 echo "length of the array = ".sizeof($number);
                 $number3=array("first_number"=>18, "second_number"=>12);
                 $sum3=$number3["first_number"]+$number3["second_number"];
                 echo "Sum of the two variable is $sum3.<br>";
                 print_r($number3);
                 echo"<br>";
                 $number4=array(array(18, 12), array(1, 2));
                 $sum4=$number4[0][0]+$number4[0][1];
                 echo "sum of the two variable is $sum4.<br>";
                 echo 'I am a "string".<br>';
                 $variable1=18;
                 echo 'The value of Variable1 is $variable1. <br>';
                 echo "The value of variable1 is $variable1. <br>";
                 echo "The value of variable1 is '$variable1'.<br>";
                 $string1="I am first string";
                 $length_of_string=strlen($string1);
                 echo "$length_of_string<br>";
                 //if else
                 $marks=50;
                 if($marks>=40)
                 {
                     echo"The student has passed.<br>";
                 }else{
                    echo"The student has failed.<br>";                                        
                 }
                 $marks1=50;
                 if($marks1>=40){
                     echo"The student has just passed.<br>";                     
                 }else if(($marks1>40)&&($marks1<90)){
                     echo"The student has passed.<br>";
                 }else if($marks1>90){
                     echo"The student is in the merit list.<br>";
                 }else{
                     echo"The student has failed";
                 }
                 echo"<br>";
                 $status=false;
                 if($status){
                     echo "The student has passed.<br>";
                 }else{
                     echo"The student has failed.<br>";
                     }
                 
                     
                 $marks2=40.1;    
                 if($marks2>40)
                 {
                     if($marks2==40)
                     {
                         echo"just passed.<br>";
                     }
                     else{
                         echo"passed.<br>";
                     }
                 }
                 else
                 {
                  echo"failed.<br>";
                 }       
                 //while loop
                 $counter=1;
                 while($counter<=5){
                     echo $counter ."<br>";
                     $counter++;
                 }
                 for($counter=1; $counter<=5; $counter++){
                     echo$counter;
                 }
                 echo"<br>";
                 $mark=array(4,8,15,16,23,42);
                 foreach($mark as $mark){
                     echo$mark." ";
                                      }
                                      echo"<br>";
                 
                                      
                $mark3=array("first_number"=>4, "second_number"=>8);
                foreach($mark3 as $mark3_index=>$mark3_value){
                    echo"The index is $mark3_index, the value is $mark3_value.<br>";
                }echo"<br>";
                 
                $con=mysqli_connect("localhost", "root", "", "ekart") or die(mysqli_error($con));
                $select_query="select user_id, email, first_name from users";
                $select_query_result=mysqli_query($con, $select_query) or die(mysqli_error($con));
                $total_rows_fetched=mysqli_num_rows($select_query_result);
                echo "$total_rows_fetched <br><br>";
                //
                $row=mysqli_fetch_array($select_query_result);
                echo $row['user_id']."    ";
                echo $row['email']."    ";
                echo $row['first_name']."<br>";
                
                $row=mysqli_fetch_array($select_query_result);
                echo $row['user_id']."    ";
                echo $row['email']."    ";
                echo $row['first_name']."<br>";
                $row=mysqli_fetch_array($select_query_result);
                echo $row['user_id']."    ";
                echo $row['email']."    ";
                echo $row['first_name']."<br>";
                
                $row=mysqli_fetch_array($select_query_result);
                echo $row['user_id']."    ";
                echo $row['email']."    ";
                echo $row['first_name']."<br>";
                $row=mysqli_fetch_array($select_query_result);
                echo $row['user_id']."    ";
                echo $row['email']."    ";
                echo $row['first_name']."<br>";
                
                $row=mysqli_fetch_array($select_query_result);
                echo $row['user_id']."    ";
                echo $row['email']."    ";
                echo $row['first_name']."<br>";
                
                
                
                 
                 
                 
                 
                
                
                ?>
                
               <?php
                function sum($parameter1, $parameter2){
                    $addtion=$parameter1+$parameter2;
                    return $addtion;                 
                }       
               ?>
            </div>
         			
		
	
		
	</body>
</html>
