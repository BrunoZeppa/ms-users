from flask import Flask, request, after_this_request
from flask_api import status
import pandas as pd

app = Flask(__name__)


@app.route("/api/v2/users")
def users():
    users = pd.read_csv(
        "/Users/brunozeppa/Desktop/entregable_sem3_python/ms-users/users_spreadsheet.csv")
    return {"status": "success", "number of users": len(users)}, status.HTTP_200_OK


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)
