# Learn Harness Engineering

Finished date: 2026/05/31
Author: https://walkinglabs.github.io/learn-harness-engineering/en/
Language: English
Type: Ebook
Notes: # Cẩm Nang Harness Engineering: Xây Dựng Môi Trường Đáng Tin Cậy Cho AI Agents

Chào mừng bạn đến với hướng dẫn essential về Harness Engineering — kỷ luật thiết kế hệ thống giúp biến những AI agents thông minh nhưng "bốc đồng" thành những cộng sự kỹ thuật đáng tin cậy, có thể giao việc phức tạp mà không lo "mất dấu" giữa chừng.

> 💡 Thông điệp cốt lõi: Harness Engineering không làm model "thông minh hơn". Nó tạo ra một hệ thống closed-loop để model hoạt động trong môi trường có ràng buộc, có verification, và có state management — nơi "done" thực sự nghĩa là "chạy được", không chỉ là "viết xong".

Nếu ví AI agent như một kỹ sư tài năng nhưng hay quên, thì harness chính là quy trình làm việc + checklist + hệ thống review giúp họ không bỏ sót bước, không tuyên bố "xong rồi" khi chưa test, và không mất context khi chuyển ca.

---

## 🎯 Harness Engineering Là Gì? (Và Tại Sao Bạn Cần Nó?)

### Vấn Đề Cốt Lõi: Intelligence ≠ Reliability
| Model Capability | Systemic Failure (Khi Không Có Harness) |
|-----------------|----------------------------------------|
| ✅ Code generation tốc độ cao | ❌ Mất continuity trong tasks dài, multi-session |
| ✅ Reasoning advanced | ❌ Overreach & under-finish: làm lan man, không hoàn thành đúng scope |
| ✅ Context window rộng | ❌ Declare victory too early: dừng khi code "trông ổn", chưa test |

> 🎯 Bài học then chốt: Raw intelligence without structural enforcement là liability, không phải asset.

### Định Nghĩa Harness
> Harness = Một closed-loop working system được thiết kế để ổn định hành vi của agent thông qua: explicit rules, state management, và systematic verification.

❌ Không có harness:  Prompt → Model → Output → "Xong!" (nhưng có thể bug, mất context, sai scope)  ✅ Có harness: Goal (AGENTS.md) → Init (init.sh) → Execute → Feedback → Verify (Test Suite) → Handoff (claude-progress.md)

---

## 🧰 Bộ Công Cụ Harness: 4 Artifacts Cốt Lõi

Một harness vững chắc được xây từ 4 "primitives" — những file cấu hình đóng vai trò như luật chơi, checklist, và sổ ghi chép cho agent.

| Artifact | Vai Trò Chức Năng | Lợi Ích Cốt Lõi ("So What?") |
|----------|------------------|----------------------------|
| http://agents.md/ 📜 | Rule Definition: Định nghĩa Clear Objective + constraints + boundaries | Ngăn agent "overreach" — làm ngoài scope, vi phạm rules |
| http://init.sh/ ⚙️ | Environment Setup: Chuẩn bị môi trường trước khi agent bắt đầu | Đảm bảo agent không build trên nền "gãy" — stable, reproducible starting point |
| feature_list.json ✅ | Requirement Tracking: Granular checklist cho từng requirement | Ngăn "declare victory too early" — agent phải tick-off từng item trước khi báo xong |
| http://claude-progress.md/ 📝 | State Persistence: Ghi lại progress + context cho session sau | Giải quyết loss of continuity — repository, không phải model memory, là System of Record |

> 💡 Tư duy then chốt: Repository = System of Record. Nếu một state, requirement, hay progress marker không được document trong repo, nó không tồn tại đối với agent.

---

## 🔄 Agentic Workflow: 5 Phase Vòng Lặp Đáng Tin Cậy

Harness không phải là file config tĩnh — nó là một cyclical process ưu tiên verification over raw generation.

┌─────────────────────────────────────┐ │ 1️⃣ GOAL SETTING                    │ │ • Agent đọc AGENTS.md              │ │ • Internalize Clear Objective      │ │ • Hiểu rules + boundaries          │ └────────┬────────────────────────────┘          │          ▼ ┌─────────────────────────────────────┐ │ 2️⃣ INITIALIZATION                  │ │ • Execute init.sh                  │ │ • Install dependencies             │ │ • Verify environment stability     │ └────────┬────────────────────────────┘          │          ▼ ┌─────────────────────────────────────┐ │ 3️⃣ EXECUTION                       │ │ • Agent thực thi tasks             │ │ • Concurrently update feature_list.json │ │ • Reconcile current state vs requirements │ └────────┬────────────────────────────┘          │          ▼ ┌─────────────────────────────────────┐ │ 4️⃣ FEEDBACK LOOPS                  │ │ • Monitor CLI/Logs (Runtime Feedback) │ │ • Verify & QA via Test Suite       │ │ • ❌ Failed? → Encounter Issues → Auto-fix loop │ │ • ✅ Passed? → Proceed to Phase 5  │ └────────┬────────────────────────────┘          │          ▼ ┌─────────────────────────────────────┐ │ 5️⃣ STATE PERSISTENCE               │ │ • Cleanup & Handoff via claude-progress.md │ │ • Document: what's done, what's next │ │ • Ensure "Clean State" cho session sau │ └─────────────────────────────────────┘

> 🎯 Điểm then chốt: Agent không được phép chuyển sang Phase 5 nếu Test Suite chưa return "Passed". Verification là bắt buộc, không phải optional.

---

## 🚫 Prevention Over Cure: Giải Quyết 3 Failure Modes Kinh Điển

Ngay cả agents thông minh nhất cũng fail khi thiếu System of Record. Harness engineering giải quyết 3 vấn đề phổ biến:

### 1. "Tại Sao Agents Tuyên Bố 'Xong Rồi' Quá Sớm?"
| Vấn Đề | Nguyên Nhân Gốc | Giải Pháp Harness |
|--------|----------------|-----------------|
| Agent thấy không có error syntax → báo "done" | Thiếu granular verification | ✅ feature_list.json: Buộc agent tick-off từng requirement → "done" = mọi item đã check + test passed |

### 2. "Tại Sao Tasks Dài Bị Mất Continuity?"
| Vấn Đề | Nguyên Nhân Gốc | Giải Pháp Harness |
|--------|----------------|-----------------|
| Session timeout, context window shift → agent "quên" đang làm gì | Model memory là ephemeral | ✅ http://claude-progress.md/: Repository holds "state of the world" → session sau pick up exact thread, không context drift |

### 3. "Tại Sao Initialization Cần Một Phase Riêng?"
| Vấn Đề | Nguyên Nhân Gốc | Giải Pháp Harness |
|--------|----------------|-----------------|
| Agent bắt đầu trong environment inconsistent → build trên nền gãy | Thiếu stable starting point | ✅ http://init.sh/: Dedicated phase để prepare environment → reproducible, verified foundation |

> 💡 Triết lý: Prevention > Cure. Harness không chờ agent fail rồi fix — nó thiết kế system để prevent failure ngay từ đầu.

---

## 🧭 Checklist Triển Khai Harness: 6 Câu Hỏi Then Chốt

Trước khi deploy bất kỳ agentic harness nào, hãy tự hỏi:

✅ System of Record:     "Repository có phải là ultimate authority cho state và progress không?"  ✅ Explicit Boundaries:     "AGENTS.md có định nghĩa strict rules để ngăn agent overreach không?"  ✅ Initialization Integrity:     "Có init.sh dedicated để ensure environment stable trước khi execute không?"  ✅ Victory Prevention:     "feature_list.json có buộc agent verify từng requirement individually không?"  ✅ Closed-Loop Verification:     "Có mandatory 'Verify & QA' phase trigger auto-fix loop khi fail không?"  ✅ State Continuity:     "claude-progress.md có cung cấp clean handoff cho session sau không?"

> 🎯 Nếu bạn trả lời "Không" cho bất kỳ câu nào, harness của bạn chưa sẵn sàng cho production.

---

## ✨ 5 Bài Học Gây Ngạc Nhiên Từ Harness Engineering

### 1. Harness Không Làm Model "Thông Minh Hơn"
> "A harness doesn't 'make the model smarter'; rather, it establishes a closed-loop working system for the model."

- Harness là cơ chế cho reliability, không phải intelligence booster.
- Constraining agent với explicit rules không phải là limit — đó là provide structure to succeed.

### 2. "One Giant Instruction File" Là Fatal Flaw
- Mega-prompts → instruction drift, competing priorities, model confusion.
- Giải pháp: Harness Primitives — atomic, separate files cho từng responsibility (init, rules, tracking, state).

### 3. Observability Là Cho Agent, Không Chỉ Cho Human
- Agent cần "mắt và tai" để self-correct: CLI outputs, logs, test results.
- Embed End-to-End Testing vào internal loop → agent không declare victory cho đến khi có objective proof.

### 4. Repository = System of Record, Không Phải Chat History
- Chat-based interactions là ephemeral → mất continuity khi session change.
- Harness primitives (http://init.sh/, http://claude-progress.md/) biến work từ "conversation" thành persistent session.

### 5. Verification Loop Là Trái Tim Của Reliability
Encounter Issues → Auto-fix → Verify → (Pass? Done : Loop)
- Reliability là byproduct của closed-loop verification, không phải của prompt engineering.
- Nếu harness không facilitate auto-fix qua runtime observability, bạn chỉ có expensive autocomplete, không phải agent.

---

## 🎯 Key Takeaways (Bài Cốt Lõi)

1.  Reliability > Intelligence: Harness không làm model thông minh hơn — nó làm system đáng tin cậy hơn.
2.  Repository là System of Record: State, progress, requirements phải sống trong repo, không phải trong model memory.
3.  Closed-loop verification là bắt buộc: No "done" without test suite passing.
4.  Primitives > Prompts: http://agents.md/, http://init.sh/, feature_list.json, http://claude-progress.md/ là building blocks, không phải optional extras.
5.  Observability cho agent: Agent cần runtime feedback để self-correct — monitoring không phải chỉ cho human.
6.  Prevention over cure: Harness design để prevent failure modes, không chờ fail rồi fix.
7.  Environment Designer > Prompt Whisperer: Vai trò mới của developer: build system, không chỉ viết prompt.

---

## 🧭 Lộ Trình Áp Dụng Harness Engineering

Giai đoạn 1: Foundation (Tuần 1) ✅ Tạo AGENTS.md với Clear Objective + explicit rules ✅ Viết init.sh để setup environment stable ✅ Thiết lập feature_list.json với granular requirements  Giai đoạn 2: Workflow Integration (Tuần 2) ✅ Implement 5-phase lifecycle: Goal → Init → Execute → Feedback → Handoff ✅ Integrate test suite vào verification phase ✅ Setup auto-fix loop khi test fail  Giai đoạn 3: State Management (Tuần 3) ✅ Cấu hình claude-progress.md cho state persistence ✅ Test multi-session continuity: interrupt → resume → verify no context loss ✅ Document handoff protocol cho human-agent collaboration  Giai đoạn 4: Scale & Optimize (Tuần 4+) ✅ Monitor agent performance: success rate, auto-fix frequency, time-to-verify ✅ Refine primitives dựa trên learnings ✅ Share harness templates với team để standardize reliability

---

## 🎯 Lời Khuyên Cho AI Engineer

Khi thiết kế harness: ✅ Hỏi: "Agent có thể 'declare victory' mà chưa test không?" → Nếu có, thêm verification gate. ✅ Kiểm tra: "State có sống trong repo không?" → Nếu không, thêm claude-progress.md. ✅ Tránh: Mega-prompts — split thành primitives riêng biệt cho clarity. ✅ Test: Interrupt session giữa chừng → resume → verify continuity không mất. ✅ Measure: Track "time spent in auto-fix loop" — nếu cao, refine rules hoặc test suite.

> 🎯 Câu hỏi phản tư:
> "Nếu agent của bạn bị ngắt giữa chừng, session sau có thể pick up exact thread mà không cần human intervention không? Nếu không, harness của bạn chưa đủ 'closed-loop'."

---

## 🔮 Kết Luận: Từ Prompt Whispering Đến Environment Design

Harness Engineering đánh dấu sự chuyển dịch từ:
❌ "Làm sao để viết prompt tốt hơn?"  ✅ "Làm sao để thiết kế environment tốt hơn?"

> "If the AI is the engine, the harness is the chassis and the steering."

Bạn không cần model thông minh hơn. Bạn cần system đáng tin cậy hơn. Và harness chính là công cụ để build system đó.

---
Hãy bắt đầu hôm nay: Tạo http://agents.md/ cho project tiếp theo của bạn, thêm một feature_list.json với 3 requirements, và chạy http://init.sh/ trước khi agent bắt đầu. Một harness nhỏ hôm nay có thể save bạn hàng giờ debug và rework trong tương lai. 🚀🤖🔧