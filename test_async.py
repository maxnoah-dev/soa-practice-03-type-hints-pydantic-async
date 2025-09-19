import asyncio
import time
from typing import List

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

async def demo_sync_vs_async():
    print("=== SYNCHRONOUS vs ASYNCHRONOUS DEMONSTRATION ===\n")
    
    # Synchronous version
    print("1. SYNCHRONOUS EXECUTION:")
    sync_start = time.time()
    sync_results = []
    for source, delay in [("SyncA", 1.0), ("SyncB", 1.0), ("SyncC", 1.0)]:
        print(f"{source}: Fetching...")
        time.sleep(delay)  # Blocking sleep
        print(f"{source}: Done!")
        sync_results.append(source)
    sync_end = time.time()
    
    print(f"\nSynchronous execution time: {sync_end - sync_start:.2f} seconds")
    print(f"Synchronous results: {sync_results}")
    
    # Asynchronous version
    print("\n2. ASYNCHRONOUS EXECUTION:")
    async_start = time.time()
    async_tasks = [
        fetch_data("AsyncA", 1.0),
        fetch_data("AsyncB", 1.0),
        fetch_data("AsyncC", 1.0)
    ]
    async_results = await asyncio.gather(*async_tasks)
    async_end = time.time()
    
    print(f"\nAsynchronous execution time: {async_end - async_start:.2f} seconds")
    print(f"Asynchronous results: {async_results}")
    
    improvement = (sync_end - sync_start) / (async_end - async_start)
    print(f"\n🚀 Performance improvement: {improvement:.1f}x faster!")

if __name__ == "__main__":
    print("=== ASYNC/AWAIT EXERCISE SOLUTION ===\n")
    
    print("Running the exercise example:")
    print("Expected Output:")
    print("SourceA: Fetching...")
    print("SourceB: Fetching...")
    print("SourceC: Fetching...")
    print("SourceB: Done!")
    print("SourceC: Done!")
    print("SourceA: Done!")
    print("['SourceA', 'SourceB', 'SourceC']")
    print("\nActual Output:")
    
    # Run the exercise example
    results = asyncio.run(main_concurrent_fetch())
    
    print("\n" + "="*60)
    
    # Run sync vs async comparison
    asyncio.run(demo_sync_vs_async())
    
    print("\n" + "="*60)
    print("KEY CONCEPTS DEMONSTRATED:")
    print("✅ async/await keywords")
    print("✅ asyncio.gather() for concurrent execution")
    print("✅ Non-blocking vs blocking operations")
    print("✅ Performance improvement with async programming")
    print("✅ Event loop and coroutines")
