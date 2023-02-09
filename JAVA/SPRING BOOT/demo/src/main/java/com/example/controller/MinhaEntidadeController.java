package com.example.controller;

import com.example.entity.MinhaEntidade;
import com.example.entity.MinhaEntidadeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class MinhaEntidadeController {

    @Autowired
    private MinhaEntidadeRepository repository;

    @GetMapping("/entidades")
    public List<MinhaEntidade> listarTodasEntidades() {
        return repository.findAll();
    }
}

