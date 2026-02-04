from fasthttp import FastHTTP

app = FastHTTP(debug=True)


@app.get(url="invalid://aiohttp.url/")
async def invalid_url_test(resp):
    print("This won't be printed due to invalid URL")
    return resp.json()


if __name__ == "__main__":
    app.run()
