package com.luckasz.blog.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.luckasz.blog.entities.Usuario;



public interface UsuarioRepository extends JpaRepository<Usuario, Long> {
    Usuario findByEmail(String email);
}

