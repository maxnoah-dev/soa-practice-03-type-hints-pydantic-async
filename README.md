# SOA Practice 03 - Type Hints, Pydantic & Async

Bài tập thực hiện Type Hints, Pydantic Models và Async/Concurrency sử dụng FastAPI.

## Yêu cầu bài tập

### 1. Type Hints Functions
- `capitalize_words`: Viết hoa chữ cái đầu của list strings
- `apply_operation`: Áp dụng function cho mọi phần tử trong list

### 2. Pydantic Models
- `Person`: name (str), age (int)
- `Product`: name (str), price (float), in_stock (bool = True)
- `Author` & `BlogPost`: Nested models

### 3. Async/Concurrency
- `fetch_data`: Async function với delay
- `main_concurrent_fetch`: Chạy nhiều tasks đồng thời

## Cài đặt và chạy

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Test

### API Endpoints
- `GET /test-examples` - Test type hints functions
- `GET /pydantic-examples` - Test pydantic models
- `GET /async-demo` - Test async functions

### Standalone Demo
```bash
python test_async.py
```

## Kết quả

- **Type Hints**: Sử dụng đúng List, TypeVar, Callable, Union
- **Pydantic**: Basic models, default values, nested models, validation
- **Async**: async/await, asyncio.gather(), concurrent execution
- **Performance**: Async nhanh hơn 3x so với sync (3.00s → 1.01s)

## Files

- `main.py` - FastAPI app
- `test_async.py` - Async demo
- `requirements.txt` - Dependencies