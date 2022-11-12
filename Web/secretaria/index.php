<?php include "header.php"; ?>

    <!-- Page Wrapper -->
    <div id="wrapper">

        <!-- Sidebar -->
        <?php include "menu.php"; ?>
        <!-- End of Sidebar -->

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">

                <!-- Topbar -->
                <?php include "topbar.php"; ?>
                <!-- End of Topbar -->

                <!-- Begin Page Content -->
                <div class="container-fluid">

                    <!-- Content Row -->
                    <?php include "cards.php"; ?>

                    <!-- Content Row -->

                    <?php
                        if(!isset($_GET['r'])){
                            include "template/index.php";
                        }else{                        
                            switch ($_GET['r']){
                                case 'inicio':
                                include "template/index.php";
                                break;

                                case 'cadAluno':
                                    include "template/cadAluno.php";
                                    break;

                                default:
                                include "template/index.php";
                            }   
                        }
                    ?>



                </div>
                <!-- /.container-fluid -->

            </div>
            <!-- End of Main Content -->

            <!-- Footer -->
            <?php include "footer.php"; ?>
            <!-- End of Footer -->

        </div>
        <!-- End of Content Wrapper -->

    </div>
    <!-- End of Page Wrapper -->

    <?php include "acessorio.php"; ?>

   <?php include "js.php"; ?>