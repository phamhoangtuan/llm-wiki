# Good Code, Bad Code

Finished date: 2026/05/13
Author: Tom Long
Language: English
Type: Ebook
Number of pages: 338
Notes: # Cẩm Nang Good Code, Bad Code: Tư Duy Của Một Software Engineer

Chào mừng bạn đến với hướng dẫn essential dựa trên cuốn sách "Good Code, Bad Code: Think like a software engineer" của Tom Long.

Viết code cho máy chạy thì dễ. Nhưng viết code để con người duy trì, mở rộng và tin tưởng trong nhiều năm là một nghệ thuật khác. Cuốn sách này không dạy cú pháp, mà dạy bạn cách chuyển hóa từ một Coder (người viết lệnh) thành một Software Engineer (kỹ sư xây dựng hệ thống bền vững).

> 💡 Thông điệp cốt lõi: Code chất lượng cao không phải là sở thích thẩm mỹ. Đó là sự cần thiết thực tế cho sự ổn định của doanh nghiệp và an toàn của người dùng.

---

## 🎯 Software Engineering ≠ Coding
Nhiều người nhầm lẫn giữa việc viết code và kỹ thuật phần mềm. Tom Long phân biệt rõ ràng qua 3 yếu tố:

| Yếu Tố | Coding (Viết Code) | Software Engineering (Kỹ Thuật Phần Mềm) |
|--------|-------------------|-----------------------------------------|
| Thời gian | Viết xong là quên (Write & Forget) | Code phải sống lâu, chịu được thay đổi qua nhiều năm |
| Hậu quả | Project cá nhân, sai thì sửa | Hệ thống thực tế (ngân hàng, y tế), sai có thể ruin lives |
| Môi trường | Làm việc một mình (Solitary) | Codebase là "busy places" — nhiều người cùng sửa cùng lúc |

> 🏗️ Ví dụ: Coding giống như viết một bức thư. Engineering giống như xây một tòa nhà — nhiều thợ cùng làm, và nó phải đứng vững qua bão tố.

### Quy Trình Phát Triển & Deploy Chuẩn
Để code từ máy local ra được Production, nó phải đi qua một quy trình nghiêm ngặt:
1.  Code Change: Sửa đổi trên bản local.
2.  Code Review: "Proofreading" — đồng nghiệp kiểm tra để tìm lỗi sót.
3.  Commit: Merge vào codebase chính.
4.  Pre-submit Checks: Automated tests chặn code lỗi trước khi merge.
5.  Release: Cắt snapshot, QA lần cuối.
6.  Production: Deploy cho người dùng thực tế.

---

## 🎯 4 Mục Tiêu Của Code Chất Lượng
Code tốt không phải là code "đẹp mắt". Code tốt là code đạt được 4 mục tiêu khách quan sau:

| Mục Tiêu | Ý Nghĩa Thực Tế |
|----------|----------------|
| 1. It should work ✅ | Code phải giải quyết đúng vấn đề, bao gồm cả performance, security, privacy. |
| 2. It should keep working 🛡️ | Code phải vẫn chạy khi dependencies thay đổi, tính năng mới thêm vào, nghiệp vụ evolve. |
| 3. It should be adaptable 🔄 | Yêu cầu sẽ thay đổi. Code phải cấu trúc để sửa đổi mà không cần rewrite toàn bộ. |
| 4. No reinventing the wheel 🛞 | Tận dụng giải pháp có sẵn. Viết code mới sao cho người khác có thể reuse lại. |

---

## 🏛️ 6 Trụ Cột Của Code Chất Lượng (The 6 Pillars)
Làm sao để đạt được 4 mục tiêu trên? Hãy xây dựng code dựa trên 6 trụ cột chiến thuật này:

### 1. Make Code Readable (Dễ Đọc)
Code viết cho người đọc, không chỉ cho máy chạy.
*   Vấn đề: Code khó đọc giống như công thức nấu ăn không có tiêu đề — người sau phải mất thời gian "giải mã" ý định.
*   Hậu quả: Bug dễ lọt qua review, sửa vào dễ gây lỗi mới.
*   Giải pháp: Đặt tên biến/hàm rõ nghĩa, cấu trúc logic mạch lạc.

### 2. Avoid Surprises (Tránh Bất Ngờ)
Đừng làm người đọc code bị "shock".
*   Câu chuyện ví dụ: Một hàm gọi là dialRestaurant() nhưng khi nhà hàng bận, nó tự động gọi sang nhà hàng khác. Ý tốt, nhưng là surprise. Kết quả: Khách order pizza Margarita mà lại nhận được cocktail Margarita ở quán bar bên cạnh.
*   Bài học: Function phải làm đúng những gì tên gọi mô tả. Không side effects ẩn giấu.

### 3. Make Code Hard to Misuse (Khó Dùng Sai)
Thiết kế để ngăn lỗi từ gốc.
*   Ví dụ thực tế: Cổng sau TV có nhiều loại (HDMI, nguồn, audio). Chúng được thiết kế hình dạng khác nhau để bạn không thể cắm dây nguồn vào cổng HDMI.
*   Áp dụng vào code: Dùng đúng data types, interfaces để compiler báo lỗi nếu người gọi truyền sai tham số. Đừng để họ "cắm sai ổ".

### 4. Make Code Modular (Tính Module)
Chia hệ thống thành các thành phần nhỏ, độc lập.
*   Hệ thống Modular: Giống như đồ chơi Lego — dễ tháo lắp, thay thế từng khối mà không hỏng cả cấu trúc.
*   Hệ thống "Stitched-together": Giống như dán keo các mảnh gỗ — muốn sửa một chỗ phải đập vỡ cả khối.
*   Lợi ích: Dễ reconfigure, dễ debug, dễ thay thế component.

### 5. Make Code Reusable & Generalizable (Tái Sử Dụng)
*   Reusability: Dùng cùng một code cho nhiều scenario giống nhau.
*   Ví dụ: Một cái máy khoan dùng được cho tường, sàn, trần.
*   Generalizability: Dùng code để giải quyết vấn đề khác nhưng tương đồng về khái niệm.
*   Ví dụ: Cái máy khoan đó có thể gắn thêm đầu để làm tua-vít.
*   Lợi ích: Giảm tổng số dòng code → Giảm diện tích bề mặt cho bug tấn công.

### 6. Make Code Testable (Dễ Kiểm Thử)
Testing là hàng rào phòng thủ cuối cùng trước khi lên Production.
*   3 Cấp độ Test:
1.  Unit Tests: Test từng hàm/class nhỏ.
2.  Integration Tests: Test các components phối hợp với nhau.
3.  End-to-End (E2E): Test toàn bộ workflow người dùng.
*   Testability: Code càng modular thì càng dễ test vì có thể isolate từng phần để kiểm tra độc lập.

---

## 🏗️ Chiến Lược Cấu Trúc: Layers of Abstraction
Để quản lý sự phức tạp, hãy chia vấn đề lớn thành các lớp trừu tượng (abstraction layers).

### API vs. Implementation Detail
| Thành Phần | Đặc Điểm | Ví Dụ |
|------------|----------|-------|
| Public API 📢 | Những gì caller thấy (tên hàm, params). Phải expose khái niệm cấp cao. | user.save() |
| Implementation Details ⚙️ | Logic "nuts-and-bolts" bên trong. Phải ẩn đi để tránh leak. | Câu lệnh SQL INSERT INTO... |

### Thiết Kế Function & Class
*   Small Functions: Một hàm chỉ nên làm một việc. Nếu không thể mô tả bằng một câu ngắn gọn → Hàm quá phức tạp.
*   Cohesive Classes: Group các khái niệm liên quan. Tránh "MassiveClass" — một class làm quá nhiều việc, gây khó đọc và khó reuse.
*   Layer Thickness: Lớp không quá dày (gộp nhiều abstraction) cũng không quá mỏng (tạo boilerplate không cần thiết).

### Vai Trò Của Interfaces
Interfaces giúp tạo lớp ranh giới rõ ràng, đặc biệt khi cần nhiều implementation khác nhau.
*   Ví dụ: Interface TextImportanceScorer có thể có 2 implementation: WordBasedScorer và ModelBasedScorer.
*   Lợi ích: Code phụ thuộc vào Interface sẽ modular và dễ cấu hình hơn là phụ thuộc vào concrete class.

---

## 💰 Giá Trị Dài Hạn: "Less Haste, More Speed"
Một hiểu lầm phổ biến: Viết code chất lượng làm chậm tiến độ.

| Cách Tiếp Cận | Ngắn Hạn | Dài Hạn |
|---------------|----------|---------|
| Hacky Solutions 🚀 | Nhanh vài phút (như dán kệ vào tường bằng keo) | Thảm họa sau này (kệ rơi, phải sửa lại toàn bộ) |
| High-Quality Code 🐢 | Tốn thời gian suy nghĩ ban đầu | Tăng tốc độ phát triển bền vững, tránh refactoring đau đớn |

> 🎯 Triết lý: Đầu tư vào readability, modularity, và testing ngay từ đầu sẽ ngăn codebase trở thành một đống hỗn độn fragile. Tốc độ thực sự nằm ở sự bền vững, không phải sự vội vã.

---

## ✨ Key Takeaways (Bài Cốt Lõi)

1.  Engineering > Coding: Code phải sống lâu, chịu được nhiều người sửa, và có hậu quả thực tế.
2.  4 Goals: Work → Keep Working → Adaptable → Reuse.
3.  6 Pillars: Readable, No Surprises, Hard to Misuse, Modular, Reusable, Testable.
4.  Abstraction: Ẩn implementation details, expose clean APIs.
5.  Interfaces: Giúp hệ thống modular và dễ thay thế implementation.
6.  Less Haste, More Speed: Code chất lượng không làm chậm bạn — nó ngăn bạn phải chạy chậm lại trong tương lai để sửa lỗi.

---

## 🧭 Lời Khuyên Cho Kỹ Sư Phần Mềm

Khi viết code hôm nay: ✅ Hỏi: "Người khác đọc đoạn này có hiểu ngay không?" (Readability) ✅ Kiểm tra: "Hàm này có làm gì bất ngờ không?" (No Surprises) ✅ Thiết kế: "Làm sao để compiler báo lỗi nếu người dùng truyền sai data?" (Hard to Misuse) ✅ Chia nhỏ: "Class này có đang làm quá nhiều việc không?" (Modularity) ✅ Test: "Code này có dễ viết unit test không?" (Testability) ✅ Suy nghĩ dài hạn: "Giải pháp nhanh này có gây nợ kỹ thuật không?" (Long-term Value)

> 🎯 Code chất lượng không phải là đích đến, mà là một thói quen hàng ngày. Mỗi lần bạn chọn viết code rõ ràng thay vì code "khôn ngoan", bạn đang đầu tư cho tương lai của chính mình và đồng đội.

---
Hãy bắt đầu refactor một function hôm nay: Đặt lại tên cho rõ nghĩa, tách nhỏ logic, và viết một unit test cho nó. Chúc bạn xây dựng những hệ thống bền vững và đáng tin cậy! 🚀💻🛠️