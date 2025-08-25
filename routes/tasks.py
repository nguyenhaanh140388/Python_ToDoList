from flask import Blueprint, request, jsonify
import uuid

tasks_bp = Blueprint("tasks", __name__)

# Bộ nhớ tạm thời (chưa dùng DB)
tasks = []

# CREATE
@tasks_bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()
    task = {
        "id": str(uuid.uuid4()),   # sinh id duy nhất
        "title": data.get("title") + "1test_deployCICD from gitHUB",
        "done": False
    }
    tasks.append(task)
    return jsonify(task), 201

# READ (all)
@tasks_bp.route("/", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

# READ (one)
@tasks_bp.route("/<task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200

# UPDATE
@tasks_bp.route("/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found 123456789"}), 404
    
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task), 200

# DELETE
@tasks_bp.route("/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200
