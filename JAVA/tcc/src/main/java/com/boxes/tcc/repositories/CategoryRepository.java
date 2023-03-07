package com.boxes.tcc.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.boxes.tcc.entities.Category;

public interface CategoryRepository extends JpaRepository<Category, Long> {

}
