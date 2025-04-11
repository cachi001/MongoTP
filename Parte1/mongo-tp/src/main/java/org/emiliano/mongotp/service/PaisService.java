package org.emiliano.mongotp.service;

import org.emiliano.mongotp.model.Pais;
import org.emiliano.mongotp.repository.PaisRepository;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@Service
public class PaisService {

    private final PaisRepository paisRepository;
    private final WebClient webClient;

    public PaisService(PaisRepository paisRepository, WebClient webClient) {
        this.paisRepository = paisRepository;
        this.webClient = webClient;
    }

    public void importarPaises() {
        List<Integer> codigos = new ArrayList<>();
        for (int i = 1; i < 999; i++) {
            codigos.add(i);
        }

        List<Pais> paises = importarSecuencial(codigos, new ArrayList<>());

        if (!paises.isEmpty()) {
            List<Pais> guardados = paisRepository.saveAll(paises);
            System.out.println("✅ Importación finalizada. Total países importados: " + guardados.size());
        } else {
            System.out.println("❌ No se importaron países.");
        }
    }

    private List<Pais> importarSecuencial(List<Integer> codigos, List<Pais> paises) {
        for (Integer codigo : codigos) {
            Pais pais = obtenerPais(codigo);

            if (pais != null) {

                Long id = codigo.longValue();

                Optional<Pais> paisOptional = paisRepository.findById(id);

                if (paisOptional.isPresent()) {

                    Pais paisExistente = paisOptional.get();

                    pais.setCodigoPais(paisExistente.getCodigoPais());
                    pais.setNombrePais(paisExistente.getNombrePais());
                    pais.setCapitalPais(paisExistente.getCapitalPais());
                    pais.setLatitud(paisExistente.getLatitud());
                    pais.setLongitud(paisExistente.getLongitud());
                    pais.setPoblacion(paisExistente.getPoblacion());
                    pais.setRegion(paisExistente.getRegion());
                    pais.setSubregion(paisExistente.getSubregion());

                    paises.add(paisExistente);
                }
                paises.add(pais);
            }
        }
        return paises;
    }

    private Pais obtenerPais(int codigo) {
        String codigoStr = String.format("%03d", codigo);

        try {
            List<Map<String, Object>> response = webClient.get()
                    .uri("/" + codigoStr)
                    .retrieve()
                    .bodyToMono(new ParameterizedTypeReference<List<Map<String, Object>>>() {})
                    .block(); // ← bloquea y espera la respuesta

            return mapearPais(response, codigoStr);
        } catch (Exception e) {
            System.err.println("⚠️ Error al importar código " + codigoStr + ": " + e.getMessage());
            return null;
        }
    }


    private Pais mapearPais(List<Map<String, Object>> json, String codigoStr) {
        try {
            if (json == null) return null;

            Map<String, Object> dataObject = json.get(0);

            Map<String, Object> nameObj = (Map<String, Object>) dataObject.get("name");
            String nombrePais = (String) nameObj.get("common");

            List<String> capitalList = (List<String>) dataObject.get("capital");
            String capitalPais = (capitalList != null && !capitalList.isEmpty()) ? capitalList.get(0) : null;

            String region = (String) dataObject.get("region");
            String subregion = (String) dataObject.get("subregion");
            Number poblacionNum = (Number) dataObject.get("population");
            Long poblacion = (poblacionNum != null) ? poblacionNum.longValue() : null;

            List<Double> latlng = (List<Double>) dataObject.get("latlng");
            Double latitud = (latlng != null && latlng.size() > 0) ? latlng.get(0) : null;
            Double longitud = (latlng != null && latlng.size() > 1) ? latlng.get(1) : null;

            Long codigoPais = Long.parseLong(codigoStr);

            if (nombrePais == null || capitalPais == null || region == null || subregion == null || poblacion == null || latitud == null || longitud == null) {
                return null;
            }

            return new Pais(codigoPais, nombrePais, capitalPais, region, subregion, poblacion, latitud, longitud);

        } catch (Exception e) {
            System.err.println("❌ Error al mapear país: " + e.getMessage());
            return null;
        }
    }
}
