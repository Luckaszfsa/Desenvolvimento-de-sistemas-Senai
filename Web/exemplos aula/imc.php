<html>
  <head></head>
  <body>
    <form method="GET">
      Sua Altura:
      <input type="text" name="altura">       <br>
      Seu Peso:
      <input type="text" name="peso">
      <br>
      <input type="submit" value="Salvar">
    </form>
  </body>
</html>
<?php 

  $dados = imc($_GET['altura'],$_GET['peso']);
  echo 'Seu IMC ' .$dados[0]. 'e sua FAIXA é'. $dados[1];

  function imc($a,$p) {
    $imc = $p/($a*$a);

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