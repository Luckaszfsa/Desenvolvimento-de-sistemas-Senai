<div class="row">
    <div class="col-xl-12 col-lg-7">
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
                        <label for="inputEmail4" class="form-label">Sexo</label>
                        <select class="form-control" name="sexo" id="">
                            <option value="">-</option>
                            <option value="">Masculino</option>
                            <option value="">Feminino</option>

                        </select>
                    </div>
                    <div class="col-md-4">
                        <label for="inputEmail4" class="form-label">CPF</label>
                        <input type="text" name="cpf" class="form-control" id="inputEmail4">
                    </div>
                    <div class="col-md-4">
                        <label for="inputPassword4" class="form-label">CEP</label>
                        <input onblur="pesquisacep(this.value);" type="text" name="cep" style="max-width:200px;"
                            class="form-control" id="cep">
                    </div>

                    <div class="col-sm">
                        <label for="inputPassword4" class="form-label">Rua</label>
                        <input type="text" name="rua" readonly class="form-control" id="rua">
                    </div>

                    <div class="col-sm">
                        <label for="inputPassword4" class="form-label">Cidade</label>
                        <input type="text" name="cidade" readonly class="form-control" id="cidade">
                    </div>

                    <div class="col-sm">
                        <label for="inputPassword4" class="form-label">Bairro</label>
                        <input type="text" name="bairro" readonly class="form-control" id="bairro">
                    </div>

                    <div class="col-sm">
                        <label for="inputPassword4" class="form-label">Estado</label>
                        <input type="text" name="estado" readonly class="form-control" id="estado">
                    </div>

                    <div class="col-md-12">
                        <label for="inputPassword4" class="form-label">Observação</label>
                        <textarea name="obs" class="form-control"></textarea>
                    </div>


                    <div class="col-12">
                        <br>
                        <button type="submit" class="btn btn-primary">Cadastrar</button>
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

    $sql = "INSERT INTO cadaluno (nome, estado_civil, cpf,rua,cidade,bairro, estado, obs) VALUES ('$nome', '$sexo', '$cpf','$rua','$cidade','$bairro','$estado','$obs')";

    $query = $mysqli->query($sql);

    if ($query) {
        echo "<script>alert('Salvo')</script>";
    } else {
        echo "<script>alert('Erro')</script>";
    }
}





?>