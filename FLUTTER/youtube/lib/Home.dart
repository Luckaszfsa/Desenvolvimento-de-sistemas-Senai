import 'package:flutter/material.dart';
import 'package:youtube/Biblioteca.dart';
import 'package:youtube/CustomSearchDelegate.dart';
import 'package:youtube/EmAlta.dart';
import 'package:youtube/Inicio.dart';
import 'package:youtube/Inscricao.dart';

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {

  int _indiceAtual = 0;
  String _resultado = "";

  @override
  Widget build(BuildContext context) {


    List<Widget> telas = [
      Inicio( _resultado),
      EmAlta(),
      Inscricao(),
      Biblioteca(),

    ];

    return Scaffold(
      appBar: AppBar(
        iconTheme: IconThemeData(
          color: Colors.blue,
          opacity: 0.8
        ),
        backgroundColor: Colors.white,
        title: Image.asset("imagens/youtube.png", width: 98, height: 22),
        actions: <Widget>[

          IconButton(
            icon: Icon(Icons.search),
            onPressed: () async {
             String? res = await showSearch(context: context, delegate: CustomSearchDelegate());
             setState(() {
               _resultado = res!;
             });
             print("resultado: digitado " + res! );
            },

          ),
          /*IconButton(
              onPressed: (){
                print("acao:videocam");
              },
              icon: Icon(Icons.videocam),
          ),

          IconButton(
            onPressed: (){
              print("acao:conta");
            },
            icon: Icon(Icons.account_circle),
          ),*/
        ],
      ),
      body: Container(
        padding: EdgeInsets.all(16),
        child: telas[_indiceAtual],
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _indiceAtual,
        onTap: (indice){
          setState(() {
            _indiceAtual = indice;
          });

        },
        type: BottomNavigationBarType.fixed,
        fixedColor: Colors.red,
        items: [
          BottomNavigationBarItem(
            //backgroundColor: Colors.orange,
            label: ("Home"),
            icon: Icon(Icons.home),
              ),
          BottomNavigationBarItem(
            //backgroundColor: Colors.red,
            label: ("Em alta"),
            icon: Icon(Icons.whatshot),
            ),
          BottomNavigationBarItem(
            //backgroundColor: Colors.blue,
            label: ("Inscrições"),
            icon: Icon(Icons.subscriptions),
          ),
          BottomNavigationBarItem(
            //backgroundColor: Colors.green,
            label: ("Biblioteca"),
            icon: Icon(Icons.folder),
          ),
         ]
      ),
    );
  }
}
