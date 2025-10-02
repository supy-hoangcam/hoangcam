1. Giới thiệu ATM Mini Project
Mục tiêu: xây dựng hệ thống ATM đơn giản gồm login, rút tiền, kiểm tra số dư.
Phạm vi: chỉ tập trung vào 2 chức năng chính (login, withdraw).
Công cụ: UML (draw.io, StarUML), MySQL, HTML/CSS/JS, Python/Java, Jira, GitHub.

2. Mô hình UML
Use Case Diagram (Lab 02): mô tả các tác nhân (Customer, Bank System).
Sequence Diagram (Lab 03): chi tiết luồng Rút tiền.
Class Diagram (Lab 06): các lớp ATMController, BankServer, Customer, Transaction.

3. Database & Code minh hoạ
ERD (Lab 05): bảng Users, Accounts, Transactions.
Script SQL khởi tạo database + dữ liệu mẫu.
Form Login (Lab 04): HTML/CSS/JS kiểm tra input.
Withdraw Module (Lab 07): code kết nối DB → xử lý kiểm tra số dư → cập nhật bảng Transactions.

4. Kết quả kiểm thử & Sprint Report
Test Script (Lab 08):
TC01: Login thành công.
TC02: Login sai mật khẩu.
TC03: Rút tiền thành công.
TC04: Rút tiền vượt số dư.
Jira Report (Lab 09): ảnh chụp board (To do → In progress → Done), sprint burndown.

5. Kết luận & Định hướng mở rộng
Đã tích hợp đầy đủ artifacts UML, DB, code, test.
Demo chạy được login + withdraw + hiển thị kết quả DB.
Mở rộng: nạp tiền, chuyển khoản, in biên lai, bảo mật OTP.

🎥 Demo trên lớp (Flow gợi ý)
Mở form login → nhập user/pass hợp lệ → login success.
Chọn chức năng Withdraw → nhập số tiền → hệ thống kiểm tra DB → cập nhật số dư.
Trình chiếu Jira board → cho thấy các User Stories, Sprint report.
Kết luận → hệ thống mô phỏng ATM cơ bản, có thể mở rộng thêm.
