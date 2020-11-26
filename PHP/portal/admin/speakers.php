<?php
require "common.php";
?>

<?php
$title = "Speakers";
require 'header.php';
echo '
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->

<div class="wrapper row3">
    <div class="rounded">
    <main class="container clear">
      <!-- main body -->
      <!-- ################################################################################################ -->
    <div class="group btmspace-30">
        <div class="custom_heading" style="margin-top:1px;">
	     <h2 style="border-radius: 3px; background-color:#095586; color:#FFFFFF; margin-top:5px;"><span style="padding: 0.5em 6px 1px; border-left: 6px solid #FFCC33; height: 500px;"></span>SPEAKERS</h2>
	</div>
	





';
                $row=mysqli_fetch_array($select_query_result);
echo'
    <ul style="margin-left: -40px;">
        <strong style="margin-top:10px; font-size:18px; color:#666666;"><h2>Special Lecture</h2></strong>
            <div class="table-responsive">
                <table class="table table-striped table-bordered table-hover">
                <tbody>      
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                </tbody>
                </table>
            </div>
        </ul>
        






';
                $row=mysqli_fetch_array($select_query_result);
echo'
        <ul style="margin-left: -40px;">
        <strong style="margin-top:10px; font-size:18px; color:#666666;"><h2>Animesh Chakravorty Endowment Lecture</h2></strong>
            <div class="table-responsive">
                <table class="table table-striped table-bordered table-hover">
                <tbody>      
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                </tbody>
                </table>
            </div>
        </ul>
        






';
                $row=mysqli_fetch_array($select_query_result);
echo'
        <ul style="margin-left: -40px;">
        <strong style="margin-top:10px; font-size:18px; color:#666666;"><h2>C. N. R. Rao National Prize for Chemical Research Lecture</h2></strong>
            <div class="table-responsive">
                <table class="table table-striped table-bordered table-hover">
                <tbody>      
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                </tbody>
                </table>
            </div>
        </ul>
        




';
                $row=mysqli_fetch_array($select_query_result);
echo'
        <ul style="margin-left: -40px;">
        <strong style="margin-top:10px; font-size:18px; color:#666666;"><h2>CRSI Honorary Fellow</h2></strong>
            <div class="table-responsive">
                <table class="table table-striped table-bordered table-hover">
                <tbody>      
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                </tbody>
                </table>
            </div>
        </ul>
        






        <ul style="margin-left: -40px;">
        <strong style="margin-top:10px; font-size:18px; color:#666666;"><h2>CRSI Silver Medal Lectures</h2></strong>
            <div class="table-responsive">
                <table class="table table-striped table-bordered table-hover">
                <tbody>  
                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>

                </tbody>
                </table>
            </div>
        </ul>
        



        <ul style="margin-left: -40px;">
        <strong style="margin-top:10px; font-size:18px; color:#666666;"><h2>CRSI Bronze Medal Lectures</h2></strong>
            <div class="table-responsive">
                <table class="table table-striped table-bordered table-hover">
                <tbody>      
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                
                </tbody>
                </table>
            </div>
        </ul>



        <ul style="margin-left: -40px;">
        <strong style="margin-top:10px; font-size:18px; color:#666666;"><h2>Other Special Lectures</h2></strong>
            <div class="table-responsive">
                <table class="table table-striped table-bordered table-hover">
                <tbody>      
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                                ';
                $row=mysqli_fetch_array($select_query_result);
                echo'
                <tr>
                <td>
                    <p><img style="float: left; margin: 0px 15px 15px 0px;  border: 1px solid #ddd; border-radius: 50%; 
                padding: 5px; " src="data:image/jpeg;base64,'.base64_encode($row['img'] ).'" width="100"> <span style="font-size:14px; font-weight:bold;">
                <a style="font-size:14px; font-weight:bold;line-height: 1.8em" href="';
                echo $row['link'];
                    echo'" 
                target="_blank" >';
                echo $row['name'];
                    echo'</a></span> <br>';
                echo $row['title'];
                    echo'<br/>
	        <span style="width:780px; font-size:14px; color:#565656;"> <b> Talk Title:</b>';
                echo $row['talk_title'];
                    echo'</span>
                    </p>
                </td>
                </tr>
                </tbody>
                </table>
            </div>
        </ul>



    </div>
    </main>
    </div>
</div>';
require 'footer.php'
?>