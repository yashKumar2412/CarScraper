package com.carscraper.api.model;

import jakarta.persistence.*;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.UUID;

@Entity
@Table(name = "car_deals", uniqueConstraints = {
        @UniqueConstraint(columnNames = {"Brand", "Model", "Expiry_Date"})
})
public class CarDeal {

    @Id
    @GeneratedValue
    private UUID id;

    @Column(nullable = false)
    private String brand;

    @Column
    private String imageUrl;

    @Column(nullable = false)
    private String model;

    @Column(precision = 10, scale = 2)
    private BigDecimal msrp;

    @Column(name = "monthly_payment", precision = 10, scale = 2)
    private BigDecimal monthlyPayment;

    @Column(name = "due_at_signing", precision = 10, scale = 2)
    private BigDecimal dueAtSigning;

    @Column(name = "down_payment", precision = 10, scale = 2)
    private BigDecimal downPayment;

    @Column(name = "bank_fee", precision = 10, scale = 2)
    private BigDecimal bankFee;

    @Column(name = "total_payments", precision = 10, scale = 2)
    private BigDecimal totalPayments;

    @Column(name = "purchase_option", precision = 10, scale = 2)
    private BigDecimal purchaseOption;

    @Column(name = "termination_fee", precision = 10, scale = 2)
    private BigDecimal terminationFee;

    @Column(name = "excess_mile_fee", precision = 10, scale = 2)
    private BigDecimal excessMileFee;

    @Column(name = "miles_per_year", precision = 10, scale = 2)
    private BigDecimal milesPerYear;

    @Column(name = "doc_fee", precision = 10, scale = 2)
    private BigDecimal docFee;

    @Column(name = "offer_starts")
    private LocalDate offerStarts;

    @Column(name = "offer_ends")
    private LocalDate offerEnds;

    @Column(name = "lease_term", precision = 10, scale = 2)
    private BigDecimal leaseTerm;

    @Column(name = "lease_bonus", precision = 10, scale = 2)
    private BigDecimal leaseBonus;

    @Column
    private String drivetrain;

    @Column
    private String trim;

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public BigDecimal getMsrp() {
        return msrp;
    }

    public void setMsrp(BigDecimal msrp) {
        this.msrp = msrp;
    }

    public BigDecimal getMonthlyPayment() {
        return monthlyPayment;
    }

    public void setMonthlyPayment(BigDecimal monthlyPayment) {
        this.monthlyPayment = monthlyPayment;
    }

    public BigDecimal getDueAtSigning() {
        return dueAtSigning;
    }

    public void setDueAtSigning(BigDecimal dueAtSigning) {
        this.dueAtSigning = dueAtSigning;
    }

    public BigDecimal getDownPayment() {
        return downPayment;
    }

    public void setDownPayment(BigDecimal downPayment) {
        this.downPayment = downPayment;
    }

    public BigDecimal getBankFee() {
        return bankFee;
    }

    public void setBankFee(BigDecimal bankFee) {
        this.bankFee = bankFee;
    }

    public BigDecimal getTotalPayments() {
        return totalPayments;
    }

    public void setTotalPayments(BigDecimal totalPayments) {
        this.totalPayments = totalPayments;
    }

    public BigDecimal getPurchaseOption() {
        return purchaseOption;
    }

    public void setPurchaseOption(BigDecimal purchaseOption) {
        this.purchaseOption = purchaseOption;
    }

    public BigDecimal getTerminationFee() {
        return terminationFee;
    }

    public void setTerminationFee(BigDecimal terminationFee) {
        this.terminationFee = terminationFee;
    }

    public BigDecimal getExcessMileFee() {
        return excessMileFee;
    }

    public void setExcessMileFee(BigDecimal excessMileFee) {
        this.excessMileFee = excessMileFee;
    }

    public BigDecimal getMilesPerYear() {
        return milesPerYear;
    }

    public void setMilesPerYear(BigDecimal milesPerYear) {
        this.milesPerYear = milesPerYear;
    }

    public LocalDate getOfferStarts() {
        return offerStarts;
    }

    public void setOfferStarts(LocalDate offerStarts) {
        this.offerStarts = offerStarts;
    }

    public LocalDate getOfferEnds() {
        return offerEnds;
    }

    public void setOfferEnds(LocalDate offerEnds) {
        this.offerEnds = offerEnds;
    }

    public BigDecimal getDocFee() {
        return docFee;
    }

    public void setDocFee(BigDecimal docFee) {
        this.docFee = docFee;
    }

    public BigDecimal getLeaseTerm() {
        return leaseTerm;
    }

    public void setLeaseTerm(BigDecimal leaseTerm) {
        this.leaseTerm = leaseTerm;
    }

    public BigDecimal getLeaseBonus() {
        return leaseBonus;
    }

    public void setLeaseBonus(BigDecimal leaseBonus) {
        this.leaseBonus = leaseBonus;
    }

    public String getDrivetrain() {
        return drivetrain;
    }

    public void setDrivetrain(String drivetrain) {
        this.drivetrain = drivetrain;
    }

    public String getTrim() {
        return trim;
    }

    public void setTrim(String trim) {
        this.trim = trim;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }
}