<div class="row">
    <div class="col-xl-12 col-lg-12">
        <div class="card shadow mb-4">
            <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 class="m-0 font-weight-bold text-primary">Cadastro de Disciplinas</h6>
            </div>
            <div class="card-body">
                <form class="row g-3" method="post" action="index.php?r=cadDisciplina">
                    <div class="col-md-12">
                        <label for="inputEmail4" class="form-label">Nome da Disciplina</label>
                        <input type="text" name="disciplina" class="form-control" id="inputEmail4">
                    </div>

                    <div class="col-md-4">
                        <label for="inputPassword4" class="form-label">Tipo</label>
                        <select class="form-control" name="tipo">
                            <option value="">-</option>
                            <option value="Ciências Naturais">Ciências Naturais</option>
                            <option value="Exatas">Exatas</option>
                            <option value="Humanas">Humanas</option>
                        </select>
                    </div>

                    <div class="col-md-4">
                        <label for="inputEmail4" class="form-label">Carga Horária</label>
                        <input type="text" name="ch" class="form-control" id="inputEmail4">
                    </div>


                    <div class="col-12">
                        <button type="submit" class="btn btn-primary">Cadastrar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>


<?php
if (!empty($_POST['disciplina'])) {
    include "_scripts/config.php";
    $disciplina = $_POST['disciplina'];
    $tipo = $_POST['tipo'];
    $ch = $_POST['ch'];

    if (cadDisciplina($disciplina) >= 1) { ?>
<script type="text/javascript">
Swal.fire(
    'Ops!',
    'Esse Disciplina já está cadastrada.',
    'question'
)
</script>
<?php } else {

        $sql = "INSERT INTO caddisciplina (nome_disciplina, carga_horaria, tipo) VALUES ('$disciplina','$tipo','$tipo')";
        $query = $mysqli->query($sql);

        if ($query) { ?>
<script type="text/javascript">
Swal.fire({
    title: 'Salvo',
    text: 'Disciplina Cadastrada com Sucesso',
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