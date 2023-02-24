import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:youtube/Video.dart';

const CHAVE_YOUTUBE_API = "AIzaSyDyHOfL3MzdUJu1hDArw9vFe28JWERxY84";
const ID_CANAL = "UCt_4wzTQqmcUvemNkeO0plA";
const URL_BASE = "https://www.googleapis.com/youtube/v3/";

class Api {

   Future<List<Video>> pesquisar( String pesquisa) async {

    http.Response response = await http.get(
      Uri.parse(URL_BASE + "search"
          "?part=snippet"
          "&type=video"
          "&maxResults=20"
          "&order=relevance"
          "&key=$CHAVE_YOUTUBE_API"
          //"&channelId=$ID_CANAL"
          "&q=$pesquisa"
    )
    );

if( response.statusCode == 200 ) {

  Map<String, dynamic> dadosJson = jsonDecode( response.body );

  List<Video> videos = dadosJson["items"].map<Video>(
      (map) {
        return Video.fromJson(map);
        //return Video.converterJson(map);
      }
  ).toList();

  return videos;

  //for( var video in videos ) {
    //return videos;
  //}

  for( var video in dadosJson["items"]){
    print("Resultado: " + video.toString());
  }
  //print("resultado: " + dadosJson["items"].toString());

}else{

}
return pesquisar(pesquisa);

  }
}