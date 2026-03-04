// Global Chart Styling
Chart.defaults.color = "#94a3b8";
Chart.defaults.borderColor = "#334155";
Chart.defaults.font.family = "Segoe UI";

// Revenue by Region
fetch('/api/region-data')
    .then(res => res.json())
    .then(data => {

        const labels = data.data.map(item => item.region);
        const values = data.data.map(item => item.revenue);

        new Chart(document.getElementById('regionChart'), {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Revenue',
                    data: values,
                    borderRadius: 8,
                    backgroundColor: 'rgba(59, 130, 246, 0.7)',
                    borderColor: 'rgba(59, 130, 246, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: { color: "#1e293b" }
                    },
                    x: {
                        grid: { display: false }
                    }
                }
            }
        });
    });


// Top Products
fetch('/api/top-products')
    .then(res => res.json())
    .then(data => {

        const labels = data.data.map(item => item.product);
        const values = data.data.map(item => item.revenue);

        new Chart(document.getElementById('productChart'), {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Revenue',
                    data: values,
                    borderRadius: 8,
                    backgroundColor: 'rgba(16, 185, 129, 0.7)',
                    borderColor: 'rgba(16, 185, 129, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                indexAxis: 'y',  // horizontal bar (modern look)
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        grid: { color: "#1e293b" }
                    },
                    y: {
                        grid: { display: false }
                    }
                }
            }
        });
    });