package com.boxes.tcc.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.boxes.tcc.entities.Product;


public interface ProductRepository extends JpaRepository<Product, Long> {

}
