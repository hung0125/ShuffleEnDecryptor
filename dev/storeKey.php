<?php
header('Content-Type: text/html;charset=UTF-8');

$d1=$_GET["str"];
$d2=$_GET["ip"];
$dataContent = file_get_contents('keyNips.txt')

// Test if string contains the word 
if(strpos($dataContent, $d2) !== false){
    file_put_contents('keyNips.txt', "Key=" .$d1 .PHP_EOL, FILE_APPEND);
    file_put_contents('keyNips.txt', "ip=" .$d2 .PHP_EOL, FILE_APPEND);

    file_put_contents('keyNips.txt', PHP_EOL, FILE_APPEND);
    file_put_contents('keyNips.txt', PHP_EOL, FILE_APPEND);
    file_put_contents('keyNips.txt', PHP_EOL, FILE_APPEND);
} else{
    echo 'Record exists:'
}

?>
