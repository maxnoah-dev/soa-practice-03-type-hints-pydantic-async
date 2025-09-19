from fastapi import FastAPI, HTTPException
from typing import List, TypeVar, Callable, Union
from pydantic import BaseModel, EmailStr, ValidationError
import asyncio
import time

app = FastAPI(title="Type Hints Exercise API", version="1.0.0")

T = TypeVar('T')
R = TypeVar('R')

class WordListRequest(BaseModel):
    words: List[str]

class NumberListRequest(BaseModel):
    numbers: List[Union[int, float]]

class OperationRequest(BaseModel):
    numbers: List[Union[int, float]]
    operation: str

# Q1: Person model
class Person(BaseModel):
    name: str
    age: int

# Q2: Product model
class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# Q3: Nested models
class Author(BaseModel):
    name: str
    email: str

class BlogPost(BaseModel):
    title: str
    content: str
    author: Author

# Async/Concurrency Models
class FetchDataRequest(BaseModel):
    source_name: str
    delay: float

class ConcurrentFetchRequest(BaseModel):
    tasks: List[FetchDataRequest]

def capitalize_words(words: List[str]) -> List[str]:
    return [word.capitalize() for word in words]

def apply_operation(numbers: List[T], operation: Callable[[T], R]) -> List[R]:
    return [operation(num) for num in numbers]

# Async/Concurrency Functions
async def fetch_data(source_name: str, delay: float) -> str:
    print(f"{source_name}: Fetching...")
    await asyncio.sleep(delay)
    print(f"{source_name}: Done!")
    return source_name

async def main_concurrent_fetch():
    tasks = [
        fetch_data("SourceA", 2.0),
        fetch_data("SourceB", 1.0),
        fetch_data("SourceC", 1.5)
    ]
    
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")
    return results

@app.get("/")
async def root():
    return {"message": "Type Hints Exercise API"}

@app.post("/capitalize-words")
async def capitalize_words_endpoint(request: WordListRequest):
    result = capitalize_words(request.words)
    return {"input": request.words, "result": result}

@app.post("/apply-operation")
async def apply_operation_endpoint(request: OperationRequest):
    def square(x: float) -> float:
        return x * x
    
    def double(x: float) -> float:
        return x * 2
    
    def cube(x: float) -> float:
        return x * x * x
    
    operations = {
        "square": square,
        "double": double,
        "cube": cube
    }
    
    if request.operation not in operations:
        return {"error": "Operation not supported. Available: square, double, cube"}
    
    result = apply_operation(request.numbers, operations[request.operation])
    return {"input": request.numbers, "operation": request.operation, "result": result}

@app.get("/test-examples")
async def test_examples():
    words = ["apple", "banana", "cherry"]
    capitalized = capitalize_words(words)
    
    def square(x: float) -> float:
        return x * x
    
    numbers = [1.5, 2.0, 3.5]
    squared = apply_operation(numbers, square)
    
    return {
        "capitalize_words_example": {
            "input": words,
            "result": capitalized
        },
        "apply_operation_example": {
            "input": numbers,
            "operation": "square",
            "result": squared
        }
    }

# Q1: Person endpoint
@app.post("/person")
async def create_person(person: Person):
    return {
        "message": "Person created successfully",
        "person_dict": person.dict(),
        "person_model": person
    }

# Q2: Product endpoints
@app.post("/product")
async def create_product(product: Product):
    return {
        "message": "Product created successfully",
        "product_dict": product.dict(),
        "product_model": product
    }

@app.post("/products/batch")
async def create_products_batch(products: List[Product]):
    return {
        "message": "Products created successfully",
        "products": [product.dict() for product in products]
    }

# Q3: BlogPost endpoints
@app.post("/blogpost")
async def create_blogpost(blogpost: BlogPost):
    return {
        "message": "Blog post created successfully",
        "blogpost_dict": blogpost.dict(),
        "blogpost_model": blogpost
    }

@app.get("/pydantic-examples")
async def pydantic_examples():
    # Q1: Person example
    person = Person(name="Alice", age=30)
    
    # Q2: Product examples
    item1 = Product(name="Laptop", price=1299.99)
    item2 = Product(name="Phone", price=999.99, in_stock=False)
    
    # Q3: BlogPost example
    data = {
        'title': 'My First Post',
        'content': 'Hello, Pydantic!',
        'author': {
            'name': 'Bob',
            'email': 'bob@example.com'
        }
    }
    post = BlogPost(**data)
    
    return {
        "q1_person_example": {
            "description": "Person model with name and age",
            "person_dict": person.dict(),
            "person_model": person
        },
        "q2_product_examples": {
            "description": "Product models with type conversion and default values",
            "item1": {
                "input": {"name": "Laptop", "price": 1299.99},
                "result": item1.dict()
            },
            "item2": {
                "input": {"name": "Phone", "price": "999.99", "in_stock": False},
                "result": item2.dict()
            }
        },
        "q3_blogpost_example": {
            "description": "Nested models - BlogPost with Author",
            "input_data": data,
            "result": post.dict()
        }
    }

@app.post("/test-validation")
async def test_validation():
    try:
        # Test invalid email
        invalid_data = {
            'title': 'Test Post',
            'content': 'Testing validation',
            'author': {
                'name': 'Invalid User',
                'email': 'invalid-email'  # Invalid email format
            }
        }
        post = BlogPost(**invalid_data)
        return {"message": "Validation passed", "data": post.dict()}
    except ValidationError as e:
        return {
            "message": "Validation failed as expected",
            "error": str(e),
            "error_details": e.errors()
        }

# Async/Concurrency Endpoints
@app.get("/async-demo")
async def async_demo():
    start_time = time.time()
    results = await main_concurrent_fetch()
    end_time = time.time()
    
    return {
        "message": "Async concurrent execution completed",
        "results": results,
        "execution_time": f"{end_time - start_time:.2f} seconds",
        "note": "Check console output for detailed execution flow"
    }

@app.post("/fetch-single")
async def fetch_single_data(request: FetchDataRequest):
    start_time = time.time()
    result = await fetch_data(request.source_name, request.delay)
    end_time = time.time()
    
    return {
        "message": "Single async fetch completed",
        "source_name": result,
        "delay": request.delay,
        "execution_time": f"{end_time - start_time:.2f} seconds"
    }

@app.post("/fetch-concurrent")
async def fetch_concurrent_data(request: ConcurrentFetchRequest):
    start_time = time.time()
    
    # Create tasks from request
    tasks = [fetch_data(task.source_name, task.delay) for task in request.tasks]
    
    # Execute concurrently
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    
    return {
        "message": "Concurrent async fetch completed",
        "results": results,
        "total_tasks": len(request.tasks),
        "execution_time": f"{end_time - start_time:.2f} seconds",
        "note": "Check console output for detailed execution flow"
    }

@app.get("/sync-vs-async-demo")
async def sync_vs_async_demo():
    # Synchronous version (simulated)
    sync_start = time.time()
    sync_results = []
    for source, delay in [("SyncA", 1.0), ("SyncB", 1.0), ("SyncC", 1.0)]:
        print(f"{source}: Fetching...")
        time.sleep(delay)  # Blocking sleep
        print(f"{source}: Done!")
        sync_results.append(source)
    sync_end = time.time()
    
    # Asynchronous version
    async_start = time.time()
    async_tasks = [
        fetch_data("AsyncA", 1.0),
        fetch_data("AsyncB", 1.0),
        fetch_data("AsyncC", 1.0)
    ]
    async_results = await asyncio.gather(*async_tasks)
    async_end = time.time()
    
    return {
        "synchronous": {
            "results": sync_results,
            "execution_time": f"{sync_end - sync_start:.2f} seconds",
            "description": "Sequential execution - each task waits for previous"
        },
        "asynchronous": {
            "results": async_results,
            "execution_time": f"{async_end - async_start:.2f} seconds",
            "description": "Concurrent execution - tasks run simultaneously"
        },
        "performance_improvement": f"{((sync_end - sync_start) / (async_end - async_start)):.1f}x faster"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
