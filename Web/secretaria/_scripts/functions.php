<?php
function totalCard($tipo)
{
    include "config.php";
    $sql = "SELECT * FROM cadaluno";
    $query = $mysqli->query($sql);
    $total = $query->num_rows;

    return $total;
}

function validarAluno($cpf)
{
    include "config.php";
    $sql = "SELECT id FROM cadaluno WHERE cpf = '$cpf'";
    $query = $mysqli->query($sql);
    $total = $query->num_rows;

    return $total;
}