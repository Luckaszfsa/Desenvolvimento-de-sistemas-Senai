import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'dart:math';

void main(){
  runApp(const MaterialApp(
    home: const Home() ,
    debugShowCheckedModeBanner: false,
  ));
}

class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  var _frases = [
    "Para bom entendedor, meia palavra basta",
    "De grão em grão, a galinha enche o papo",
    "Casa de ferreiro, espeto de pau",
    "Onde há fumaça há fogo",
    "Pimenta nos olhos dos outros é refresco",
    "Quem com ferro fere, com ferro será ferido"
  ];

  var _fraseGerada = "Clique abaixo para gerar uma frase!";

  void _gerarFrase(){

    var numeroSorteado = Random().nextInt(_frases.length);


    setState(() {
      _fraseGerada = _frases[numeroSorteado];
    });

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Ditados populares'),
        backgroundColor: Colors.blueAccent,
      ),
      body: Center(
        child: Container(
          padding: EdgeInsets.all(16),
          width: double.infinity,
          child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget> [
                Image.asset("images/logo.png"),
                Text(
                  _fraseGerada,
                  textAlign: TextAlign.justify,
                  style: TextStyle(
                      fontSize: 17,
                      fontStyle: FontStyle.italic,
                      color: Colors.black
                  ),
                ),
                ElevatedButton(
                    child: Text(
                      "Nova Frase",
                      style: TextStyle(
                          fontSize: 25,
                          color: Colors.white,
                          fontWeight: FontWeight.bold),
                    ),
                    onPressed: _gerarFrase,
                )
              ]
          ),
        ),
       )
    );
  }
}
