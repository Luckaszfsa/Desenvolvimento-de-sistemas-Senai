<?php
include 'config.php';

$email = $_POST['email'];
$senha = md5($_POST['senha']);

$sql = "SELECT id FROM login WHERE email = '$email'";
$query = $mysqli->query($sql);
$total = $query->num_rows;

if ($total >= 1) {
    "Usuario já cadastrado";
} else {
    $sql = "INSERT INTO login values (NULL, '$usuario','$senha', '$email')";
    $query = $mysqli->query($sql);

    if ($query) {
        echo "Cadastro realizado com sucesso";
    } else {
        echo "Problema na query";
    }
}