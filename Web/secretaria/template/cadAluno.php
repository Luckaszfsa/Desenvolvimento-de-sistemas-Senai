<div class="row">
    <div class="col-xl-12 col-lg-12">
        <div class="card shadow mb-4">
            <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 class="m-0 font-weight-bold text-primary">Cadastro de Alunos</h6>
            </div>
            <div class="card-body">
                <form class="row g-3" method="post" action="index.php?r=cadAluno">
                    <div class="col-md-12">
                        <label for="inputEmail4" class="form-label">Nome</label>
                        <input type="text" name="nome" class="form-control" id="inputEmail4">
                    </div>

                    <div class="col-md-4">
                        <label for="inputPassword4" class="form-label">Sexo</label>
                        <select class="form-control" name="sexo">
                            <option value="">-</option>
                            <option value="M">Masculino</option>
                            <option value="F">Feminino</option>
                        </select>
                    </div>

                    <div class="col-md-4">
                        <label for="inputEmail4" class="form-label">CPF</label>
                        <input type="text" name="cpf" id="cpf" class="form-control" id="inputEmail4"
                            onblur="return verificarCPF(this.value)">
                    </div>
                    <div class="col-md-4">
                        <label for="inputPassword4" class="form-label">CEP</label>
                        <input type="text" name="cep" id="cep" onblur="pesquisacep(this.value);" class="form-control">
                    </div>

                    <div class="col-md-12">
                        <label for="inputPassword4" class="form-label">Rua</label>
                        <input type="text" name="rua" id="rua" readonly class="form-control">
                    </div>

                    <div class="col-md-6">
                        <label for="inputPassword4" class="form-label">Cidade</label>
                        <input type="text" name="cidade" id="cidade" readonly class="form-control">
                    </div>

                    <div class="col-md-6">
                        <label for="inputPassword4" class="form-label">Bairro</label>
                        <input type="text" name="bairro" readonly class="form-control" id="bairro">
                    </div>

                    <div class="col-md-12">
                        <label for="inputPassword4" class="form-label">Estado</label>
                        <input type="text" name="estado" readonly class="form-control" id="uf">
                    </div>

                    <div class="col-md-12">
                        <label for="inputPassword4" class="form-label">Observação</label>
                        <textarea name="obs" rows="7" cols="10" class="form-control"></textarea>
                    </div>


                    <div class="col-12">
                        <button type="submit" class="btn btn-primary">Sign in</button>
                    </div>
                </form>
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