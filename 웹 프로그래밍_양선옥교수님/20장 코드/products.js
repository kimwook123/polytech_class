// 상품 데이터
const products = [
    { id: 1, name: "노트북", price: 1200000 },
    { id: 2, name: "마우스", price: 30000 },
    { id: 3, name: "키보드", price: 80000 }
];

// 1. id가 2인 상품 찾기
function findProductById(id) {
    const result = products.find(product => product.id === id);
    const resultDiv = document.getElementById('result1');
    
    if (result) {
        resultDiv.innerHTML = `
            <pre>${JSON.stringify(result, null, 2)}</pre>
            <p><strong>설명:</strong> find() 메서드를 사용하여 id가 ${id}인 첫 번째 상품을 찾았습니다.</p>
        `;
    } else {
        resultDiv.innerHTML = `<p>id가 ${id}인 상품을 찾을 수 없습니다.</p>`;
    }
}

// 2. 가격이 50,000 이상인 상품 찾기
function findProductsByPrice(minPrice) {
    const result = products.filter(product => product.price >= minPrice);
    const resultDiv = document.getElementById('result2');
    
    if (result.length > 0) {
        let html = `<p><strong>가격이 ${minPrice.toLocaleString()}원 이상인 상품:</strong></p>`;
        html += '<table>';
        html += '<tr><th>ID</th><th>이름</th><th>가격</th></tr>';
        result.forEach(product => {
            html += `<tr><td>${product.id}</td><td>${product.name}</td><td>${product.price.toLocaleString()}원</td></tr>`;
        });
        html += '</table>';
        html += `<p><strong>설명:</strong> filter() 메서드를 사용하여 가격이 ${minPrice.toLocaleString()}원 이상인 상품들을 필터링했습니다.</p>`;
        resultDiv.innerHTML = html;
    } else {
        resultDiv.innerHTML = `<p>가격이 ${minPrice.toLocaleString()}원 이상인 상품이 없습니다.</p>`;
    }
}

// 3. 상품 이름 목록
function displayProductNames() {
    const names = products.map(product => product.name);
    const resultDiv = document.getElementById('result3');
    
    let html = '<p><strong>상품 이름 배열:</strong></p>';
    html += `<pre>${JSON.stringify(names, null, 2)}</pre>`;
    html += '<p><strong>설명:</strong> map() 메서드를 사용하여 모든 상품의 이름만 추출하여 새로운 배열을 만들었습니다.</p>';
    resultDiv.innerHTML = html;
}

// 4. localStorage에 저장하기
function saveToLocalStorage() {
    try {
        localStorage.setItem('products', JSON.stringify(products));
        const resultDiv = document.getElementById('result4');
        resultDiv.innerHTML = `
            <p><strong style="color: green;">✓ 저장 완료!</strong></p>
            <p>상품 목록이 localStorage에 저장되었습니다.</p>
            <p><strong>저장된 데이터:</strong></p>
            <pre>${JSON.stringify(JSON.parse(localStorage.getItem('products')), null, 2)}</pre>
        `;
    } catch (error) {
        document.getElementById('result4').innerHTML = `<p style="color: red;">오류: ${error.message}</p>`;
    }
}

// 5. localStorage에서 불러오기
function loadFromLocalStorage() {
    try {
        const storedData = localStorage.getItem('products');
        const resultDiv = document.getElementById('result5');
        
        if (storedData) {
            const loadedProducts = JSON.parse(storedData);
            let html = `<p><strong>localStorage에서 불러온 데이터:</strong></p>`;
            html += '<table>';
            html += '<tr><th>ID</th><th>이름</th><th>가격</th></tr>';
            loadedProducts.forEach(product => {
                html += `<tr><td>${product.id}</td><td>${product.name}</td><td>${product.price.toLocaleString()}원</td></tr>`;
            });
            html += '</table>';
            resultDiv.innerHTML = html;
        } else {
            resultDiv.innerHTML = `<p>저장된 상품 목록이 없습니다. 먼저 저장해주세요.</p>`;
        }
    } catch (error) {
        document.getElementById('result5').innerHTML = `<p style="color: red;">오류: ${error.message}</p>`;
    }
}

// 전체 상품 목록 표시
function displayAllProducts() {
    const resultDiv = document.getElementById('resultAll');
    
    let html = '<table>';
    html += '<tr><th>ID</th><th>이름</th><th>가격</th></tr>';
    products.forEach(product => {
        html += `<tr><td>${product.id}</td><td>${product.name}</td><td>${product.price.toLocaleString()}원</td></tr>`;
    });
    html += '</table>';
    
    resultDiv.innerHTML = html;
}
