package com.luckasz.blog.controller;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.luckasz.blog.dto.UsuarioDTO;
import com.luckasz.blog.entities.Usuario;
import com.luckasz.blog.services.UsuarioService;

import jakarta.validation.Valid;

@RestController
@RequestMapping("/api/usuarios")
public class UsuarioController {

    @Autowired
    private UsuarioService usuarioService;
    
    @GetMapping("/{id}")
    public UsuarioDTO buscarUsuarioPorId(@PathVariable Long id) {
        Usuario usuario = usuarioService.findById(id);
        return new UsuarioDTO(usuario);
    }

    @GetMapping
    public List<UsuarioDTO> buscarTodosUsuarios() {
        List<Usuario> usuarios = usuarioService.findAll();
        return usuarios.stream().map(UsuarioDTO::new).collect(Collectors.toList());
    }

    @PostMapping("/cadastro")
    public UsuarioDTO cadastrarUsuario(@Valid @RequestBody UsuarioDTO usuarioDTO) {
        Usuario usuario = usuarioService.save(usuarioDTO.toEntity());
        return new UsuarioDTO(usuario);
    }

    @PutMapping("/{id}")
    public UsuarioDTO atualizarUsuario(@PathVariable Long id, @Valid @RequestBody UsuarioDTO usuarioDTO) {
        Usuario usuario = usuarioService.updateUsuario(id, usuarioDTO.toEntity());
        return new UsuarioDTO(usuario);
    }

    @DeleteMapping("/{id}")
    public String excluirUsuario(@PathVariable Long id) {
        usuarioService.deleteById(id);
        return "Usuário excluído com sucesso!";
    }
}

