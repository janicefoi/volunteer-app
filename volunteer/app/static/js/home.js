const ctx = document.getElementById('hoursChart').getContext('2d');
const hoursChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Volunteering hours', 'Events', 'Donations'],
        datasets: [{
            data: [20, 6, 10], // Example data, replace with your actual data
            backgroundColor: ['#4e73df', '#e74a3b', '#f6c23e', '#36b9cc', '#1cc88a'],
            hoverBackgroundColor: ['#2e59d9', '#e02d1b', '#d4af37', '#17a2b8', '#17a673'],
            hoverBorderColor: "rgba(234, 236, 244, 1)",
        }],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        cutoutPercentage: 75,
        legend: {
            position: 'right',
            labels: {
                boxWidth: 20,
                padding: 15,
            },
        },
        tooltips: {
            callbacks: {
                label: function(tooltipItem, data) {
                    var dataset = data.datasets[tooltipItem.datasetIndex];
                    var total = dataset.data.reduce(function(previousValue, currentValue) {
                        return previousValue + currentValue;
                    });
                    var currentValue = dataset.data[tooltipItem.index];
                    var percentage = Math.floor(((currentValue / total) * 100) + 0.5);
                    return currentValue + ' hours (' + percentage + '%)';
                }
            }
        }
    }
});
