import 'package:flutter/material.dart';

class TelaContato extends StatefulWidget {
  const TelaContato({Key? key}) : super(key: key);

  @override
  State<TelaContato> createState() => _TelaContatoState();
}

class _TelaContatoState extends State<TelaContato> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text("Contato"),
        backgroundColor: Colors.green,

      ),
      body: SingleChildScrollView(
        child: Container(
          padding: EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget> [
              Row(
                children: <Widget>[
                  Image.asset("imagens/detalhe_contato.png"),
                  Padding(padding: EdgeInsets.only(left: 10),
                    child: Text(
                      "Contato",
                      style: TextStyle(
                          fontSize: 20,

                      ),
                    ),
                  )
                ],
              ),
              Padding(padding: EdgeInsets.only(top: 16),
                child:Text(
                    "atendimento@atmconsultoria.com.br"
                ) ,
              ),
              Padding(padding: EdgeInsets.only(top: 16),
                child:Text(
                    "Telefone: (11) 3525 - 8596"
                ) ,
              ),
              Padding(padding: EdgeInsets.only(top: 16),
                child:Text(
                    "Celular: (11) 99586-5236"
                ) ,
              )

            ],
          ),

        ),
      ),
    );
  }
}
