package com.boxes.tcc.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.boxes.tcc.entities.OrderItem;

public interface OrderItemRepository extends JpaRepository<OrderItem, Long> {

}
