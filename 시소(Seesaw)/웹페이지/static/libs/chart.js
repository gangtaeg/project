document.addEventListener('DOMContentLoaded', function() {
  const ctx = document.getElementById('priceChart').getContext('2d');

  const priceData = {
      labels: ['1시', '2시', '3시', '4시', '5시', '6시'],
      datasets: [{
          label: '물건 시세 변동',
          data: [100, 120, 90, 115, 130, 140],
          borderColor: 'rgba(54, 162, 235, 1)',
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          fill: true,
          tension: 0.1
      }]
  };

  const config = {
      type: 'line',
      data: priceData,
      options: {
          responsive: true,
          plugins: {
              legend: { position: 'top' },
              tooltip: { enabled: true }
          },
          scales: {
              x: { beginAtZero: true },
              y: { beginAtZero: true }
          }
      }
  };

  const priceChart = new Chart(ctx, config);

  document.getElementById('loadDataBtn').addEventListener('click', function() {
      priceChart.update();
  });
});