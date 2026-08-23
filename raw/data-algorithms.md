# Data Algorithms

Finished date: 2026/04/14
Author: Mahmoud Parsian
Language: English
Type: Ebook
Number of pages: 778
Notes: # Cẩm Nang Market Basket Analysis: Khám Phá Bí Mật Giỏ Hàng Của Khách Hàng

Chào mừng bạn đến với hướng dẫn essential về Market Basket Analysis (MBA) — một kỹ thuật data mining kinh điển giúp khám phá những mối liên hệ ẩn giấu giữa các sản phẩm trong hàng triệu giao dịch.

Hãy tưởng tượng bạn là chủ một siêu thị: MBA chính là "trợ lý thông minh" giúp bạn trả lời câu hỏi: "Nếu khách mua bánh mì, khả năng họ mua kèm bơ là bao nhiêu?" — từ đó sắp xếp kệ hàng, đề xuất sản phẩm, và tối đa hóa lợi nhuận.

---

## 🎯 Market Basket Analysis Là Gì?
> Market Basket Analysis (MBA) là kỹ thuật khai phá dữ liệu để xác định affinities và correlations giữa các sản phẩm trong tập giao dịch lớn.

Trong bối cảnh Data Algorithms, MBA là bài toán tính toán intensively — lý tưởng để xử lý song song bằng các framework như Hadoop và Spark.

### Mục Tiêu Cốt Lõi: Tạo Ra Association Rules
MBA tự động sinh ra các luật kết hợp dạng "if-then":
Nếu khách mua X → Khả năng cao họ cũng mua YVí dụ: {Bánh mì} → {Bơ} nghĩa là: "Nếu mua bánh mì, khách có xu hướng mua kèm bơ."

---

## 📊 2 Chỉ Số Đánh Giá Luật Kết Hợp
Để biết một rule có đáng tin hay không, ta dùng 2 metrics:

| Metric | Công Thức | Ý Nghĩa Thực Tế |
|--------|-----------|----------------|
| Support | Số giao dịch chứa {X,Y} / Tổng giao dịch | Mức độ phổ biến của nhóm sản phẩm. Support thấp = hiếm khi xuất hiện cùng nhau. |
| Confidence | Số giao dịch chứa {X,Y} / Số giao dịch chứa {X} | Xác suất mua Y khi đã mua X. Confidence cao = mối liên hệ mạnh. |

> 💡 Ví dụ:
> - Support của {Coca, Pizza} = 5% → 5% hóa đơn có cả hai món.
> - Confidence của {Pizza} → {Coca} = 70% → 7/10 người mua pizza cũng mua Coca.
> → Đây là rule đáng để đặt Coca gần quầy pizza!

---

## ⚙️ Triển Khai MBA Với MapReduce: Logic Cốt Lõi
Với hàng triệu giao dịch và hàng tỷ tổ hợp sản phẩm tiềm năng, ta cần distributed algorithms. Dưới đây là workflow MapReduce kinh điển:

### 🔹 Mapper Phase: Chuẩn Hóa & Đếm
python # Input: Một giao dịch = tập các sản phẩm # Output: Các cặp/tổ hợp sản phẩm đã sắp xếp + count = 1  def mapper(transaction):     # BƯỚC QUAN TRỌNG: Sort alphabetically!     sorted_items = sorted(transaction)  # ["coke", "pizza"] không phải ["pizza", "coke"]          # Generate combinations (pairs, triples, etc.)     for combo in generate_combinations(sorted_items):         emit(key=combo, value=1) 

> ⚠️ Tại sao phải sort?
> Nếu không sort, "coke, pizza" và "pizza, coke" sẽ bị tính là 2 keys khác nhau → sai frequency counts!

### 🔹 Reducer Phase: Tổng Hợp Kết Quả
python # Input: (combo, [1, 1, 1, ...]) # Output: (combo, total_count)  def reducer(combo, counts):     total = sum(counts)     emit(key=combo, value=total)  # Frequency cuối cùng của tổ hợp này 

---

## 🆚 Hadoop vs Spark: Hai Cấp Độ Triển Khai
| Framework | Trọng Tâm | Quy Trình |
|-----------|-----------|-----------|
| Hadoop/MapReduce | Tìm frequent patterns (các tổ hợp xuất hiện thường xuyên) | 1 phase: Count frequency của các itemsets |
| Spark | Tìm patterns + sinh association rules + tính confidence | 2 phases:<br>1️⃣ Tìm frequent patterns<br>2️⃣ Generate subpatterns để tính rule probabilities |

> 💡 Spark thắng ở đâu?
> Nhờ abstraction cao hơn và in-memory processing, Spark có thể thực hiện cả pipeline MBA (từ raw data → rules) trong một workflow thống nhất, nhanh hơn nhiều so với MapReduce truyền thống.

---

## 🌍 Ứng Dụng Thực Tế: Không Chỉ Là Siêu Thị
MBA không chỉ dành cho "giỏ hàng" theo nghĩa đen. Các industry áp dụng bao gồm:

| Ngành | Ứng Dụng MBA | Giá Trị Mang Lại |
|--------|-------------|-----------------|
| E-commerce (Amazon, Shopee) | Đề xuất "Customers who bought this also bought..." | Tăng cross-sell, cải thiện trải nghiệm người dùng |
| Bán lẻ truyền thống | Sắp xếp kệ hàng: đặt sản phẩm hay mua kèm gần nhau | Tăng giá trị đơn hàng trung bình |
| Tài chính / Thẻ tín dụng | Phân tích mẫu mua sắm, phát hiện giao dịch bất thường | Fraud detection: nếu rule {Gas station} → {Grocery} bị phá vỡ, có thể là thẻ bị đánh cắp |
| Bảo hiểm y tế | Phát hiện claim fraud khi các dịch vụ thường đi cùng nhau lại xuất hiện riêng lẻ | Giảm thiểu gian lận, tiết kiệm chi phí |
| Viễn thông | Phân tích gói dịch vụ khách hàng hay mua kèm | Thiết kế bundle sản phẩm hấp dẫn hơn |

---

## ✨ Key Takeaways (Bài Cốt Lõi)

1.  MBA = Tìm pattern ẩn trong giỏ hàng: Giúp hiểu hành vi khách hàng và tự động sinh recommendation.
2.  Support & Confidence là 2 metrics sống còn: Support đo độ phổ biến, Confidence đo độ tin cậy của rule.
3.  Sort trước khi count: Bước tưởng nhỏ nhưng quyết định độ chính xác của toàn bộ pipeline MapReduce.
4.  Spark > Hadoop cho MBA: Nhờ khả năng xử lý multi-phase workflow và in-memory computing.
5.  Ứng dụng đa ngành: Từ retail đến finance, telecom, healthcare — nơi nào có transaction data, nơi đó MBA có giá trị.
6.  Business impact rõ ràng: Tối ưu layout, tăng doanh thu, phát hiện fraud — tất cả bắt đầu từ một câu hỏi đơn giản: "Sản phẩm nào hay đi cùng nhau?"

---

## 🧭 Lời Khuyên Cho Data Engineer

Khi triển khai MBA: ✅ Luôn sort items trong Mapper để tránh duplicate keys ✅ Bắt đầu với pair patterns (order=2) trước khi mở rộng sang triples ✅ Dùng Spark nếu cần sinh rules + tính confidence end-to-end ✅ Filter bằng min_support/min_confidence để tránh "rule explosion" ✅ Kết hợp với business knowledge: rule có confidence cao nhưng support quá thấp có thể không khả thi thương mại

---

> 🎯 Market Basket Analysis không chỉ là thuật toán — nó là cầu nối giữa dữ liệu thô và quyết định kinh doanh thông minh. Một rule nhỏ như {Tã em bé} → {Bia} có thể thay đổi hoàn toàn cách bạn sắp xếp siêu thị.

---
Hãy bắt đầu với một tập dữ liệu giao dịch nhỏ, tính Support/Confidence cho vài cặp sản phẩm, và xem bạn khám phá được điều gì thú vị. Chúc bạn "đào" được vàng từ giỏ hàng! 🛒🔍🚀