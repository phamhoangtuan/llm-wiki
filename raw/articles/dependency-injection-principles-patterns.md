# Dependency Injection

Finished date: 2026/05/31
Author: Steven van Deursen & Mark Seemann
Language: English
Type: Ebook
Number of pages: 643
Notes: # Cẩm Nang Dependency Injection: Nghệ Thuật Quản Lý Phụ Thuộc Và Vòng Đời Đối Tượng

Chào mừng bạn đến với hướng dẫn essential về Dependency Injection (DI) — không phải là một "thư viện magic", mà là kỷ luật thiết kế phần mềm giúp bạn xây dựng hệ thống dễ maintain, dễ test, và dễ mở rộng.

> 💡 Thông điệp cốt lõi: Dependency Injection không phải là đích đến. Nó là phương tiện để đạt được maintainability thông qua loose coupling — nơi các component có thể thay thế, intercept, hoặc mở rộng mà không gây "domino effect" phá vỡ toàn hệ thống.

Nếu ví việc xây phần mềm như nấu ăn, thì DI chính là Sauce Béarnaise của nghề bếp: khó làm lúc đầu, dễ "hỏng" nếu thiếu kỷ luật, nhưng khi master được, nó trở thành nền tảng cho mọi món ăn tinh tế khác.

---

## 🎯 Dependency Injection Là Gì? (Định Nghĩa Lại Cho Đúng)

> Dependency Injection = Một tập hợp các nguyên tắc và pattern thiết kế phần mềm giúp phát triển loosely coupled code.

### Phân Biệt Thuật Ngữ Quan Trọng
| Thuật Ngữ | Định Nghĩa | Ví Dụ |
|-----------|-----------|-------|
| Abstraction | Định nghĩa "cái gì" một service làm (interface/abstract class) | IPaymentProcessor, ILogger |
| Class/Component | Implementation cụ thể chứa behavior thực tế | StripePaymentProcessor, FileLogger |
| Dependency | Service/yêu cầu mà một class cần để hoạt động | OrderService cần IPaymentProcessor để xử lý thanh toán |

### 🧒 Analogies: Đứa Trẻ Và Tủ Lạnh
❌ Cách Cũ (Control Freak): Đứa trẻ tự mở tủ lạnh → lấy nước → có thể lấy nhầm đồ hết hạn, quên đóng cửa.  ✅ Cách Mới (Dependency Injection): Đứa trẻ nói: "Con cần đồ uống với bữa trưa." → Bố mẹ (infrastructure) cung cấp đồ uống phù hợp, an toàn.

> 🎯 Bài học: Class không nên "tự đi lấy" dependencies. Nó nên state a need, và infrastructure sẽ supply những gì cần thiết.

---

## 🔍 Phân Loại Dependencies: Cái Nào Cần Inject, Cái Nào Không?

Không phải mọi dependency đều cần DI. Hãy phân loại để áp dụng chiến lược phù hợp:

| Loại Dependency | Đặc Điểm | Quản Lý | Ví Dụ |
|----------------|----------|---------|-------|
| Stable Dependencies ✅ | • Có sẵn trong environment (standard libraries)<br>• Logic deterministic (toán học, string manipulation)<br>• Value Types không thay đổi theo context | New up internally — không cần DI | string, DateTime, Math.PI, List<T> |
| Volatile Dependencies ⚠️ | • Non-deterministic behavior (DateTime.Now, Random)<br>• Infrastructure/setup (database, file system, API calls)<br>• Chưa tồn tại ở thời điểm viết code | Bắt buộc inject để đảm bảo testability và stability | IDatabase, IHttpClient, IClock, IEmailSender |

> 💡 Rule of thumb: Nếu dependency làm cho class khó test hoặc khó reuse, đó là volatile dependency → cần inject.

---

## 🧭 3 Pattern Inject Chính: Chọn Đúng Cho Đúng Ngữ Cảnh

### 1. Constructor Injection (Primary Pattern) 🏆
Khi nào dùng? Cho mandatory dependencies — những thứ class không thể hoạt động nếu thiếu.

csharp // ✅ Đúng: Yêu cầu dependencies qua constructor public class OrderService {     private readonly IPaymentProcessor _payment;     private readonly ILogger _logger;          public OrderService(IPaymentProcessor payment, ILogger logger)     {         _payment = payment ?? throw new ArgumentNullException(nameof(payment));         _logger = logger ?? throw new ArgumentNullException(nameof(logger));     } } "So What?" Layer:
- ✅ Đảm bảo Class Invariant: Object không bao giờ tồn tại ở trạng thái invalid.
- ✅ Encapsulation: Dependencies được bảo vệ, không bị thay đổi từ bên ngoài.
- ❌ Tránh nhầm với Constrained Construction anti-pattern: Đừng thiết kế constructor chỉ để "làm hài lòng DI container".

---

### 2. Method Injection (Contextual Pattern) 🔄
Khi nào dùng? Khi dependency thay đổi theo từng call — không phải lúc nào cũng giống nhau.

csharp // ✅ Đúng: Dependency truyền qua parameter khi cần public class CurrencyConverter {     public decimal Convert(decimal amount, string from, string to, IExchangeRateProvider rateProvider)     {         var rate = rateProvider.GetRate(from, to);         return amount * rate;     } } "So What?" Layer:
- ✅ Linh hoạt cho varying execution context.
- ❌ Không dùng cho mandatory dependencies — sẽ làm method signature phức tạp, khó đọc.

---

### 3. Property Injection (Extensibility Pattern) 🎁
Khi nào dùng? Cho optional dependencies — class vẫn hoạt động nếu thiếu, nhưng có thể mở rộng behavior.

csharp // ✅ Đúng: Optional dependency qua property public class ReportGenerator {     public IEmailSender EmailSender { get; set; } // Optional          public void GenerateReport(ReportData data)     {         // ... generate report ...                  // Chỉ gửi email nếu đã được cấu hình         EmailSender?.Send(data.Recipient, data.Content);     } } "So What?" Layer:
- ✅ Extensibility model cho reusable libraries với "local defaults".
- ⚠️ Last resort để break cyclic dependencies (xem Section 5).
- ❌ Không dùng cho mandatory dependencies — class có thể crash nếu property chưa được set.

---

## 🏗️ Composition Root: Trái Tim Của Object Composition

> Composition Root = Vị trí duy nhất, tập trung trong application nơi toàn bộ object graph được wired together.

### Tại Sao Cần Composition Root?
- ✅ Centralize the "Control Freak": Thay vì mỗi class tự "new up" dependencies, tất cả được tập trung ở một chỗ.
- ✅ Maintain purity: Phần còn lại của application chỉ focus vào business logic, không lo về wiring.
- ✅ Single point of change: Thay đổi cấu hình dependency → chỉ sửa ở Composition Root.

### Implementation Mechanics
| Loại Application | Composition Root Location |
|-----------------|--------------------------|
| Console App | Main() method |
| http://asp.net/ Core | Startup.ConfigureServices() + custom controller activators |
| UWP/Xamarin | OnLaunched() hoặc application startup logic |

### Pure DI vs. DI Containers: Chọn Công Cụ Phù Hợp

| Tiêu Chí | Pure DI (Manual) | DI Container (Autofac, Simple Injector) |
|----------|---------------------|-------------------------------------------|
| Feedback Cycle | ✅ Compile-time errors — nhanh, type-safe | ❌ Runtime errors — khó debug hơn |
| Transparency | ✅ Rõ ràng, dễ trace object graph | ❌ "Magic" auto-wiring — khó hiểu với newbies |
| Complexity | ❌ Manual wiring tốn công với graph lớn | ✅ Auto-wiring tiết kiệm thời gian |
| Risk | ✅ Không phụ thuộc third-party library | ❌ Leaky abstractions, container-specific bugs |

> 🎯 Verdict:
> - Bắt đầu với Pure DI để học fundamentals và giữ type safety.
> - Chuyển sang DI Container khi manual wiring trở nên quá tốn kém và error-prone.

---

## ⏳ Object Lifetime Management: Quản Lý Vòng Đời Dependencies

Quản lý lifetime là trách nhiệm duy nhất của Composition Root. Consumer không bao giờ được biết hoặc quản lý lifetime của dependencies.

### Lifestyle Catalog
| Lifestyle | Định Nghĩa | Khi Nào Dùng | Ví Dụ |
|-----------|-----------|-------------|-------|
| Singleton 🔒 | Một instance duy nhất cho toàn application lifetime | Statelesss services, caching, configuration | ILogger, IConfiguration, IMemoryCache |
| Transient 🔄 | Instance mới cho mỗi request từ consumer | Stateful services, short-lived operations | IHttpContextAccessor, IDbConnection |
| Scoped 🌐 | Một instance shared trong logical context (ví dụ: một web request) | Services cần maintain state trong request | IUnitOfWork, ICurrentUser |

### ⚠️ Captive Dependency: Lỗi Chết Người
Định nghĩa: Inject một short-lived dependency (Transient/Scoped) vào một long-lived component (Singleton).

csharp // ❌ SAI: Scoped dependency bị "capture" bởi Singleton public class CachedDataService // Singleton {     public CachedDataService(IDbConnection connection) // Scoped!     {         // Connection bị giữ lại quá lâu → stale data, memory leak     } } Hậu quả:
- 🔄 Stale data: Dependency không được refresh khi context thay đổi.
- 💥 Memory leak: Object không được dispose đúng lúc.
- 🐛 Concurrency bugs: Shared state gây race conditions.

Directive:
> "Never inject a Scoped or Transient dependency into a Singleton."

---

## 🚫 Anti-Patterns & Code Smells: Những Cái Bẫy Cần Tránh

### 1. Service Locator Anti-Pattern 🎭
csharp // ❌ SAI: Class tự "hỏi" container để lấy dependencies public class OrderService {     public void ProcessOrder()     {         var payment = Container.GetService<IPaymentProcessor>(); // 🚫         payment.Charge();     } } "So What?" Layer:
- ❌ Obscures requirements: Không biết class cần gì nếu không đọc implementation.
- ❌ Hard to test: Phải setup container mock phức tạp.
- ❌ Violates DIP: Class phụ thuộc vào container, không phải abstraction.

---

### 2. Ambient Context Anti-Pattern 🌐
csharp // ❌ SAI: Global static access point public class OrderService {     public void Log(string message)     {         Logger.Global.Log(message); // 🚫 Global state khó intercept     } } "So What?" Layer:
- ❌ Global state khó replace cho testing.
- ❌ Khó intercept cho cross-cutting concerns (logging, auditing).
- ✅ Refactor thành injected abstraction: ILogger.

---

### 3. Control Freak Anti-Pattern 🎮
csharp // ❌ SAI: Class tự "new up" volatile dependencies public class OrderService {     private readonly SqlDatabase _db = new SqlDatabase(); // 🚫 Hard-coded implementation          public void SaveOrder(Order order)     {         _db.Save(order);     } } "So What?" Layer:
- ❌ Locks into specific implementation — khó thay đổi, khó test.
- ✅ Acceptable cho Stable Dependencies (string, List<T>).
- ❌ Violation cho Volatile Dependencies — bắt buộc inject.

---

### 4. Code Smells Cần Refactor
| Smell | Dấu Hiệu | Giải Pháp |
|-------|----------|-----------|
| Constructor Over-injection | Constructor có >4-5 parameters | • Refactor theo Facade Service<br>• Sử dụng Domain Events để decouple |
| Constrained Construction | Mọi class phải có constructor mặc định để container hoạt động | • Preserve encapsulation — đừng compromise class design cho library |
| Cyclic Dependencies | A → B → A (circular reference) | • Refactor shared logic vào class thứ 3<br>• Last resort: Property Injection để break loop |

---

## 🧱 SOLID Principles: Nền Tảng Cho DI Thành Công

DI không tồn tại trong chân không — nó được driving bởi SOLID principles:

| Nguyên Tắc | Vai Trò Trong DI | Ví Dụ Thực Tế |
|------------|-----------------|--------------|
| S - Single Responsibility | Đảm bảo class chỉ có một lý do để change → dễ inject dependencies | OrderService chỉ xử lý order logic, không lo logging → inject ILogger |
| O - Open/Closed | Code open for extension, closed for modification → enable Interception | Decorate IPaymentProcessor với CachingPaymentProcessor mà không sửa code gốc |
| L - Liskov Substitution | Abstraction có thể replace bằng bất kỳ implementation nào → enable Polymorphism | Thay StripePaymentProcessor bằng PayPalPaymentProcessor mà không sửa consumer |
| I - Interface Segregation | Interfaces nhỏ, specific → dễ intercept specific methods | IReadableRepository và IWritableRepository thay vì IRepository béo |
| D - Dependency Inversion | High-level và low-level modules cùng depend vào abstractions → enable DI | OrderService (high) và SqlDatabase (low) cùng depend vào IDatabase |

> 🎯 Climax của DI: Khi follow SOLID, bạn đạt được Interception — khả năng "wrap" class với cross-cutting concerns (logging, security, caching) mà consumer không hề biết.

csharp // Decorator Pattern: Wrap IPaymentProcessor với caching public class CachingPaymentProcessor : IPaymentProcessor {     private readonly IPaymentProcessor _inner;     private readonly IMemoryCache _cache;          public CachingPaymentProcessor(IPaymentProcessor inner, IMemoryCache cache)     {         _inner = inner;         _cache = cache;     }          public async Task<PaymentResult> Charge(PaymentRequest request)     {         // Check cache trước khi gọi inner processor         return await _cache.GetOrCreateAsync(request.CacheKey, async entry =>             await _inner.Charge(request)         );     } } 

---

## ✨ Key Takeaways (Bài Cốt Lõi)

1.  DI là phương tiện, không phải đích đến: Mục tiêu cuối cùng là maintainability thông qua loose coupling.
2.  Phân loại dependencies: Stable (new internally) vs. Volatile (bắt buộc inject).
3.  Constructor Injection là default: Cho mandatory dependencies — đảm bảo class invariant.
4.  Composition Root là bắt buộc: Centralize object composition để maintain purity của application.
5.  Quản lý lifetime cẩn thận: Tránh Captive Dependency — không inject Scoped/Transient vào Singleton.
6.  Tránh anti-patterns: Service Locator, Ambient Context, Control Freak — tất cả đều phá vỡ loose coupling.
7.  SOLID là nền tảng: DI chỉ hoạt động tốt khi follow SRP, OCP, LSP, ISP, DIP.
8.  Pure DI trước, Container sau: Học fundamentals với manual wiring, chỉ dùng container khi thực sự cần.

---

## 🧭 Lộ Trình Áp Dụng DI Cho Project Của Bạn

Giai đoạn 1: Foundation (Tuần 1-2) ✅ Phân loại dependencies trong codebase: Stable vs. Volatile ✅ Refactor volatile dependencies thành constructor injection ✅ Tạo Composition Root đơn giản ở entry point  Giai đoạn 2: Best Practices (Tuần 3-4) ✅ Áp dụng SOLID principles để refactor classes có constructor over-injection ✅ Implement object lifetime management (Singleton/Transient/Scoped) ✅ Viết unit tests cho classes với mocked dependencies  Giai đoạn 3: Advanced Patterns (Tuần 5-6) ✅ Implement Decorator pattern cho cross-cutting concerns (logging, caching) ✅ Refactor cyclic dependencies bằng Property Injection (last resort) ✅ Evaluate DI container nếu manual wiring trở nên quá phức tạp  Giai đoạn 4: Scale & Maintain (Tuần 7+) ✅ Document dependency graph và lifetime decisions ✅ Setup CI/CD để catch DI-related bugs sớm ✅ Train team trên DI principles để maintain consistency

---

## 🎯 Lời Khuyên Từ Senior Architect

Khi design system với DI: ✅ Hỏi: "Class này có thực sự cần dependency này không? (SRP check)" ✅ Kiểm tra: "Dependency này là Stable hay Volatile? Có cần inject không?" ✅ Tránh: Service Locator, Ambient Context, Control Freak — tất cả đều phá loose coupling ✅ Test: Viết unit test trước khi implement — nếu khó mock, design cần refactor ✅ Document: Ghi lại lifetime decisions ở Composition Root để tránh Captive Dependency

> 🎯 Câu hỏi phản tư:
> "Nếu ngày mai business requirement thay đổi, codebase của bạn có dễ dàng replace một implementation mà không cần sửa 10 files khác không?"

---

## 🔮 Kết Luận: DI Là Kỷ Luật, Không Phải Phép Màu

Dependency Injection không làm bạn thành architect overnight. Nhưng nó cung cấp framework tư duy để:
- ✅ Xây system dễ maintain, dễ test, dễ mở rộng
- ✅ Tránh technical debt từ tight coupling
- ✅ Enable advanced patterns như Interception và AOP

> "Proper DI is the disciplined management of an application's entire structural integrity."

Hãy bắt đầu nhỏ: chọn một class, refactor dependencies thành constructor injection, và cảm nhận sự khác biệt khi viết unit test. Một bước nhỏ hôm nay có thể save bạn hàng giờ debug trong tương lai.

---
Chúc bạn master được nghệ thuật Dependency Injection — nơi mỗi dependency không phải là gánh nặng, mà là một cơ hội để xây system linh hoạt, bền vững, và đáng tự hào. 🚀🔧✨