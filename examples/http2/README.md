# HTTP/2 Examples

This directory contains examples demonstrating HTTP/2 support in FastHTTP.

## What is HTTP/2?

HTTP/2 is a major revision of the HTTP protocol that provides:
- **Multiplexing** - Multiple requests can be sent over a single connection
- **Header compression** - Reduces overhead
- **Server push** - Server can proactively send resources
- **Better performance** - Reduced latency for multiple requests

## Enabling HTTP/2

Simply set `http2=True` when creating the FastHTTP app:

```python
from fasthttp import FastHTTP

app = FastHTTP(http2=True)
```

## Installation

For HTTP/2 support, install with the http2 extra:

```bash
pip install fasthttp-client[http2]
```

## Examples

### HTTP/2 Example (`http2_example.py`)
Demonstrates HTTP/2 requests to servers that support it (Google, GitHub).

**Run:**
```bash
python http2_example.py
```

## Important Notes

1. **Server Support**: The target server must support HTTP/2
2. **Fallback**: If a server doesn't support HTTP/2, httpx will automatically fall back to HTTP/1.1
3. **Transparent**: The fallback is automatic and transparent - no code changes needed

## Common HTTP/2 Servers

### Servers that support HTTP/2:
- **Google** - https://www.google.com
- **GitHub** - https://github.com
- **YouTube** - https://www.youtube.com
- **Twitter/X** - https://twitter.com

### Servers that typically use HTTP/1.1:
- **httpbin.org** - https://httpbin.org
- Many older websites
- Some API services

## How to Verify HTTP/2

When HTTP/2 is enabled, you'll see this in your logs:

```
INFO │ fasthttp │ ✔ HTTP/2 enabled
```

httpx will automatically use HTTP/2 for servers that support it and fall back to HTTP/1.1 for servers that don't. The behavior is transparent.

---

For more information, see the main [FastHTTP Documentation](../../docs/en/index.md) or [HTTP/2 Support Guide](../../docs/en/http2-support.md).
