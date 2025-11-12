from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.get("/")
def root():
    return jsonify(
        {
            "message": "Hello from Flask on OCI Container Instance!",
            "version": "1.0.0",
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)


