package org.emiliano.mongotp.controller;

import org.emiliano.mongotp.repository.PaisRepository;
import org.emiliano.mongotp.service.PaisService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("paises")
public class PaisController {

    private final PaisService paisService;

    public PaisController (PaisService paisService){
        this.paisService = paisService;

    }

    @PostMapping("/importar")
    public ResponseEntity<?> importarPaises (){
         try {
             paisService.importarPaises();
             return ResponseEntity.ok().body("Importando Paises...");
         } catch (Exception e) {

             return ResponseEntity.status(HttpStatus.valueOf(404)).body(e.getMessage());
        }
    }
}
