<!doctype html>
<html lang="pt-br">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../../../favicon.ico">

    <title>Login - Escola do Sol</title>

    <!-- Bootstrap core CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="_css/signin.css" rel="stylesheet">
</head>

<body class="text-center">
    <form class="form-signin" method="post">
        <img class="mb-4" src="_images/logo.png" alt="" width="120" height="80">
        <h1 class="h3 mb-3 font-weight-normal">Escola do Sol</h1>
        <label for="inputEmail" class="sr-only">E-mail</label>
        <input type="email" id="inputEmail" name="email" class="form-control" placeholder="E-mail" required autofocus>
        <label for="inputPassword" class="sr-only">Senha</label>
        <input type="password" name="senha" id="inputPassword" class="form-control" placeholder="Senha" required>

        <button class="btn btn-lg btn-primary btn-block" type="submit">Entrar</button>
        <p class="mt-5 mb-3 text-muted">&copy; 2017-2022</p>
    </form>
</body>
<script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>

</html>


<?php

if (isset($_POST)) {

  $email = $_POST['email'];
  $senha = $_POST['senha'];

  $valida_email = "luckasz.mendes@gmail.com";
  $valida_senha = '123';



  if ($email == $valida_email) { //verificamos se o e-mail está correto 

    if ($senha == $valida_senha) { //caso o e-mail esteja ok, validamos a senha 
?>
<script>
Swal.fire({
    icon: 'success',
    title: 'Login',
    text: 'Login com sucesso'
})
</script>
<?php } else { //caso o login esteja ok e a senha incorreta, mensagem de erro 
    ?>
<script>
Swal.fire({
    icon: 'info',
    title: 'Login',
    text: 'senha incorreta'
})
</script>
<?php }
  } else { //caso o login não esteja ok, já avisamos sem validar a senha 
    ?>

<script>
Swal.fire({
    icon: 'info',
    title: 'Login',
    text: 'Login incorreto'
})
</script>

<?php }
} ?>