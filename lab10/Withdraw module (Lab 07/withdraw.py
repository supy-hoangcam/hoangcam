import mysql.connector
import hashlib

DB_CONFIG = {
    "user": "root",
    "password": "123456",
    "host": "localhost",
    "database": "atm_demo"
}

def verify_pin(card_no, pin):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT pin_hash, status FROM cards WHERE card_no=%s", (card_no,))
    row = cur.fetchone()
    conn.close()

    if not row:
        return False, "Card not found"
    pin_hash, status = row
    if status != "ACTIVE":
        return False, f"Card status {status}"
    return pin_hash == hashlib.sha256(pin.encode()).hexdigest(), None

def withdraw(card_no, amount):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    try:
        conn.start_transaction()
        cur.execute("""
            SELECT a.account_id, a.balance 
            FROM accounts a
            JOIN cards c ON a.account_id = c.account_id
            WHERE c.card_no=%s
            FOR UPDATE
        """, (card_no,))
        row = cur.fetchone()
        if not row:
            raise Exception("Account not found")

        account_id, balance = row
        if balance < amount:
            raise Exception("Insufficient funds")

        # Trừ tiền
        cur.execute("UPDATE accounts SET balance=balance-%s WHERE account_id=%s",
                    (amount, account_id))

        # Ghi log transaction
        cur.execute("""
            INSERT INTO transactions(account_id, card_no, atm_id, tx_type, amount, balance_after)
            VALUES (%s, %s, 1, 'WITHDRAW', %s, %s)
        """, (account_id, card_no, amount, balance - amount))

        conn.commit()
        print(f"Withdraw success: {amount} (new balance: {balance - amount})")

    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        conn.close()


if __name__ == "__main__":
    # Test demo
    card_no = "12345678"
    pin = "1234"
    amount = 1000

    ok, err = verify_pin(card_no, pin)
    if not ok:
        print("PIN check failed:", err)
    else:
        withdraw(card_no, amount)
