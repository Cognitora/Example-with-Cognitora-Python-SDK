# Cognitora Python SDK Example

This repository demonstrates the basic usage of the Cognitora Python SDK for executing code with networking capabilities.

## Prerequisites

- Python 3.7 or higher
- `cognitora` package installed via pip

## API Keys

You'll need to obtain API keys for the Cognitora service:

- **Cognitora API Key**: Get from [Cognitora Dashboard](https://www.cognitora.dev/home/get-started)

## Environment Variables (Recommended)

For security, create a `.env` file in the project root:

```
COGNITORA_API_KEY=your_cognitora_api_key_here
```

## Installation

```bash
pip install cognitora python-dotenv
```

## Usage

1. Import the Cognitora client:
```python
from cognitora import Cognitora
```

2. Initialize the Cognitora client using one of these methods:

# Method 1: Pass API key directly
```python
from cognitora import Cognitora
client = Cognitora(api_key="cgk_1234567890abcdef")
```

# Method 2: Use environment variable (recommended)
```python
import os
from dotenv import load_dotenv
from cognitora import Cognitora

# Load environment variables from .env file
load_dotenv()

# Client will automatically use COGNITORA_API_KEY from environment
client = Cognitora()
```

# Method 3: With custom configuration
```python
from cognitora import Cognitora

client = Cognitora(
    api_key="your_api_key",
    base_url="https://api.cognitora.dev",  # Production default
    timeout=30
)
```

3. Execute code using the code interpreter:
```python
result = client.code_interpreter.execute(
    code="print('Hello from Cognitora!')",
    language="python",
    networking=True
)
```

4. Process the results:
```python
print(f"Status: {result.data.status}")
for output in result.data.outputs:
    print(f"{output.type}: {output.data}")
```

## Example Output

When running the example script, you should see output similar to:
```
Status: success
stdout: Hello from Cognitora!
```

## API Reference

### Cognitora Client
- `Cognitora(api_key=None, base_url="https://api.cognitora.dev", timeout=30)`: Initialize the client with optional parameters
  - `api_key` (str): Your Cognitora API key. If not provided, will look for COGNITORA_API_KEY environment variable
  - `base_url` (str): API endpoint URL (default: "https://api.cognitora.dev")
  - `timeout` (int): Request timeout in seconds (default: 30)

### Code Interpreter
- `execute(code, language, networking)`: Execute code in the specified language
  - `code` (str): The code to execute
  - `language` (str): The programming language (e.g., "python")
  - `networking` (bool): Whether to enable internet access (default: True)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
