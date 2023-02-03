<?php include "config.php"; ?>
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Projeto Bolão</title>
</head>

<body>
    <div class="container col-md-4 ">
        <div class="row">
            <table class="table">
                <thead>
                    <tr>
                        <th style="text-align:center;vertical-align:middle">Time A</th>
                        <th style="text-align:center;vertical-align:middle">Resultado</th>
                        <th style="text-align:center;vertical-align:middle">x</th>
                        <th style="text-align:center;vertical-align:middle">Resultado</th>
                        <th style="text-align:center;vertical-align:middle">Time B</th>
                    </tr>
                </thead>
                <form method="post" action="_scripts/salvar.php">
                    <tbody>
                        <?php
                        include "config.php";
                        $sql = "SELECT * FROM jogos WHERE rodada = '1 RODADA' AND situacao = 'ABERTO'";
                        $query = $mysqli->query($sql);
                        $a = 1;
                        while ($dados = $query->fetch_array()) {
                        ?>
                            <input type="hidden" name="jogo<?php echo $a; ?>" value="<?php echo $dados['Id']; ?>">
                            <tr>


                                <td style="text-align:center;vertical-align:middle">
                                    <img src="images/<?php echo $dados['timea']; ?>.png"> <br>
                                    <?php echo $dados['timea']; ?>


                                <td style="text-align:center;vertical-align:middle">
                                    <input type="text" name="timea<?php echo $a; ?>" size='1' maxlength="2" required>
                                </td>

                                </td>
                                <td style="text-align:center;vertical-align:middle"> x </td>
                                <td style="text-align:center;vertical-align:middle" size='1'>
                                    <input type="text" name="timeb<?php echo $a; ?>" size='1' maxlength="2" required>
                                </td>
                                <td style="text-align:center;vertical-align:middle">
                                    <img src="images/<?php echo $dados['timeb']; ?>.png"> <br>
                                    <?php echo $dados['timeb']; ?>

                                </td>

                            </tr>
                            <tr style="text-align:center;vertical-align:middle">
                                <td colspan="5">
                                    <?php echo $dados['dia']; ?><br>
                                    <?php echo $dados['localidade'] . ' '; ?>
                                    <?php echo $dados['horario'] . ' '; ?>
                                    <?php echo $dados['tipo'] . ' '; ?>
                                </td>
                            </tr>
                        <?php $a++;
                        } ?>

                    </tbody>


                    <div>
                        <tr>
                            <td>
                                <button type="submit" class="btn btn-primary">Salvar</button>
                            </td>
                        </tr>
                    </div>

                </form>

            </table>
        </div>



    </div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous">
    </script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
</body>

</html>