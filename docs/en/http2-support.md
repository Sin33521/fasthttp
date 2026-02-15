# HTTP/2 Support

FastHTTP supports HTTP/2 protocol for improved performance with servers that support it. HTTP/2 provides multiplexing, header compression, and better overall performance for multiple concurrent requests.

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

This installs the required dependencies for HTTP/2 support.

## How It Works

When HTTP/2 is enabled:

1. FastHTTP attempts to use HTTP/2 for all requests
2. If the server supports HTTP/2, the connection uses HTTP/2
3. If the server doesn't support HTTP/2, httpx automatically falls back to HTTP/1.1
4. No code changes needed - everything is handled automatically

## Example

```python
from fasthttp import FastHTTP
from fasthttp.response import Response

app = FastHTTP(http2=True)

@app.get(url="https://www.google.com/")
async def get_google(resp: Response):
    print(f"Status: {resp.status}")
    return resp.status

@app.get(url="https://github.com/")
async def get_github(resp: Response):
    print(f"Status: {resp.status}")
    return resp.status

if __name__ == "__main__":
    app.run()
```

## Important Notes

### Server Support

Not all servers support HTTP/2. Here are some that do:

- **Google** - https://www.google.com
- **GitHub** - https://github.com
- **YouTube** - https://www.youtube.com
- **Twitter/X** - https://twitter.com

Servers that typically use HTTP/1.1:

- **httpbin.org** - https://httpbin.org
- Many older websites
- Some API services

### Automatic Fallback

If a server doesn't support HTTP/2, httpx automatically falls back to HTTP/1.1. Your code doesn't need to handle this - it's transparent.

### Performance Benefits

HTTP/2 provides the most benefit when:

- Making multiple concurrent requests to the same server
- The server supports HTTP/2
- You have a good network connection

For single requests, the performance difference may be minimal.

### Redirects

Some servers may redirect from HTTP/2 to HTTP/1.1 during redirects. This is normal behavior and handled automatically.

## Checking HTTP/2 Status

You can verify if HTTP/2 is being enabled in your logs:

```
INFO     │ fasthttp │ ✔ HTTP/2 enabled
```

When HTTP/2 is enabled, httpx will automatically use HTTP/2 for servers that support it and fall back to HTTP/1.1 for servers that don't. The fallback is transparent and automatic.

**Note:** Most modern browsers and HTTP clients will show HTTP/2 in their network inspector when connecting to servers that support it. The same applies to httpx with HTTP/2 enabled.

## Limitations

1. **Server Support** - Only works with servers that support HTTP/2
2. **Proxy Support** - Some proxies may not support HTTP/2
3. **Testing** - Not all HTTP testing services support HTTP/2

## Troubleshooting

### HTTP/2 Not Working

If HTTP/2 doesn't seem to be working:

1. **Check server support** - Verify the server actually supports HTTP/2
2. **Check installation** - Ensure you installed with `[http2]` extra
3. **Check redirects** - Some servers redirect to HTTP/1.1
4. **Enable debug mode** - Use `debug=True` to see detailed logs

```python
app = FastHTTP(
    http2=True,
    debug=True  # See detailed logs
)
```

### Fallback to HTTP/1.1

If you see HTTP/1.1 being used instead of HTTP/2:

- This is normal for servers that don't support HTTP/2
- The fallback is automatic and transparent
- No code changes needed

---

For more information, see the [Examples](examples.md) section.
