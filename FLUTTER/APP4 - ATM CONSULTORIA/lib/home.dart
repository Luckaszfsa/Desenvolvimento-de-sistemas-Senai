import 'package:atm_consultoria/TelaCliente.dart';
import 'package:atm_consultoria/TelaContato.dart';
import 'package:atm_consultoria/TelaEmpresa.dart';
import 'package:atm_consultoria/TelaServico.dart';
import 'package:flutter/material.dart';

class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {

  void _abrirEmpresa(){
    Navigator.push(
        context,
        MaterialPageRoute(builder: (context)=> TelaEmpresa()));
  }

  void _abrirServico(){
    Navigator.push(
        context,
        MaterialPageRoute(builder: (context)=> TelaServico()));
  }

  void _abrirCliente(){
    Navigator.push(
        context,
        MaterialPageRoute(builder: (context)=> TelaCliente()));
  }

  void _abrirContato(){
    Navigator.push(
        context,
        MaterialPageRoute(builder: (context)=> TelaContato()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text("ATM Consultoria"),
        backgroundColor: Colors.green,
      ),
      body: Container(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Image.asset('imagens/logo.png'),
            Padding(
              padding: EdgeInsets.only(top: 32),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
                  GestureDetector(
                    onTap: _abrirEmpresa,
                    child: Image.asset("imagens/menu_empresa.png"),
                  ),
                  GestureDetector(
                      onTap: _abrirServico,
                      child: Image.asset("imagens/menu_servico.png")
                  )
                ],
              ),

            ),

            Padding(
              padding: EdgeInsets.only(top: 32),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
                  GestureDetector(
                    onTap: _abrirCliente,
                    child: Image.asset("imagens/menu_cliente.png"),
                  ),
                  GestureDetector(
                      onTap: _abrirContato,
                      child: Image.asset("imagens/menu_contato.png")
                  )
                ],
              ),

            )
          ],
        ),
      ),
    );
  }
}
