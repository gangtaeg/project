// app.js

document.addEventListener("DOMContentLoaded", function() {
  // 카드 애니메이션 추가
  const cards = document.querySelectorAll('.card');
  cards.forEach((card, index) => {
      card.style.opacity = 0;
      card.style.transform = "translateY(20px)";
      setTimeout(() => {
          card.style.transition = "all 0.5s ease-out";
          card.style.opacity = 1;
          card.style.transform = "translateY(0)";
      }, index * 100);  // 각 카드가 순차적으로 나타나도록 설정
  });

  // 실시간 시세 그래프 업데이트
  const ctx = document.getElementById('price-chart').getContext('2d');
  const priceData = {
      labels: ['9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM'],
      datasets: [{
          label: 'Price (USD)',
          data: [100, 110, 120, 130, 125, 135, 140, 150],
          borderColor: '#007bff',
          backgroundColor: 'rgba(0, 123, 255, 0.2)',
          tension: 0.2,
          fill: true,
      }]
  };

  const config = {
      type: 'line',
      data: priceData,
      options: {
          responsive: true,
          plugins: {
              legend: {
                  position: 'top',
              },
              tooltip: {
                  enabled: true,
              }
          },
          scales: {
              x: {
                  title: {
                      display: true,
                      text: 'Time'
                  }
              },
              y: {
                  title: {
                      display: true,
                      text: 'Price (USD)'
                  },
                  beginAtZero: false
              }
          }
      }
  };

  const priceChart = new Chart(ctx, config);

  // 실시간 시세 데이터 업데이트 (10초마다)
  setInterval(() => {
      fetch('sample-data.json')  // 샘플 데이터 로딩
          .then(response => response.json())
          .then(data => {
              const newPrice = data.latestPrice;
              const newTime = new Date().toLocaleTimeString().slice(0, 5);

              priceChart.data.labels.push(newTime);
              priceChart.data.datasets[0].data.push(newPrice);

              if (priceChart.data.labels.length > 5) {
                  priceChart.data.labels.shift();
                  priceChart.data.datasets[0].data.shift();
              }

              priceChart.update();
          })
          .catch(error => console.error('Error fetching data:', error));
  }, 10000); // 10초마다 시세 업데이트

});