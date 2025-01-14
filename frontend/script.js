let allCars = [];
let uniqueBrands = []

// Fetch all cars from the API
function fetchCars() {
    fetch('http://localhost:8080/api/v1')
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch cars.');
            return response.json();
        })
        .then(cars => {
            allCars = cars; // Save all cars for filtering
            console.log(allCars);   
            populateBrandFilter(cars); // Populate the brand multi-select dropdown
            displayCars(cars); // Display all cars initially
        })
        .catch(error => {
            console.error('Error fetching cars:', error);
            const carList = document.getElementById('car-list');
            if (carList) carList.innerHTML = `<p>Unable to load cars.</p>`;
        });
}

// Populate the brand multi-select dropdown
function populateBrandFilter(cars) {
    const brandFilter = document.getElementById('brand-filter');
    if (!brandFilter) return;

    // Clear any existing options
    brandFilter.innerHTML = '';

    
    // Add default "All Brands" option
    const allBrandsOption = document.createElement('option');
    allBrandsOption.value = '';
    allBrandsOption.textContent = 'All Brands';
    allBrandsOption.selected = true;
    brandFilter.appendChild(allBrandsOption);

    // Get unique brands and create options
    uniqueBrands = [...new Set(cars.map(car => car.brand))];
    uniqueBrands.forEach(brand => {
        const option = document.createElement('option');
        option.value = brand;
        option.textContent = brand;
        brandFilter.appendChild(option);
    });
}

// Get selected brands from the multi-select dropdown
function getSelectedBrands() {
    const brandFilter = document.getElementById('brand-filter');

    const selectedBrands = Array.from(brandFilter.selectedOptions)
        .map(option => option.value)
        .filter(value => value != '')

    return selectedBrands;
}

// Display a list of cars in the UI
function displayCars(cars) {
    const carList = document.getElementById('car-list');
    if (!carList) return;

    carList.innerHTML = ''; // Clear previous content
    if (cars.length === 0) {
        carList.innerHTML = `<p>No cars match your search or filter criteria.</p>`;
        return;
    }

    cars.forEach(car => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <img src="${car.imageUrl}" alt="${car.model}" class="card-img" />
            <h3>${car.model}</h3>
            <p><strong>Brand:</strong> ${car.brand}</p>
            <p><strong>Monthly Payment:</strong> $${car.monthlyPayment ? car.monthlyPayment.toFixed(2) : 'N/A'}</p>
            <p><strong>Due at Signing:</strong> $${car.dueAtSigning ? car.dueAtSigning.toFixed(2) : 'N/A'}</p>
            <button onclick="viewCar('${car.id}')">View Details</button>
        `;
        carList.appendChild(card);
    });
}

// Filter cars based on search and filters
function filterCars() {
    const searchQuery = document.getElementById('search-bar').value.toLowerCase();
    const selectedBrands = getSelectedBrands();
    const minPrice = parseFloat(document.getElementById('min-price').value) || 0;
    const maxPrice = parseFloat(document.getElementById('max-price').value) || Infinity;
    const minDue = parseFloat(document.getElementById('min-due').value) || 0;
    const maxDue = parseFloat(document.getElementById('max-due').value) || Infinity;

    const filteredCars = allCars.filter(car => {
        const matchesSearch = car.model.toLowerCase().includes(searchQuery) || car.brand.toLowerCase().includes(searchQuery);
        const matchesBrand = selectedBrands.length === 0 || selectedBrands.includes(car.brand);
        const matchesPrice = car.monthlyPayment >= minPrice && car.monthlyPayment <= maxPrice;
        console.log(car.dueAtSigning)
        const matchesDue = car.dueAtSigning >= minDue && car.dueAtSigning <= maxDue;

        return matchesSearch && matchesBrand && matchesPrice && matchesDue;
    });

    console.log(filteredCars);
    displayCars(filteredCars);
}

// Navigate to the car details page
function viewCar(id) {
    window.location.href = `car.html?id=${id}`;
}

// Fetch details for a specific car (existing code)
function fetchCarDetails(carId) {
    fetch(`http://localhost:8080/api/v1/${carId}`)
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch car details.');
            return response.json();
        })
        .then(car => {
            const carDetails = document.getElementById('car-details');
            if (!carDetails) return;

            // Predefined mappings for user-friendly labels
            const fieldLabels = {
                msrp: "MSRP",
                monthlyPayment: "Monthly Payment",
                dueAtSigning: "Due at Signing",
                downPayment: "Down Payment",
                bankFee: "Bank Fee",
                totalPayments: "Total Payments",
                purchaseOption: "Purchase Option",
                terminationFee: "Termination Fee",
                excessMileFee: "Excess Mile Fee (per mile)",
                milesPerYear: "Miles Per Year",
                offerStarts: "Offer Starts",
                offerEnds: "Offer Ends",
                docFee: "Doc Fee",
                leaseTerm: "Lease Term (months)",
                leaseBonus: "Lease Bonus",
                drivetrain: "Drivetrain",
                trim: "Trim",
            };

            // Image section
            let detailsHtml = `
                <img src="${car.imageUrl}" alt="${car.model}" class="car-details-img" />
                <div class="car-details-text">
                    <h2>${car.model}</h2>
            `;

            // Dynamically add non-null fields
            for (const [key, value] of Object.entries(car)) {
                if (value !== null && fieldLabels[key]) {
                    if (
                        key === "msrp" ||
                        key === "monthlyPayment" ||
                        key === "dueAtSigning" ||
                        key === "downPayment" ||
                        key === "bankFee" ||
                        key === "totalPayments" ||
                        key === "purchaseOption" ||
                        key === "terminationFee" ||
                        key === "docFee"
                    ) {
                        detailsHtml += `<div><strong>${fieldLabels[key]}:</strong></div><div>$${value.toLocaleString()}</div>`;
                    } else if (key === "excessMileFee") {
                        detailsHtml += `<div><strong>${fieldLabels[key]}:</strong></div><div>$${value.toFixed(2)}</div>`;
                    } else if (key === "milesPerYear" || key === "leaseTerm" || key === "leaseBonus") {
                        detailsHtml += `<div><strong>${fieldLabels[key]}:</strong></div><div>${value.toLocaleString()}</div>`;
                    } else if (key === "offerStarts" || key === "offerEnds") {
                        detailsHtml += `<div><strong>${fieldLabels[key]}:</strong></div><div>${new Date(value).toLocaleDateString()}</div>`;
                    } else {
                        detailsHtml += `<div><strong>${fieldLabels[key]}:</strong></div><div>${value}</div>`;
                    }
                }
            }

            // Close the container
            detailsHtml += `</div>`;

            // Update the car details section
            carDetails.innerHTML = detailsHtml;
        })
        .catch(error => {
            console.error('Error fetching car details:', error);
            const carDetails = document.getElementById('car-details');
            if (carDetails) carDetails.innerHTML = `<p>Unable to load car details.</p>`;
        });
}

// Handle DOMContentLoaded event
document.addEventListener('DOMContentLoaded', () => {
    const currentPage = window.location.pathname;

    if (currentPage.endsWith('index.html') || currentPage === '/') {
        fetchCars();

        const searchBar = document.getElementById('search-bar');
        if (searchBar) {
            searchBar.addEventListener('input', filterCars);
        }

        const applyFiltersButton = document.getElementById('apply-filters');
        if (applyFiltersButton) {
            applyFiltersButton.addEventListener('click', filterCars);
        }
    }

    if (currentPage.endsWith('car.html')) {
        const urlParams = new URLSearchParams(window.location.search);
        const carId = urlParams.get('id');
        if (carId) {
            fetchCarDetails(carId);
        }
    }
});