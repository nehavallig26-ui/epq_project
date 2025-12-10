// charts.js: render drag/downforce graphs using Chart.js
function renderCharts(data) {
    if (!data || !data.speeds_kmh) return;
    const speeds = data.speeds_kmh;
    const drag = data.drag;
    const down = data.downforce;

    const ctx1 = document.getElementById("chartDrag");
    if (ctx1) {
        new Chart(ctx1, {
            type: 'line',
            data: {
                labels: speeds,
                datasets: [{ label: 'Drag (N)', data: drag, fill: false }]
            },
            options: { responsive: true, plugins: { legend: { display: true }}}
        });
    }

    const ctx2 = document.getElementById("chartDownforce");
    if (ctx2) {
        new Chart(ctx2, {
            type: 'line',
            data: {
                labels: speeds,
                datasets: [{ label: 'Downforce (N)', data: down, fill: false }]
            },
            options: { responsive: true, plugins: { legend: { display: true }}}
        });
    }
}

window.renderCharts = renderCharts;
