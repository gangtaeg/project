document.addEventListener("DOMContentLoaded", function() {
    // 샘플 데이터 (실제 서버에서 가져올 데이터)
    const sampleData = {
        "latestPrice": 145,
        "transactions": [
            {
                "id": 1,
                "date": "2025-01-01",
                "buyer": "UserA",
                "seller": "UserB",
                "amount": 100,
                "status": "완료"
            },
            {
                "id": 2,
                "date": "2025-01-02",
                "buyer": "UserC",
                "seller": "UserD",
                "amount": 50,
                "status": "대기"
            },
            {
                "id": 3,
                "date": "2025-01-03",
                "buyer": "UserE",
                "seller": "UserF",
                "amount": 200,
                "status": "완료"
            }
        ]
    };

    // 최신 시세 업데이트
    const priceValue = document.querySelector('#price-value');
    priceValue.textContent = `₩${sampleData.latestPrice}`;

    // 거래 내역을 테이블에 표시
    const tableBody = document.querySelector('#transaction-table tbody');
    sampleData.transactions.forEach(transaction => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${transaction.id}</td>
            <td>${transaction.date}</td>
            <td>${transaction.buyer}</td>
            <td>${transaction.seller}</td>
            <td>₩${transaction.amount}</td>
            <td>${transaction.status}</td>
        `;
        tableBody.appendChild(row);
    });

    console.log('페이지 초기화 완료!');
});