# Bài Tập Type Hints, Pydantic & Async/Concurrency - FastAPI

Dự án này thực hiện các bài tập về Type Hints, Pydantic Models và Async/Concurrency sử dụng FastAPI với type hints phù hợp.

## Mục Lục
1. [Các Function đã thực hiện](#các-function-đã-thực-hiện)
2. [Pydantic Models](#pydantic-models)
3. [Async/Concurrency Functions](#asyncconcurrency-functions)
4. [API Endpoints](#api-endpoints)
5. [Cài đặt và chạy](#cài-đặt-và-chạy)
6. [Cách test](#cách-test)
7. [Kết quả đạt được](#kết-quả-đạt-được)

## Các Function đã thực hiện

### 1. `capitalize_words`
- **Mục đích**: Nhận một danh sách strings và trả về danh sách mới với mỗi string được viết hoa chữ cái đầu
- **Type Hints**: `List[str] -> List[str]`
- **Ví dụ**: `["apple", "banana", "cherry"]` → `["Apple", "Banana", "Cherry"]`

### 2. `apply_operation`
- **Mục đích**: Áp dụng một operation cho mọi phần tử trong danh sách
- **Type Hints**: Sử dụng `TypeVar` và `Callable` cho type hints chính xác
- **Ví dụ**: `[1.5, 2.0, 3.5]` với square operation → `[2.25, 4.0, 12.25]`

## Pydantic Models

### 1. `Person` Model
- **Fields**: `name: str`, `age: int`
- **Mục đích**: Model cơ bản với string và integer fields
- **Ví dụ**: `Person(name="Alice", age=30)`

### 2. `Product` Model
- **Fields**: `name: str`, `price: float`, `in_stock: bool = True`
- **Mục đích**: Model với default values và type conversion
- **Ví dụ**: `Product(name="Laptop", price=1299.99)`

### 3. `Author` & `BlogPost` Models (Nested)
- **Author**: `name: str`, `email: str`
- **BlogPost**: `title: str`, `content: str`, `author: Author`
- **Mục đích**: Thể hiện nested models và validation

## Async/Concurrency Functions

### 1. `fetch_data`
- **Mục đích**: Async function mô phỏng việc fetch data với delay
- **Parameters**: `source_name: str`, `delay: float`
- **Returns**: `str` (source name)
- **Tính năng**: Non-blocking sleep, concurrent execution

### 2. `main_concurrent_fetch`
- **Mục đích**: Thể hiện concurrent execution sử dụng `asyncio.gather`
- **Tính năng**: Chạy nhiều `fetch_data` tasks đồng thời
- **Hiệu suất**: Cho thấy cải thiện 3x so với synchronous execution

## API Endpoints

### Type Hints Functions
- `GET /` - Root endpoint
- `GET /test-examples` - Test cả hai functions với examples
- `POST /capitalize-words` - Capitalize words endpoint
- `POST /apply-operation` - Apply operation endpoint

### Pydantic Models
- `GET /pydantic-examples` - Test tất cả Pydantic models với examples
- `POST /person` - Tạo Person instance
- `POST /product` - Tạo Product instance
- `POST /products/batch` - Tạo nhiều Product instances
- `POST /blogpost` - Tạo BlogPost với nested Author
- `POST /test-validation` - Test validation error handling

### Async/Concurrency
- `GET /async-demo` - Demo concurrent async execution
- `POST /fetch-single` - Test single async fetch
- `POST /fetch-concurrent` - Test multiple concurrent fetches
- `GET /sync-vs-async-demo` - So sánh sync vs async performance

## Cài đặt và chạy

### 1. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 2. Chạy FastAPI server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Chạy standalone async demo
```bash
python test_async.py
```

## Cách test

### 1. Test Type Hints Functions
Server có test endpoints thể hiện cả hai functions hoạt động với examples chính xác:

- **capitalize_words**: `["apple", "banana", "cherry"]` → `["Apple", "Banana", "Cherry"]`
- **apply_operation**: `[1.5, 2.0, 3.5]` với square → `[2.25, 4.0, 12.25]`

Truy cập `http://localhost:8000/test-examples` để xem kết quả.

### 2. Test Pydantic Models
Test tất cả Pydantic models với examples:

- **Person**: `Person(name="Alice", age=30)` → `{'name': 'Alice', 'age': 30}`
- **Product**: Type conversion và default values
  - `Product(name="Laptop", price=1299.99)` → `{'name': 'Laptop', 'price': 1299.99, 'in_stock': True}`
  - `Product(name="Phone", price="999.99", in_stock=False)` → `{'name': 'Phone', 'price': 999.99, 'in_stock': False}`
- **BlogPost**: Nested models với Author
  - `BlogPost(**data)` với data chứa nested author information

Truy cập `http://localhost:8000/pydantic-examples` để xem tất cả examples.

### 3. Test Async/Concurrency Demo
Test async functions với standalone script:

```bash
python test_async.py
```

Kết quả mong đợi thể hiện:
- **Concurrent execution**: Tất cả tasks bắt đầu đồng thời
- **Non-blocking operations**: Tasks không chờ nhau
- **Performance improvement**: Nhanh hơn 3x so với synchronous execution

## Kết quả đạt được

### 1. Type Hints
- Sử dụng đúng `List`, `TypeVar`, `Callable`, và `Union`
- Type hints chính xác cho function arguments và return types
- Generic types với TypeVar cho flexibility

### 2. Pydantic Models
- Basic models với string và integer fields
- Default values và type conversion
- Nested models với validation
- Error handling cho validation

### 3. Async/Concurrency
- `async/await` keywords
- `asyncio.gather()` cho concurrent execution
- Non-blocking vs blocking operations
- Event loop và coroutines
- Performance improvement với async programming

### 4. API Integration
- FastAPI endpoints với automatic validation
- Pydantic models integration
- Error handling demonstration
- Interactive API documentation tại `http://localhost:8000/docs`

### 5. Performance Results
- **Synchronous execution**: 3.00 giây (tuần tự)
- **Asynchronous execution**: 1.01 giây (đồng thời)
- **Cải thiện hiệu suất**: **3.0x nhanh hơn!**

## Cấu trúc Project

```
SOA_Practice_03_521H0476/
├── main.py              # FastAPI application chính
├── test_async.py        # Standalone async demo script
├── requirements.txt     # Dependencies
└── README.md           # Documentation này
```

## Tóm tắt

Dự án này hoàn thành tất cả các yêu cầu bài tập:
1. **Type Hints**: Functions với type hints chính xác
2. **Pydantic Models**: Basic, nested, và validation models
3. **Async/Concurrency**: Concurrent execution với performance improvement
4. **FastAPI Integration**: API endpoints với automatic validation
5. **Testing**: Comprehensive testing với examples và performance comparison

Tất cả code đều clean, follow best practices, và có documentation đầy đủ bằng tiếng Việt.