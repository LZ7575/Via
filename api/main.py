from uvicorn import run

# Running the app (can also run using the uvicorn cli)
def main():
    run("src.api:app", host="0.0.0.0", port=3000, reload=True)

# Calling main
if __name__ == "__main__":
    main()