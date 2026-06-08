# localStorage와 배열 메서드 가이드

## 1. 배열 메서드 (Array Methods)

### find() - 조건에 맞는 첫 번째 요소 찾기

```javascript
const products = [
  { id: 1, name: "노트북", price: 1200000 },
  { id: 2, name: "마우스", price: 30000 },
  { id: 3, name: "키보드", price: 80000 },
];

// id가 2인 상품 찾기
const product = products.find((p) => p.id === 2);
console.log(product); // { id: 2, name: "마우스", price: 30000 }
```

### filter() - 조건에 맞는 모든 요소 필터링

```javascript
// 가격이 50,000 미만인 상품 찾기
const cheapProducts = products.filter((p) => p.price < 50000);
console.log(cheapProducts); // [ { id: 2, name: "마우스", price: 30000 } ]
```

### map() - 배열의 각 요소를 변환

```javascript
// 상품 이름만 추출
const names = products.map((p) => p.name);
console.log(names); // ["노트북", "마우스", "키보드"]
```

---

## 2. localStorage 기초

### localStorage란?

- 브라우저에 데이터를 로컬에 저장하는 웹 저장소
- 도메인별로 약 5-10MB 저장 가능
- 브라우저를 닫아도 데이터가 유지됨
- 동기적으로 동작 (느릴 수 있음)

### localStorage 저장하기

```javascript
// 객체나 배열은 JSON 형식으로 변환하여 저장
const products = [...];
localStorage.setItem('products', JSON.stringify(products));
```

### localStorage 불러오기

```javascript
// 저장된 데이터를 가져오고 JSON으로 파싱
const savedProducts = JSON.parse(localStorage.getItem("products"));
```

### localStorage 삭제하기

```javascript
// 특정 키 삭제
localStorage.removeItem("products");

// 전체 삭제
localStorage.clear();
```

---

## 3. 실제 예제

### 상품 정보를 localStorage에 저장하고 불러오기

```javascript
// 저장
function saveProducts() {
  const products = [
    { id: 1, name: "노트북", price: 1200000 },
    { id: 2, name: "마우스", price: 30000 },
    { id: 3, name: "키보드", price: 80000 },
  ];

  localStorage.setItem("products", JSON.stringify(products));
  console.log("상품 목록이 저장되었습니다!");
}

// 불러오기
function loadProducts() {
  const savedData = localStorage.getItem("products");

  if (savedData) {
    const products = JSON.parse(savedData);
    console.log("저장된 상품 목록:", products);
    return products;
  } else {
    console.log("저장된 상품 목록이 없습니다.");
    return [];
  }
}

// 검색 (저장된 데이터에서)
function findSavedProduct(id) {
  const products = loadProducts();
  return products.find((p) => p.id === id);
}

// 가격 필터 (저장된 데이터에서)
function filterBySavedPrice(maxPrice) {
  const products = loadProducts();
  return products.filter((p) => p.price < maxPrice);
}
```

---

## 4. 브라우저 개발자 도구에서 확인하기

1. F12 또는 우클릭 → 검사 (Inspect) 열기
2. Application 탭 (또는 Storage 탭)
3. 좌측 Storage 섹션에서 "Local Storage" 선택
4. 현재 사이트 클릭
5. 저장된 데이터 확인 가능

---

## 5. localStorage의 장점과 단점

### 장점 ✓

- 브라우저를 닫아도 데이터 유지
- 별도의 서버 없이 클라이언트에서 처리
- 사용하기 간단

### 단점 ✗

- 도메인당 약 5-10MB 제한
- 보안에 민감한 데이터 저장 불가 (누구나 접근 가능)
- 동기적으로 동작하여 대량 데이터 처리 시 느림
- 서버와의 동기화 불가 (클라이언트 로컬에만 저장)
