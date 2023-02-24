<div class="row">
    <div class="col-xl-12 col-lg-12">
        <div class="card shadow mb-4">
            <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 class="m-0 font-weight-bold text-primary">Alterar Cadastro de Alunos</h6>
            </div>
            <div class="card-body">
                <table id="example" class="table table-striped" style="width:100%">
                    <thead>
                        <tr>
                            <th>Aluno</th>
                            <th>Rua</th>
                            <th>Bairro</th>
                            <th>Cidade</th>
                            <th>#</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        include "_scripts/config.php";
                        $sql = "SELECT * FROM cadAluno";
                        $query = $mysqli->query($sql);
                        while ($dados = $query->fetch_array()) {
                        ?>

                        <tr>
                            <td><?php echo $dados['nome']; ?></td>
                            <td><?php echo $dados['rua']; ?></td>
                            <td><?php echo $dados['bairro']; ?></td>
                            <td><?php echo $dados['cidade']; ?></td>
                            <td>
                                <a href="index.php?r=alterarAluno&id=<?php echo $dados['id']; ?>">
                                    <i class="fa-solid fa-pen"></i>
                                </a>
                                &nbsp;&nbsp;
                                <i class="fa-solid fa-trash"></i>
                            </td>
                        </tr>

                        <?php } ?>
                    </tbody>
                    <tfoot>
                        <tr>
                            <th>Aluno</th>
                            <th>Rua</th>
                            <th>Bairro</th>
                            <th>Cidade</th>
                            <th></th>
                        </tr>
                    </tfoot>
                </table>
            </div>
        </div>
    </div>
</div>

<script type="text/javascript" src="//js.nicedit.com/nicEdit-latest.js"></script>
<script type="text/javascript">
bkLib.onDomLoaded(function() {
    nicEditors.allTextAreas()
});
</script>

<?php
if (!empty($_POST['nome'])) {
    include "_scripts/config.php";
    $nome = $_POST['nome'];
    $sexo = $_POST['sexo'];
    $cpf = $_POST['cpf'];
    $cep = $_POST['cep'];
    $rua = $_POST['rua'];
    $cidade = $_POST['cidade'];
    $bairro = $_POST['bairro'];
    $estado = $_POST['estado'];
    $obs = $_POST['obs'];

    if (validarUsuario($cpf, 'cadAluno') >= 1) { ?>
<script type="text/javascript">
Swal.fire(
    'Ops!',
    'Esse CPF já está cadastrado.',
    'question'
)
</script>
<?php } else {

        $sql = "INSERT INTO cadAluno (nome, estado_civil, cpf, rua, bairro, estado,obs, cidade) VALUES ('$nome','$sexo','$cpf','$rua','$bairro','$estado','$obs','$cidade')";
        $query = $mysqli->query($sql);

        if ($query) { ?>
<script type="text/javascript">
Swal.fire({
    title: 'Salvo',
    text: 'Aluno Cadastrado com Sucesso',
    icon: 'success',
    confirmButtonText: 'Ok'
}).then((result) => {
    if (result.isConfirmed) {
        location.href = "index.php?r=inicio";
    }
})
</script>
<?php } else { ?>
<script type="text/javascript">
swal("Erro");
</script>
<?php }
    }
}

?>