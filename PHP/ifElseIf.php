<?php

$marks = 50;


if ($marks>90){
    echo "The student is in the merit list";
}
else if (($marks>40) and ($marks < 90)){
    echo "The student has passed";
}
else if ($marks>=40){
    echo "The student has just passed";
}
else{
    echo "The student has failed";
}



?>