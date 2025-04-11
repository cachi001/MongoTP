package org.emiliano.mongotp.repository;

import org.emiliano.mongotp.model.Pais;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PaisRepository extends JpaRepository<Pais, Long> {
}
