// script.js

document.addEventListener("DOMContentLoaded", function() {
    // 샘플 데이터 (실제 서버에서 가져올 데이터)
    fetch('sample-data.json')  // 샘플 데이터 파일 로딩
        .then(response => response.json())
        .then(data => {
            // 거래 내역을 테이블에 표시
            const tableBody = document.querySelector('#transaction-table tbody');
            data.transactions.forEach(transaction => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${transaction.id}</td>
                    <td>${transaction.date}</td>
                    <td>${transaction.buyer}</td>
                    <td>${transaction.seller}</td>
                    <td>$${transaction.amount}</td>
                    <td>${transaction.status}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error loading the data:', error));

    console.log('Page initialized and event listeners set up.');
});