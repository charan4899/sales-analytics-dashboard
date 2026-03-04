let currentPage = 1;
let totalPages = 1;

document.addEventListener("DOMContentLoaded", function () {
    loadPage(currentPage);
});

function loadPage(page) {

    fetch(`/api/reports?page=${page}`)
        .then(response => response.json())
        .then(result => {

            const tbody = document.querySelector("#salesTable tbody");
            tbody.innerHTML = "";

            result.data.forEach(row => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${row.product_name}</td>
                    <td>${row.region}</td>
                    <td>$${row.revenue}</td>
                    <td>${row.month}</td>
                `;
                tbody.appendChild(tr);
            });

            currentPage = result.page;
            totalPages = result.total_pages;

            document.getElementById("pageInfo").innerText =
                `Page ${currentPage} of ${totalPages}`;

        })
        .catch(error => {
            console.error("Error loading reports:", error);
        });
}

function nextPage() {
    if (currentPage < totalPages) {
        loadPage(currentPage + 1);
    }
}

function prevPage() {
    if (currentPage > 1) {
        loadPage(currentPage - 1);
    }
}