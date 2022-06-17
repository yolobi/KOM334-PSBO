from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

data_book = {
    "author": "string",
    "isbn": "string",
    "title": "updated",
    "status_peminjaman": True,
    "id": 1,
    "description": "string",
    "id_peminjam": 1,
    "tanggal_peminjaman": "2022-06-17"
}

def test_get_book_by_id():
    response = client.get('/book/1')
    assert response.status_code == 200
    assert response.json() == data_book

def test_get_book_by_id_failed():
    response = client.get('/book/100')
    assert response.status_code == 404
    assert response.json() == {
        'detail' : 'Book with id 100 is not found'
    }

def test_delete_failed_book():
    response = client.delete('/book/200')
    assert response.status_code == 404
    assert response.json() == {
        'detail':'Book with id 200 is not found'
    }

def test_get_librarian_by_id():
    response = client.get('/librarian/1')
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nip": "12345"
    }

def test_get_librarian_by_id_failed():
    response = client.get('/librarian/100')
    assert response.status_code == 404
    assert response.json() == {
        'detail': 'Librarian with id 100 is not found'
    }
    

def test_delete_Librarian_failed():
    response = client.delete('/librarian/200')
    assert response.status_code == 404
    assert response.json() == {
        'detail':'Librarian with id 200 is not found'
    }

def test_get_Student_by_id():
    response = client.get('/student/1')
    assert response.status_code == 200
    assert response.json() == {
        "denda": 0,
        "nisn": "9988",
        "id": 1
    }

def test_get_Student_by_id_failed():
    response = client.get('/student/100')
    assert response.status_code == 404
    assert response.json() == {
        'detail': 'Student with id 100 is not found'
    }

def test_delete_Student_failed():
    response = client.delete('/student/200')
    assert response.status_code == 404
    assert response.json() == {
        'detail':'Student with id 200 is not found'
    }

def test_student_pinjam():
    response = client.put('/student/pinjam/1/2')
    assert response.status_code == 200
    assert response.json() == 'buku telah dipinjam'

def test_get_Log_by_id_failed():
    response = client.get('/log/100')
    assert response.status_code == 404
    assert response.json() == {
        'detail': 'log with id 100 is not found'
    }

def test_delete_Log_failed():
    response = client.delete('/log/200')
    assert response.status_code == 404
    assert response.json() == {
        'detail':'log with id 200 is not found'
    }