# ATM Mini Project - UML Design

## Mục tiêu
Mô tả luồng tương tác chi tiết của hệ thống ATM.

## 1. Use Case Diagram
Diễn tả các chức năng chính: Login, Withdraw Cash, Deposit Cash, Check Balance, Change PIN.

Actors:
- **Customer**: người dùng tương tác trực tiếp với ATM.
- **BankSystem**: xử lý xác thực, giao dịch và lưu trữ dữ liệu.

## 2. Sequence Diagram: Quy trình rút tiền

### Đối tượng tham gia
- **Customer**: Khách hàng sử dụng ATM.
- **ATM**: Máy ATM, trung gian giữa khách hàng và ngân hàng.
- **BankServer**: Hệ thống ngân hàng xác thực và xử lý giao dịch.

### Luồng thông điệp chính
1. Customer insertCard() vào ATM.
2. ATM promptPIN(), Customer enterPIN().
3. ATM gửi validatePIN() tới BankServer → nhận validationResult.
4. Nếu PIN hợp lệ → ATM showOptions().
5. Customer chọn Withdraw, nhập số tiền.
6. ATM gửi requestWithdrawal(amount) tới BankServer.
7. BankServer approveTransaction(), ATM dispenseCash() và printReceipt().
8. Nếu PIN sai → ATM showError("Invalid PIN").

## 3. Hướng dẫn Upload GitHub
1. Tạo repo mới trên GitHub (vd: `atm-mini-uml`).
2. Clone repo:
   ```bash
   git clone https://github.com/<username>/atm-mini-uml.git
   ```
3. Copy các thư mục `diagrams/` và `docs/` vào repo.
4. Commit và push:
   ```bash
   git add .
   git commit -m "Add ATM UML diagrams and description"
   git push origin main
   ```

## 4. Render PlantUML
- Cài plugin PlantUML trong VS Code.
- Mở file `.puml` và dùng `Alt+D` (hoặc chuột phải → "Preview Current Diagram") để xem sơ đồ.
