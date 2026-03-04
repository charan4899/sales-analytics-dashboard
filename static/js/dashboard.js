document.addEventListener("DOMContentLoaded", function () {

    // Get selected region from URL
    const params = new URLSearchParams(window.location.search);
    const region = params.get("region");

    let url = "/api/monthly-data";
    if (region) {
        url += "?region=" + region;
    }

    fetch(url)
        .then(response => response.json())
        .then(result => {
            renderChart(result.data);
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });

});

function renderChart(monthlyData) {

    if (!monthlyData || monthlyData.length === 0) {
        document.getElementById('revenueChart').outerHTML =
            "<p style='text-align:center;color:white;'>No data available</p>";
        return;
    }

    const labels = monthlyData.map(item => item.month);
    const values = monthlyData.map(item => item.revenue);

    const ctx = document.getElementById('revenueChart').getContext('2d');

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Monthly Revenue',
                data: values,
                borderColor: '#38bdf8',
                backgroundColor: 'rgba(56,189,248,0.2)',
                borderWidth: 2,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}