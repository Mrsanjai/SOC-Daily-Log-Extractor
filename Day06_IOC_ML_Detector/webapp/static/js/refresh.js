// webapp/static/js/refresh.js

async function fetchAlerts() {
    try {
        const response = await fetch("/alerts");
        const alerts = await response.json();

        const tbody = document.getElementById("alert-body");
        tbody.innerHTML = "";

        alerts.forEach(alert => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${new Date(alert.timestamp).toLocaleString()}</td>
                <td>${alert.source}</td>
                <td>${alert.ioc}</td>
                <td>${alert.summary}</td>
                <td>${alert.mitre_tactic}</td>
                <td>${alert.mitre_technique}</td>
                <td class="severity-${alert.severity.toLowerCase()}">${alert.severity}</td>
            `;

            tbody.appendChild(row);
        });
    } catch (err) {
        console.error("Failed to fetch alerts:", err);
    }
}

setInterval(fetchAlerts, 3000);
window.onload = fetchAlerts;
