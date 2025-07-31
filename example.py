"""Cognitora Python SDK Example

This script demonstrates the basic usage of the Cognitora Python SDK for executing code with networking capabilities.

The example shows how to:
1. Initialize the Cognitora client using environment variables (recommended)
2. Execute Python code using the code interpreter
3. Process and display the results

Client initialization methods:
# Method 1: Pass API key directly
client = Cognitora(api_key="cgk_1234567890abcdef")

# Method 2: Use environment variable (recommended)
import os
os.environ['COGNITORA_API_KEY'] = 'cgk_1234567890abcdef'
client = Cognitora()  # Will use environment variable

# Method 3: With custom configuration
client = Cognitora(
    api_key="your_api_key",
    base_url="https://api.cognitora.dev",  # Production default
    timeout=30
)

For more information about the Cognitora Python SDK, visit:
https://pypi.org/project/cognitora/

Prerequisites:
- Install required packages: pip install cognitora python-dotenv
- Create a .env file with your API key:
  COGNITORA_API_KEY=your_cognitora_api_key_here
- Get your API key from: https://www.cognitora.dev/home/get-started
"""
import os
from dotenv import load_dotenv
from cognitora import Cognitora

# Load environment variables from .env file
load_dotenv()

# Initialize the client (will automatically use COGNITORA_API_KEY from environment)
client = Cognitora()

# Execute Python code with networking enabled
result = client.code_interpreter.execute(
    code="print('Hello from Cognitora!')",
    language="python",
    networking=True  # Enable internet access (default for code interpreter)
)

print(f"Status: {result.data.status}")
for output in result.data.outputs:
    print(f"{output.type}: {output.data}")
