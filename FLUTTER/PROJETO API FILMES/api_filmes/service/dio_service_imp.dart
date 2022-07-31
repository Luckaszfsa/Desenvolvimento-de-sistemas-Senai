// ignore: depend_on_referenced_packages
import 'dart:html';

import 'package:dio/dio.dart';
import 'package:movieapp/service/dio_service.dart';

import 'dio_service.dart';

class DioServiceImp implements Dioservice {
  @override
  Dio getDio() {
    return Dio(
      BaseOptions(
        baseUrl: 'https://api.themoviedb.org/4/',
        headers: {
          'content-type': 'application/json;charset=utf-8',
          'authorization':
              'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYTljYWE1MDgyZTcwMDMzMzRkNzMzNGIzMGVmYjdhMCIsInN1YiI6IjYyZDc0MDFkYWJmOGUyMDA2ZWIyNDczZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.slGIYFtiq5x6mSagCjlZDa1SkC31uQVFOj7nfCcAFlU',
        },
      ),
    );
  }
}
