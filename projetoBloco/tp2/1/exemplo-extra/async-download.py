import asyncio
import aiohttp
import time
import requests
from typing import List

urls = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/photos",
    "https://jsonplaceholder.typicode.com/todos",
    "https://jsonplaceholder.typicode.com/users"
]


def download_sync(urls: List[str]) -> List[str]:
    results = []
    start_time = time.time()

    for url in urls:
        try:
            response = requests.get(url)
            results.append(f"Downloaded {url} - Status: {response.status_code}")
        except Exception as e:
            results.append(f"Error downloading {url}: {str(e)}")

    end_time = time.time()
    print(f"Tempo total síncrono: {end_time - start_time:.2f} segundos")
    return results


async def download_url(session: aiohttp.ClientSession, url: str) -> str:
    try:
        async with session.get(url) as response:
            content = await response.text()
            return f"Downloaded {url} - Status: {response.status}"
    except Exception as e:
        return f"Error downloading {url}: {str(e)}"


async def download_async(urls: List[str], max_concurrent: int = 4) -> List[str]:
    start_time = time.time()

    connector = aiohttp.TCPConnector(limit=max_concurrent)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [download_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Tempo total assíncrono (max {max_concurrent} conexões): {end_time - start_time:.2f} segundos")
    return results


def run_comparison(urls: List[str]):
    print("\n=== Download Síncrono ===")
    sync_results = download_sync(urls)
    for result in sync_results:
        print(result)

    concurrent_limits = [2,3, 4, 8]  # Variando o número de downloads simultâneos

    for limit in concurrent_limits:
        print(f"\n=== Download Assíncrono (máximo {limit} simultâneos) ===")
        async_results = asyncio.run(download_async(urls, limit))
        for result in async_results:
            print(result)


if __name__ == "__main__":
    print("Iniciando comparações de download...")
    run_comparison(urls)