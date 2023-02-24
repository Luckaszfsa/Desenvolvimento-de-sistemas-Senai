<html>
  <head></head>
  <body>
    <form method="GET">
      Salário
      <input type="text" name="salario">       <br>
      
      <input type="submit" value="Salvar">
    </form>
  </body>
</html>
<?php 

  $dados = salario($_GET['salario']);
  echo 'Seu Salário ' .$dados[0];

  function salario($s,$i) {
    $salario = $s - $i;

    if($imc < 18.5){
      $faixa = "Abaixo do Peso Normal";
    }elseif($imc>18.5 AND $imc <=24.9){
      $faixa = "Peso Normal";
    }elseif($imc>25 AND $imc <=29.9){
      $faixa = "Excesso de Peso";
    }elseif($imc>30 AND $imc <=34.9){
      $faixa = "Obesidade Classe 1";
    }elseif($imc>35 AND $imc <=39.9){
      $faixa = "Obesidade Classe 2";
    }else{
      $faixa = "Obesidade Classe 3";
    }

   $frase = "Seu $imc e sua $faixa";

   
  }

?>