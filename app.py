from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(
            {
                "app": "dummy-jenkins-python-app",
                "message": "Hello! This small app is ready for Jenkins practice.",
                "endpoints": ["/health", "/api/greet?name=YourName"],
            }
        )

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/api/greet")
    def greet():
        name = request.args.get("name", "DevOps learner").strip()
        if not name:
            name = "DevOps learner"

        return jsonify({"message": f"Hello, {name}!"})

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
