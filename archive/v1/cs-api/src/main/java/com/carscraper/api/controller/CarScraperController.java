package com.carscraper.api.controller;

import com.carscraper.api.dto.CarDealBasicInfo;
import com.carscraper.api.model.CarDeal;
import com.carscraper.api.service.CarScraperService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/v1")
public class CarScraperController {

    @Autowired
    private CarScraperService carScraperService;

    @GetMapping("")
    public List<CarDealBasicInfo> getAllCarsBasicInfo() {
        return carScraperService.getAllCarsBasicInfo();
    }

    @GetMapping("/{id}")
    public CarDeal getCarDetails(@PathVariable String id) {
        Optional<CarDeal> carDeal = carScraperService.getCarDetails(id);
        return carDeal.orElse(null);
    }
}
