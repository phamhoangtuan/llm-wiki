# Game Theory: An open access textbook with 165 solved exercises

Finished date: 2026/04/04
Author: Giacomo Bonanno
Language: English
Type: Ebook
Number of pages: 585
Notes: # Cẩm Nang Lý Thuyết Trò Chơi: Từ Cơ Bản Đến Nâng Cao

Chào mừng bạn đến với hướng dẫn essential về "Game Theory: An Open Access Textbook" của Giacomo Bonanno. Đây không chỉ là một cuốn sách giáo khoa khô khan, mà là một lộ trình tư duy chiến lược, giúp bạn hiểu cách những cá thể thông minh và duy lý (rational individuals) tương tác với nhau trong các tình huống cạnh tranh hoặc hợp tác.

Hãy tưởng tượng bạn đang bước vào một bàn cờ lớn, nơi mỗi nước đi đều phụ thuộc vào nước đi của đối thủ. Cuốn sách này chia làm 5 Phần, dẫn dắt bạn từ những khái niệm đơn giản nhất đến những mô hình phức tạp nhất về niềm tin và thông tin.

---

## 🎯 Tổng Quan: Trò Chơi Không Hợp Tác (Non-Cooperative Game Theory)
Trọng tâm của cuốn sách là non-cooperative game theory—nơi mỗi người chơi đều tối ưu hóa lợi ích của chính mình.
*   Mục tiêu: Hiểu cách ra quyết định khi kết quả phụ thuộc vào hành động của người khác.
*   Cấu trúc: 5 Phần, đi từ thứ tự ưu tiên (ordinal) → con số cụ thể (cardinal) → kiến thức & niềm tin → các cân bằng tinh vi → thông tin không đầy đủ.

---

## 📊 Phần I: Games with Ordinal Payoffs (Khi chỉ cần biết "Thích cái nào hơn")
Ở mức cơ bản nhất, người chơi không cần biết chính xác lợi ích là bao nhiêu, chỉ cần biết thứ tự ưu tiên (ví dụ: "Thắng > Hòa > Thua").

### 1. Trò Chơi Chiến Lược (Strategic Form)
*   Bối cảnh: Các người chơi ra quyết định cùng lúc (simultaneous-move).
*   Khái niệm chìa khóa:
*   Game-frames vs. Games: Khung trò chơi là mô tả vật lý, còn Trò chơi bao gồm cả sở thích của người chơi.
*   Dominance (Tính ưu thế): Một nước đi luôn tốt hơn nước đi khác bất kể đối thủ làm gì.
*   IDSDS (Iterated Deletion of Strictly Dominated Strategies): Loại bỏ dần các nước đi "dở tệ" để tìm ra lựa chọn hợp lý.
*   Nash equilibrium: Điểm mà không ai muốn đơn phương thay đổi quyết định của mình.

### 2. Trò Chơi Động (Dynamic Games)
*   Bối cảnh: Các nước đi diễn ra tuần tự (sequential), người sau biết nước đi của người trước.
*   Công cụ: Backward induction (Quy nạp ngược).
*   Cách hiểu: Hãy nghĩ từ cuối trò chơi ngược về đầu để xác định nước đi tối ưu tại mỗi thời điểm.
*   Khi thông tin không hoàn hảo: Sử dụng Information sets (tập thông tin) để mô tả việc người chơi không biết chính xác nước đi trước đó.
*   Subgame-perfect equilibrium (SPE): Một cân bằng phải đúng trong mọi tiểu trò chơi (subgame), không chỉ ở tổng thể.

> 💡 Ví dụ: Giống như chơi cờ vua. Bạn không chỉ nghĩ nước đi hiện tại, mà phải tính trước các nước đi tiếp theo của đối thủ để phản đòn (Backward induction).

---

## 🎲 Phần II: Games with Cardinal Payoffs (Khi cần con số cụ thể & Xác suất)
Cuộc đời không chỉ là thứ tự, mà còn là rủi ro. Phần này đưa con số và xác suất vào bàn cờ.

### 1. Expected Utility (Hữu dụng kỳ vọng)
*   Nền tảng: Hàm utility von Neumann-Morgenstern (vNM).
*   Ý nghĩa: Giúp xếp hạng các "lotteries" (kết quả xác suất).
*   Thái độ với rủi ro: Người chơi có thể là Risk averse (ngại rủi ro), Neutral (trung lập), hoặc Loving (thích rủi ro).

### 2. Mixed Strategies (Chiến lược hỗn hợp)
*   Khi nào dùng? Khi không có điểm cân bằng thuần túy.
*   Cách hoạt động: Người chơi ngẫu nhiên hóa lựa chọn của mình để làm đối thủ "mất cảm giác" (indifferent) giữa các chiến lược của họ.
*   Mixed-strategy Nash equilibrium: Điểm cân bằng khi cả hai đều chơi ngẫu nhiên theo tỷ lệ tối ưu.

### 3. Dynamic Games with Cardinal Payoffs
*   Behavioral strategies: Gán xác suất cho các lựa chọn tại mỗi tập thông tin.
*   Lưu ý: SPE luôn tồn tại nhưng đôi khi cho phép các hành vi "vô lý" ở những nhánh trò chơi không bao giờ xảy ra.

---

## 🧠 Phần III: Advanced Topics I - Knowledge and Belief (Tôi biết, bạn biết, tôi biết bạn biết...)
Đây là phần "hàn lâm" nhất, giải mã những gì người chơi thực sự biết và tin về nhau.

### 1. Knowledge & Common Knowledge
*   Information partitions: Cách hình thức hóa kiến thức của từng người.
*   Common knowledge (Kiến thức chung): Không chỉ là "mọi người đều biết", mà là "mọi người đều biết rằng mọi người đều biết...", lặp lại vô hạn.
*   Ví dụ: Đèn giao thông màu đỏ là Common knowledge. Nếu chỉ một người thấy đỏ mà người kia không biết người kia thấy đỏ, tai nạn có thể xảy ra.

### 2. Beliefs & Updating
*   Bayesian updating: Cập nhật niềm tin khi có thông tin mới.
*   AGM belief revision: Cách xử lý khi nhận được thông tin gây ngạc nhiên (mâu thuẫn với niềm tin cũ).
*   Agreement Theorem: Những người cùng tư duy không thể "đồng ý về việc bất đồng" (agree to disagree) nếu họ chia sẻ chung kiến thức.

### 3. Common Knowledge of Rationality (CKR)
*   Định lý quan trọng: Trong trò chơi chiến lược, CKR tương đương với các chiến lược sống sót qua quá trình IDSDS. Nói cách khác, nếu mọi người đều biết nhau duy lý, họ sẽ không chơi những nước đi dở tệ.

---

## 🔍 Phần IV: Advanced Topics II - Equilibrium Refinements (Khi Nash Equilibrium chưa đủ tốt)
Đôi khi Nash equilibrium hoặc SPE đưa ra quá nhiều kết quả, trong đó có những kết quả vô lý. Chúng ta cần các bộ lọc (refinements).

| Khái Niệm | Đặc Điểm Chính | Mục Đích |
|-----------|----------------|----------|
| Weak Sequential Equilibrium | Đòi hỏi Sequential rationality (tối ưu tại mọi tập thông tin) và cập nhật Bayesian tại các nhánh đã xảy ra. | Loại bỏ các đe dọa không tin cậy. |
| Sequential Equilibrium | Thêm yêu cầu KW-consistency: Niềm tin tại các nhánh chưa xảy ra phải là giới hạn của một chuỗi chiến lược hỗn hợp. | Đảm bảo niềm tin "hợp lý" ngay cả khi sai sót xảy ra. |
| Perfect Bayesian Equilibrium (PBE) | Dựa trên Plausibility orders và AGM-consistency. | Một cách tiếp cận trực quan hơn để mô tả cân bằng mà không cần giới hạn toán học phức tạp. |

> 🛠️ Tại sao cần Refinements? Để loại bỏ các kịch bản "nếu tôi đi nước này, anh sẽ làm kia" mà thực tế không ai tin là sẽ xảy ra.

---

## ❓ Phần V: Advanced Topics III - Incomplete Information (Khi không biết luật chơi)
Phần cuối cùng xử lý tình huống khó nhất: Bạn không biết đối thủ muốn gì, hoặc thậm chí không biết rõ luật chơi.

### 1. Static Games with Incomplete Information
*   Harsanyi transformation: Một thủ thuật thiên tài. Biến thông tin không đầy đủ (về đối thủ) thành thông tin không hoàn hảo (bằng cách thêm một nước đi của Nature - Tự nhiên).
*   Giải pháp: Bayesian Nash equilibrium. Người chơi tối ưu hóa dựa trên niềm tin xác suất về "type" (loại hình) của đối thủ.

### 2. Dynamic Games with Incomplete Information
*   Ứng dụng thực tế:
*   Reputation effects: Hiệu ứng danh tiếng (ví dụ: trò chơi Chain-Store).
*   Costly signaling: Tín hiệu tốn kém (ví dụ: đình công lao động để chứng minh sức mạnh).
*   Type-space approach: Phương pháp gốc của Harsanyi dùng "types" để mô hình hóa, tương đương với các mô hình state-space đã học.

---

## ✨ Key Takeaways (Bài Cốt Lõi)

1.  Từ Ordinal đến Cardinal: Bắt đầu bằng sở thích đơn giản, sau đó thêm con số và xác suất để xử lý rủi ro.
2.  Thời gian matters: Trò chơi động (sequential) cần Backward induction và SPE để đảm bảo tính tin cậy của các lời đe dọa.
3.  Kiến thức là sức mạnh: Common knowledge và Belief updating là nền tảng để dự đoán hành vi của đối thủ.
4.  Cân bằng cần tinh chỉnh: Nash equilibrium đôi khi quá rộng, cần các refinements như PBE để lọc bỏ các kết quả vô lý.
5.  Biến bất định thành xác suất: Harsanyi transformation giúp giải quyết các trò chơi mà người chơi không biết rõ nhau bằng cách đưa yếu tố ngẫu nhiên (Nature) vào.

---

## 🚀 Lời Khuyên Cho Người Học
*   Đừng sợ toán: Các công cụ như Bayesian updating hay Expected Utility chỉ là cách hình thức hóa trực giác thông thường.
*   Tập tư duy ngược: Luôn thử áp dụng Backward induction khi gặp các quyết định tuần tự.
*   Đặt câu hỏi về thông tin: Trong mọi tình huống chiến lược, hãy hỏi: "Tôi biết gì? Đối thủ biết gì? Chúng ta có chung kiến thức không?"

> 🎯 Lý thuyết trò chơi không dạy bạn cách thắng mọi cuộc chơi, mà dạy bạn cách hiểu luật chơi—và hiểu cả những người chơi cùng bạn.

---
Hãy bắt đầu từ Phần I, nắm vững Nash equilibrium, rồi dần dần khám phá thế giới phức tạp của niềm tin và thông tin không đầy đủ. Chúc bạn tư duy chiến lược sắc bén! 🧠♟️