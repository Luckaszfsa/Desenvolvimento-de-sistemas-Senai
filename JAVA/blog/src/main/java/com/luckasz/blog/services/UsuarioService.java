package com.luckasz.blog.services;

import java.util.List;

import com.luckasz.blog.entities.Usuario;

public interface UsuarioService {
    List<Usuario> findAll();

    Usuario findById(Long id);

    Usuario save(Usuario usuario);

    void deleteById(Long id);
    
   

	Usuario updateUsuario(Long id,Usuario usuario);
}
