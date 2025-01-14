package com.carscraper.api.service;

import com.carscraper.api.dto.CarDealBasicInfo;
import com.carscraper.api.model.CarDeal;
import com.carscraper.api.repository.CarScraperRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class CarScraperService {

    @Autowired
    CarScraperRepository carScraperRepository;

    public List<CarDealBasicInfo> getAllCarsBasicInfo() {
        return carScraperRepository.findBasicInfoForAllCars();
    }

    public Optional<CarDeal> getCarDetails(String id) {
        return carScraperRepository.findById(UUID.fromString(id));
    }
}
