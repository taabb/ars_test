from flask import Flask, render_template, redirect, url_for, request
import uuid

app = Flask(__name__)

todo_data = []


# list = ["Купить тетради", "Сходить на тренеровку", "Покушать"]

@app.route("/")
def index():
    return render_template("index.html", db = todo_data)


@app.route("/add_item", methods=["POST", "GET"])
def add_item():
    text = request.form.get("text")
    text = text.strip()
    if not len(text) > 0:
        return redirect(url_for("index"))
    else:
        item = {
            "id": str(uuid.uuid4()),
            "text":  text,
            "status": False,
        }

        todo_data.append(item)
        print(todo_data)

        return redirect(url_for("index"))


@app.route("/change_item/<id>")
def change_status(id):
    for item in todo_data:
        if item["id"] == id:
            item["status"] = not item["status"]

    return redirect(url_for("index"))


@app.route("/delete/<id>")
def delete(id):
    for item in todo_data:
        if item["id"] == id:
            todo_data.remove(item)

    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()