#!/usr/bin/env python3
"""
Quick test to verify uvicorn compatibility and server startup.
"""

import asyncio
import subprocess
import time
import httpx
import sys
from pathlib import Path


async def test_server_startup():
    """Test that the server starts correctly with uvicorn."""
    print("🧪 Testing DAVAI POC Server Startup")
    print("=" * 50)
    
    # Start server process
    print("1️⃣ Starting server with uvicorn...")
    
    # Change to backend directory
    backend_dir = Path(__file__).parent
    
    # Start uvicorn process
    process = subprocess.Popen(
        ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8001"],
        cwd=backend_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Wait a moment for server to start
    print("⏳ Waiting for server to start...")
    await asyncio.sleep(3)
    
    try:
        # Test health endpoint
        print("2️⃣ Testing health endpoint...")
        async with httpx.AsyncClient() as client:
            response = await client.get("http://127.0.0.1:8001/api/health", timeout=5.0)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Health check passed: {data.get('message', 'OK')}")
                
                # Test API docs
                print("3️⃣ Testing API documentation...")
                docs_response = await client.get("http://127.0.0.1:8001/docs", timeout=5.0)
                
                if docs_response.status_code == 200:
                    print("✅ API docs accessible")
                    print("🎉 Server startup test PASSED!")
                    result = True
                else:
                    print(f"❌ API docs not accessible: {docs_response.status_code}")
                    result = False
            else:
                print(f"❌ Health check failed: {response.status_code}")
                result = False
                
    except Exception as e:
        print(f"❌ Server test failed: {e}")
        result = False
    
    finally:
        # Stop server
        print("4️⃣ Stopping server...")
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
        
        print("✅ Server stopped")
    
    return result


async def main():
    """Run the server test."""
    try:
        success = await test_server_startup()
        
        if success:
            print("\n🎉 Uvicorn compatibility test PASSED!")
            print("\n🚀 Ready to start the server:")
            print("   uvicorn main:app --host 0.0.0.0 --port 8000 --reload")
            print("   ./start.sh")
            print("   python main.py")
        else:
            print("\n❌ Uvicorn compatibility test FAILED!")
            print("   Check the error messages above")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n👋 Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
