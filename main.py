from app.modules.uploader import upload_to_test

if __name__ == "__main__":
    data = {
        "message": "Привет от Python!",
        "author": "Andrey"
    }
    upload_to_test("https://httpbin.org/post", data)
