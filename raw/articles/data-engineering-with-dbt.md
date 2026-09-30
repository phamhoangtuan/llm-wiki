# Data Engineering with dbt

Finished date: 2026/05/08
Author: Roberto Zagni
Language: English
Type: Ebook
Number of pages: 603
Notes: # Cẩm Nang dbt: Kết Thúc Kỷ Nguyên Data Silo, Khai Mở Modern Data Stack

Chào mừng bạn đến với hướng dẫn essential về cuộc cách mạng dbt — công cụ đang định hình lại cách chúng ta xây dựng, vận hành và tin tưởng vào dữ liệu doanh nghiệp.

> 💡 Thông điệp cốt lõi: dbt không chỉ là một tool. Nó là tư duy mới: biến data engineering thành software engineering, biến analyst thành analytics engineer, và biến "ống dẫn dữ liệu" thành "nhà máy lọc thông tin" đáng tin cậy.

Nếu ví dữ liệu như dầu thô, thì trước đây chúng ta chỉ biết khoan và vận chuyển. dbt giúp chúng ta lọc, tinh chế, và đóng chai — để mọi người trong tổ chức đều có thể sử dụng một cách an toàn và hiệu quả.

---

## 🎯 Bối Cảnh: Tại Sao Chúng Ta Cần Một Cuộc "Data Renaissance"?

| Vấn Đề Cũ | Giải Pháp Mới với dbt |
|-----------|----------------------|
| ❌ Data silo: Kỹ sư và analyst làm việc riêng lẻ | ✅ Analytics Engineer: Vai trò cầu nối, sở hữu transformation layer |
| ❌ Logic nghiệp vụ ẩn trong spreadsheet, stored procedures | ✅ Logic minh bạch trong SQL + version control |
| ❌ Pipeline brittle, khó maintain, đầy technical debt | ✅ DataOps: Áp dụng software engineering best practices vào data |
| ❌ "Strong boundaries" trong database tạo rigid silos | ✅ "Soft boundaries" trong cloud warehouse + dbt automation |

> 🔄 Sự thay đổi không nằm ở công cụ, mà nằm ở tư duy: từ "di chuyển dữ liệu" sang "tinh chế thông tin".

---

## 🚀 5 Takeaways Cốt Lõi: Từ Lý Thuyết Đến Thực Chiến

### 🔹 Takeaway 1: Sự Trỗi Dậy Của Analytics Engineer
Vai trò mới, tư duy mới, kết quả mới.Truyền thống: Data Engineer (plumber) → [No Man's Land] → Analyst (storyteller)  Hiện đại với dbt: Data Engineer → Analytics Engineer → Analyst                    ↓            Sở hữu transformation layer            Áp dụng software engineering mindset            Biến raw data thành trusted dataAnalytics Engineer làm gì?
- ✅ Viết SQL transformations có cấu trúc, reusable
- ✅ Áp dụng testing, documentation, version control cho data code
- ✅ Bridge the gap: Hiểu cả technical plumbing lẫn business storytelling

> 💡 Ví dụ: Thay vì analyst phải tự viết query phức tạp để tính "customer lifetime value", analytics engineer xây dựng model dim_customers đã tính sẵn, được test, documented — analyst chỉ cần SELECT * FROM dim_customers.

---

### 🔹 Takeaway 2: SQL Là Ngôn Ngữ Phổ Quát — Với "Secret Sauce" Của dbt
SQL đã tồn tại từ thập niên 80, nhưng dbt khiến nó trở nên mạnh mẽ hơn bao giờ hết.

#### Jinja Templating: "Gia Vị" Biến SQL Thành Superpower
sql -- Thay vì viết lặp đi lặp lại: CREATE VIEW revenue_usd AS SELECT amount * 1.2 AS amount_usd FROM orders; CREATE VIEW revenue_eur AS SELECT amount * 0.9 AS amount_eur FROM orders;  -- Với Jinja macro trong dbt: {% macro convert_currency(amount, currency) %}   {{ amount }} * {{ var('exchange_rates')[currency] }} {% endmacro %}  -- Sử dụng: SELECT    {{ convert_currency('amount', 'USD') }} AS amount_usd,   {{ convert_currency('amount', 'EUR') }} AS amount_eur FROM orders 

#### Declarative Logic: Mô Tả "Cái Gì", dbt Lo "Làm Sao"
| Cách Cũ (Imperative) | Cách Mới với dbt (Declarative) |
|---------------------|-------------------------------|
| Viết DDL thủ công: CREATE TABLE, CREATE VIEW | Mô tả model trong SQL, dbt tự sinh DDL |
| Quản lý dependencies bằng tay | dbt tự động build DAG từ ref() |
| Test logic bằng query ad-hoc | Định nghĩa tests trong YAML, chạy tự động |

> 🎯 Lợi ích: Non-technical stakeholders có thể đọc và hiểu business logic trong SQL, trong khi engineers vẫn có thể biểu diễn transformations phức tạp một cách ngắn gọn.

---

### 🔹 Takeaway 3: Data Engineering = Software Engineering (DataOps)
"Copy and paste kills your future self." — Triết lý then chốt của DataOps.

#### 3 Trụ Cột Của DataOps Với dbt
| Trụ Cột | Thực Hành Với dbt | Lợi Ích |
|---------|------------------|---------|
| Version Control 📦 | Mọi model, test, config nằm trong Git (GitHub/GitLab) | Track changes, collaborate, rollback dễ dàng |
| Quality Assurance 🧪 | Automated tests: unique, not_null, relationships, custom tests | Catch data issues before they reach stakeholders |
| Modularity 🧱 | Break monolithic scripts thành small, reusable models + macros | Giảm technical debt, dễ maintain, dễ onboard người mới |

#### Ví Dụ: Testing Trong dbt
yaml # models/schema.yml version: 2  models:   - name: dim_customers     columns:       - name: customer_id         tests:           - unique           - not_null       - name: email         tests:           - relationships:               to: ref('stg_users')               field: user_id 

> 💡 Kết quả: Thay vì "firefighting" khi dashboard báo số sai, team có thể prevent issues từ gốc — chuyển từ reactive sang proactive.

---

### 🔹 Takeaway 4: "Soft Boundaries" Trong Cloud Warehousing
Tư duy tổ chức dữ liệu thay đổi khi chuyển từ on-prem sang cloud.

| Hệ Thống Cũ (PostgreSQL) | Cloud-Native (Snowflake + dbt) |
|-------------------------|-------------------------------|
| Database = "Strong boundary": rigid, hard to reorganize | Database/schema = "Soft folders": flexible, organizational |
| Security & access quản lý thủ công, phức tạp | dbt automation + hierarchical RBAC: linh hoạt nhưng vẫn secure |
| Scale vertically: nâng cấp server | Scale horizontally: thêm resources on-demand |

#### Ví Dụ: Tổ Chức Project dbt Với Soft Boundaries
my_dbt_project/ ├── models/ │   ├── staging/          # Raw → Cleaned (soft boundary: staging schema) │   ├── intermediate/     # Business logic (soft boundary: intermediate schema)   │   └── marts/           # Business-ready (soft boundary: analytics schema) │       ├── finance/ │       ├── marketing/ │       └── product/

> 🎯 Lợi ích: Team có thể tổ chức code theo business domain mà không bị giới hạn bởi rigid database structures — scale ngang mà vẫn maintainable.

---

### 🔹 Takeaway 5: Modeling Là Hành Trình 3 Tầng Trừu Tượng
Technical storage phải align với business reality. Zagni đề xuất framework Pragmatic Data Platform (PDP):

1️⃣ Conceptual Models    ↓    "Business processes & entities là gì?"    Ví dụ: Customer, Order, Product, Revenue  2️⃣ Logical Models      ↓    "Mối quan hệ và attributes ra sao?"    Ví dụ: Customer 1-n Orders, Order m-n Products  3️⃣ Physical Models    ↓    "Implement thế nào trong database?"    Ví dụ: dim_customers, fct_orders, bridge_order_products

#### Tại Sao Hành Trình Này Quan Trọng?
| Nếu Bỏ Qua | Hậu Quả |
|------------|---------|
| Nhảy thẳng vào Physical | Model kỹ thuật đúng nhưng business không hiểu, không dùng được |
| Không có Conceptual | Mất alignment giữa tech và business, dẫn đến rework |
| Thiếu Logical | Relationships mơ hồ, analytics sai lệch |

> 💡 Kết quả: Khi model với intent, business users có thể tự build reports với total confidence — vì họ hiểu logic đằng sau dữ liệu.

---

## ✨ Key Takeaways (Bài Cốt Lõi)

1.  Analytics Engineer là vai trò then chốt: Cầu nối giữa technical plumbing và business storytelling, sở hữu transformation layer.
2.  SQL + Jinja = Superpower: Declarative logic giúp mô tả "cái gì", dbt lo "làm sao" — tăng năng suất, giảm boilerplate.
3.  DataOps là bắt buộc: Version control + automated testing + modularity = maintainable, scalable data platform.
4.  Soft boundaries > Strong boundaries: Cloud warehouse + dbt automation cho phép tổ chức linh hoạt mà vẫn secure.
5.  Modeling là hành trình 3 tầng: Conceptual → Logical → Physical đảm bảo technical implementation align với business goals.
6.  "Copy and paste kills your future self": Maintainability là metric thành công duy nhất — đừng hy vọng ngắn hạn cho technical debt dài hạn.
7.  dbt không phải silver bullet: Nó là enabler — thành công phụ thuộc vào tư duy DataOps và collaboration của team.

---

## 🧭 Lộ Trình Áp Dụng dbt Cho Team Của Bạn

Giai đoạn 1: Foundation (Tuần 1-2) ✅ Cài đặt dbt Core/Cloud, kết nối với cloud warehouse (Snowflake/BigQuery) ✅ Import 1-2 source tables, viết staging models đơn giản ✅ Áp dụng basic tests: unique, not_null  Giai đoạn 2: DataOps Basics (Tuần 3-4) ✅ Đưa toàn bộ project vào Git, thiết lập PR workflow ✅ Viết documentation cho models, columns trong schema.yml ✅ Thêm custom tests cho business logic quan trọng  Giai đoạn 3: Scaling & Collaboration (Tuần 5-6) ✅ Tổ chức models theo 3-tier: staging → intermediate → marts ✅ Tạo reusable macros cho logic lặp lại (convert_currency, calculate_ltv) ✅ Thiết lập CI/CD: auto-run tests on PR, deploy on merge  Giai đoạn 4: Advanced & Governance (Tuần 7+) ✅ Áp dụng incremental models cho large tables ✅ Implement exposure tracking: biết dashboard nào dùng model nào ✅ Setup monitoring: alert khi tests fail, data freshness delayed

---

## 🎯 Lời Khuyên Từ Người Đã Đi Trước

Khi bắt đầu với dbt: ✅ Bắt đầu nhỏ: 1 source, 3 models, 5 tests — chứng minh giá trị trước khi scale. ✅ Document as you code: Viết description ngay khi tạo model, đừng để "sau này làm". ✅ Review PRs kỹ: Data code cũng quan trọng như application code — đừng merge vội. ✅ Involve business early: Cho analyst/stakeholder xem models, lấy feedback trước khi deploy. ✅ Measure success by trust: Không phải bằng số models, mà bằng mức độ business tự tin dùng data.

> 🎯 dbt không làm bạn thành analytics engineer overnight. Nhưng nó cung cấp framework để bạn phát triển tư duy đó — từng model, từng test, từng collaboration một.

---

## 🔮 Tương Lai: Beyond dbt

dbt là core của Modern Data Stack, nhưng không phải là toàn bộ bức tranh:

Modern Data Stack Ecosystem:                      ┌─────────────────┐ │   Ingestion     │ → Fivetran, Airbyte ├─────────────────┤ │   Storage       │ → Snowflake, BigQuery, Databricks   ├─────────────────┤ │ Transformation  │ → ✅ dbt (THE CORE) ✅ ├─────────────────┤ │   Orchestration │ → Airflow, Dagster, Prefect ├─────────────────┤ │   BI/Analytics  │ → Looker, Metabase, Superset └─────────────────┘

> 💡 dbt kết nối các mảnh ghép: Nó biến raw data từ ingestion thành trusted data cho BI — mà vẫn maintainable nhờ DataOps.

---

## Kết Luận: Xây Dựng Cho Tương Lai, Bắt Đầu Từ Hôm Nay

> "The goal of modern data engineering isn't just to handle 'big data' — it is to build simple, future-proof, and maintainable platforms."

Câu hỏi then chốt cho bạn và team:
❓ Stack hiện tại của bạn là:    A) Collection of disconnected silos?      B) Collaborative ecosystem designed to evolve?

Nếu câu trả lời là A, đừng lo — công cụ cho B đã nằm trong tay bạn. dbt, cloud warehouse, Git, và tư duy DataOps là những viên gạch đầu tiên.

> 🚀 Hãy bắt đầu pragmatically: Chọn 1 use case nhỏ, áp dụng 3-tier modeling, viết 5 tests đầu tiên. Mỗi bước nhỏ hôm nay là một bước gần hơn đến việc kết thúc kỷ nguyên data silo.

---
Chúc bạn xây dựng được những data platform không chỉ mạnh về kỹ thuật, mà còn đáng tin về nghiệp vụ — nơi mọi người trong tổ chức đều có thể khai thác dữ liệu với self-service confidence. 📊✨🔧