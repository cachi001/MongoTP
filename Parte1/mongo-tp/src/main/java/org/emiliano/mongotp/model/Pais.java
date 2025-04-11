package org.emiliano.mongotp.model;

import lombok.*;
import jakarta.persistence.*;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Pais {

    @Id
    private Long codigoPais;

    @Column(length = 50, nullable = false)
    private String nombrePais;

    @Column(length = 50, nullable = false)
    private String capitalPais;

    @Column(length = 50, nullable = false)
    private String region;

    @Column(length = 50, nullable = false)
    private String subregion;

    @Column(nullable = false)
    private Long poblacion;

    @Column(nullable = false)
    private double latitud;

    @Column(nullable = false)
    private double longitud;



}
