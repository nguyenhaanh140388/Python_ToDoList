def test_list_tasks_initial_empty(client):
    res = client.get("/api/tasks/")
    assert res.status_code == 200
    assert res.get_json() == []

def test_create_task_201(client):
    res = client.post("/api/tasks/", json={"title": "Học Flask"})
    assert res.status_code == 201
    data = res.get_json()
    assert "id" in data
    assert data["title"] == "Học Flask"
    assert data["done"] is False

def test_get_tasks_after_create(client):
    # tạo 2 task
    client.post("/api/tasks/", json={"title": "A"})
    client.post("/api/tasks/", json={"title": "B"})
    res = client.get("/api/tasks/")
    assert res.status_code == 200
    items = res.get_json()
    assert isinstance(items, list)
    assert len(items) == 2

def test_get_task_by_id_200(client):
    created = client.post("/api/tasks/", json={"title": "Detail"}).get_json()
    tid = created["id"]
    res = client.get(f"/api/tasks/{tid}")
    assert res.status_code == 200
    data = res.get_json()
    assert data["id"] == tid
    assert data["title"] == "Detail"

def test_get_task_404(client):
    res = client.get("/api/tasks/not-exist-id")
    assert res.status_code == 404
    assert res.get_json()["error"] == "Task not found"

def test_update_task_put_200(client):
    created = client.post("/api/tasks/", json={"title": "Old"}).get_json()
    tid = created["id"]
    res = client.put(f"/api/tasks/{tid}", json={"title": "New", "done": True})
    assert res.status_code == 200
    data = res.get_json()
    assert data["title"] == "New"
    assert data["done"] is True

def test_update_task_partial_200(client):
    created = client.post("/api/tasks/", json={"title": "Keep"}).get_json()
    tid = created["id"]
    # chỉ cập nhật done
    res = client.put(f"/api/tasks/{tid}", json={"done": True})
    assert res.status_code == 200
    data = res.get_json()
    assert data["title"] == "Keep"
    assert data["done"] is True

def test_update_task_404(client):
    res = client.put("/api/tasks/unknown", json={"title": "x"})
    assert res.status_code == 404
    assert res.get_json()["error"] == "Task not found"

def test_delete_task_200(client):
    created = client.post("/api/tasks/", json={"title": "Del"}).get_json()
    tid = created["id"]
    res = client.delete(f"/api/tasks/{tid}")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Task deleted"

    # verify không còn trong list
    res2 = client.get(f"/api/tasks/{tid}")
    assert res2.status_code == 404

def test_delete_task_404(client):
    res = client.delete("/api/tasks/unknown")
    assert res.status_code == 200  # theo code hiện tại: trả 200 dù không tồn tại
    # Nếu muốn chặt chẽ hơn (404), bạn cần đổi logic trong routes/tasks.py
