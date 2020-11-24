<?php
require "common.php";
?>


       


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
        
