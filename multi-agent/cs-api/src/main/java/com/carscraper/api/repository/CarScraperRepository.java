package com.carscraper.api.repository;

import com.carscraper.api.dto.CarDealBasicInfo;
import com.carscraper.api.model.CarDeal;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface CarScraperRepository extends JpaRepository<CarDeal, UUID> {

    @Query("SELECT c.id AS id, c.brand AS brand, c.model AS model, c.monthlyPayment AS monthlyPayment, c.dueAtSigning as dueAtSigning, c.imageUrl as imageUrl FROM CarDeal c")
    List<CarDealBasicInfo> findBasicInfoForAllCars();
}
