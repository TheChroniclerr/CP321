async function updatePlot() {
    const select = document.getElementById('metric-select');
    const metric_name = select.options[select.selectedIndex].text;;

    const country = document.getElementById('country-select').value;
    const metric = document.getElementById('metric-select').value;

    const response = await fetch(`/data?country=${country}&metric=${metric}`);
    const data = await response.json();

    const dates = data.map(d => d.date);
    const values = data.map(d => d.value);

    Plotly.react('plotly-div', [{
        x: dates,
        y: values,
        type: 'scatter',
        mode: 'lines+markers'
        // name: `${metric} in ${country}`
    }], {
        title: `${metric_name} in ${country}`,
        xaxis: {title: 'Date'},
        yaxis: {title: metric_name}
    }, {
        responsive: true
    });
}

window.onload = function () {
    // Initial plot
    updatePlot();

    // Event listeners
    document.getElementById('country-select').addEventListener('change', updatePlot);
    document.getElementById('metric-select').addEventListener('change', updatePlot);
}