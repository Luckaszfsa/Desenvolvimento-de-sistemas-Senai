package com.boxes.tcc.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.boxes.tcc.entities.Order;

public interface OrderRepository extends JpaRepository<Order, Long> {

}
