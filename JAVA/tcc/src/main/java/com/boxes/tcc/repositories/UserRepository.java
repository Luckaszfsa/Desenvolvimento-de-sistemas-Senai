package com.boxes.tcc.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.boxes.tcc.entities.User;

public interface UserRepository extends JpaRepository<User, Long> {

}
