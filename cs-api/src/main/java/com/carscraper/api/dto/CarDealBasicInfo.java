package com.carscraper.api.dto;

import java.math.BigDecimal;
import java.util.UUID;

public interface CarDealBasicInfo {
    UUID getId();
    String getBrand();
    String getModel();
    BigDecimal getMonthlyPayment();
    BigDecimal getDueAtSigning();
    String getImageUrl();
}
