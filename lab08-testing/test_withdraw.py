import pytest
import mysql.connector
import hashlib
from withdraw_module import verify_pin, withdraw   # import từ lab07

# ---- Unit Test for verify_pin ----
def test_verify_pin_correct(monkeypatch):
    # Giả lập DB trả về hash đúng
    correct_hash = hashlib.sha256("1234".encode()).hexdigest()

    def fake_execute(query, params):
        pass

    class FakeCursor:
        def execute(self, q, p): pass
        def fetchone(self): return (correct_hash,)
    class FakeConn:
        def cursor(self): return FakeCursor()
        def close(self): pass

    monkeypatch.setattr(mysql.connector, "connect", lambda **kwargs: FakeConn())
    assert verify_pin("111122223333", "1234") == True

def test_verify_pin_incorrect(monkeypatch):
    wrong_hash = hashlib.sha256("9999".encode()).hexdigest()

    class FakeCursor:
        def execute(self, q, p): pass
        def fetchone(self): return (wrong_hash,)
    class FakeConn:
        def cursor(self): return FakeCursor()
        def close(self): pass

    monkeypatch.setattr(mysql.connector, "connect", lambda **kwargs: FakeConn())
    assert verify_pin("111122223333", "1234") == False


# ---- Unit Test for withdraw ----
def test_withdraw_success(monkeypatch):
    # Mock DB account balance = 1000
    db_state = {"balance": 1000}

    class FakeCursor:
        def execute(self, q, p):
            if "SELECT account_id" in q:
                self._row = (1, db_state["balance"])
            elif "UPDATE accounts" in q:
                db_state["balance"] -= p[0]
            elif "INSERT INTO transactions" in q:
                pass
        def fetchone(self): return self._row
    class FakeConn:
        def cursor(self): return FakeCursor()
        def start_transaction(self): pass
        def commit(self): pass
        def rollback(self): pass
        def close(self): pass

    monkeypatch.setattr(mysql.connector, "connect", lambda **kwargs: FakeConn())
    withdraw("111122223333", 200)
    assert db_state["balance"] == 800   # trừ tiền đúng

def test_withdraw_insufficient(monkeypatch):
    db_state = {"balance": 100}

    class FakeCursor:
        def execute(self, q, p):
            if "SELECT account_id" in q:
                self._row = (1, db_state["balance"])
        def fetchone(self): return self._row
    class FakeConn:
        def cursor(self): return FakeCursor()
        def start_transaction(self): pass
        def commit(self): pass
        def rollback(self): pass
        def close(self): pass

    monkeypatch.setattr(mysql.connector, "connect", lambda **kwargs: FakeConn())
    with pytest.raises(Exception, match="Insufficient funds"):
        withdraw("111122223333", 200)

