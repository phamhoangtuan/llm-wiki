# Programming Kubernetes

Finished date: 2026/05/07
Author: Stefan Schimanski & Michael Hausenblas
Language: English
Type: Ebook
Number of pages: 244
Notes: # Cẩm Nang Programming Kubernetes: Xây Dựng Ứng Dụng "Native" Cho Cluster

Chào mừng bạn đến với hướng dẫn essential về Programming Kubernetes — nghệ thuật xây dựng những ứng dụng không chỉ chạy trên Kubernetes, mà còn hiểu và giao tiếp trực tiếp với Kubernetes.

> 💡 Tư duy cốt lõi: Đừng chỉ deploy ứng dụng lên Kubernetes. Hãy xây dựng ứng dụng Kubernetes-native — những chương trình biết "nói chuyện" với API server, tận dụng declarative state management để đạt được portability và automation tối đa.

Nếu ví Kubernetes như một hệ điều hành cho cloud, thì "programming Kubernetes" chính là viết những ứng dụng chạy native trên hệ điều hành đó — thay vì chỉ chạy như một process thông thường.

---

## 🎯 Programming Kubernetes Là Gì?
Programming Kubernetes = Phát triển các ứng dụng tương tác trực tiếp với Kubernetes API server để query hoặc update trạng thái của cluster resources.

| Cách Tiếp Cận | Mô Tả | Ví Dụ |
|--------------|-------|-------|
| Chạy ứng dụng trên K8s 📦 | Deploy software có sẵn (WordPress, MySQL) lên cluster | kubectl apply -f deployment.yaml |
| Programming Kubernetes 🔧 | Xây ứng dụng aware nó đang chạy trên K8s, dùng APIs để quản lý state | Viết Controller tự động scale database khi load tăng |

> 🎯 Sự khác biệt: Một bên là "khách thuê nhà", một bên là "thợ xây biết đọc bản thiết kế của chính ngôi nhà".

---

## 🔄 Controllers & Control Loop: Trái Tim Của Automation
Controller là component thực thi control loop — vòng lặp quan sát và điều chỉnh để đưa cluster về desired state.

### 3 Bước Của Control Loop
┌─────────────────────────────────┐ │  1️⃣ READ: Quan sát trạng thái   │ │     • Watch events từ API server│ │     • Phát hiện changes/drift   │ └────────┬────────────────────────┘          │          ▼ ┌─────────────────────────────────┐ │  2️⃣ CHANGE: Hành động điều chỉnh│ │     • Tạo/sửa/xóa resources     │ │     • Tương tác với external systems │ └────────┬────────────────────────┘          │          ▼ ┌─────────────────────────────────┐ │  3️⃣ UPDATE: Báo cáo kết quả    │ │     • Update .status trong API  │ │     • Ghi logs, emit metrics    │ └─────────────────────────────────┘

### Ví Dụ Thực Tế: Database Rebalance Controller
go // Pseudocode minh họa control loop for {     // 1. READ: Watch sự kiện thay đổi trên Database CR     event := watchDatabaseEvents()          // 2. CHANGE: Nếu cần rebalance, tạo mới pods     if event.needsRebalance {         createNewReplicaPods(event.cluster)         updateLoadBalancerConfig(event.cluster)     }          // 3. UPDATE: Report status về API server     updateDatabaseStatus(event.cluster, "Rebalanced") } 

> 💡 Analogy: Control loop giống như bộ điều nhiệt (thermostat): Đọc nhiệt độ → Bật/tắt máy lạnh → Cập nhật trạng thái hiển thị.

---

## 🤖 Operators: Controllers "Biết Nghiệp Vụ"
Operator là một lớp controller đặc biệt, do CoreOS giới thiệu, mã hóa domain-specific operational knowledge vào software.

### Operator = CRD + Custom Controller
| Thành Phần | Vai Trò | Ví Dụ: PostgreSQL Operator |
|------------|---------|---------------------------|
| Custom Resource Definition (CRD) 📋 | Định nghĩa schema cho resource đặc thù của ứng dụng | kind: PostgreSQLCluster với fields: replicas, storageSize, version |
| Custom Controller ⚙️ | Supervise resources đó, quản lý lifecycle | Tự động backup, failover, upgrade version khi phát hiện thay đổi |

### Lợi Ích Của Operator
yaml # Thay vì chạy 10 lệnh kubectl thủ công để deploy database: apiVersion: database.example.com/v1 kind: PostgreSQLCluster metadata:   name: prod-db spec:   replicas: 3   storageSize: 100Gi   backupSchedule: "0 2 * * *"  # Backup lúc 2h sáng hàng ngày 
→ Operator tự động handle: provisioning, scaling, backup, recovery, upgrade.

> 🎯 Operator biến "tribal knowledge" của SRE thành code có thể version-control, test, và reuse.

---

## 🛠️ Technical Building Blocks: Công Cụ Để "Nói Chuyện" Với K8s

### Ngôn Ngữ: Go Là Lựa Chọn Hàng Đầu
*   Kubernetes itself viết bằng Go → ecosystem libraries tối ưu cho Go.
*   Tuy nhiên, có client libraries cho Python, Java, JavaScript nếu cần.

### Thư Viện Cốt Lõi
| Library | Mục Đích | Ví Dụ Sử Dụng |
|---------|----------|--------------|
| client-go 🚀 | "Standard library" để tương tác với Kubernetes API | clientset.CoreV1().Pods(namespace).Get(ctx, name, options) |
| API Machinery ⚙️ | Building blocks để implement Kubernetes-like APIs | Định nghĩa Kinds (types), Resources (HTTP paths), Schemes (mapping Go types ↔ Kinds) |

### Ví Dụ: Dùng client-go Để List Pods
go import (     metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"     "k8s.io/client-go/kubernetes" )  func listRunningPods(clientset *kubernetes.Clientset, namespace string) error {     pods, err := clientset.CoreV1().Pods(namespace).List(context.TODO(), metav1.ListOptions{         FieldSelector: "status.phase=Running",     })     if err != nil {         return err     }          for _, pod := range pods.Items {         fmt.Printf("Pod: %s, Node: %s\\n", pod.Name, pod.Spec.NodeName)     }     return nil } 

> 💡 Pro Tip: Luôn dùng informers và caches từ client-go thay vì poll API trực tiếp → giảm load trên API server.

---

## 🔌 Extension Patterns: Mở Rộng Kubernetes Theo Cách Của Bạn
Kubernetes được thiết kế để mở rộng. Dưới đây là 3 patterns chính:

### 1. Custom Resources (CRDs) — Phổ Biến Nhất
*   Khi nào dùng? Khi bạn cần thêm resource type mới với schema tùy chỉnh.
*   Ưu điểm: Dễ implement, tích hợp sẵn với kubectl, RBAC, validation.
*   Hạn chế: Performance có thể bị giới hạn với workload rất lớn.

yaml # Ví dụ: Định nghĩa CRD cho "WebApp" apiVersion: apiextensions.k8s.io/v1 kind: CustomResourceDefinition metadata:   name: webapps.example.com spec:   group: example.com   versions:     - name: v1       schema:         openAPIV3Schema:           type: object           properties:             spec:               type: object               properties:                 replicas:                   type: integer                 image:                   type: string   scope: Namespaced   names:     plural: webapps     singular: webapp     kind: WebApp 

### 2. Custom API Servers — Cho Use Case Phức Tạp
*   Khi nào dùng? Khi CRDs quá hạn chế: cần custom storage backend, subresources, hoặc performance cao.
*   Trade-off: Phức tạp hơn nhiều để build và maintain.

### 3. Webhooks — Dynamic Admission Control
*   Mutating Webhook: Sửa đổi request trước khi lưu vào etcd (ví dụ: inject sidecar container).
*   Validating Webhook: Từ chối request không hợp lệ (ví dụ: chặn image từ registry không được phép).

yaml # Ví dụ: Validating Webhook chặn image không từ trusted registry apiVersion: admissionregistration.k8s.io/v1 kind: ValidatingWebhookConfiguration metadata:   name: trust-registry.example.com webhooks:   - name: validate-images.example.com     rules:       - operations: ["CREATE", "UPDATE"]         apiGroups: [""]         apiVersions: ["v1"]         resources: ["pods"]     clientConfig:       service:         namespace: webhook-system         name: validation-service         path: "/validate" 

---

## 🏭 Production-Ready: Đóng Gói, Bảo Mật, Quan Sát
Viết code chạy được là một chuyện. Deploy production là chuyện khác.

### 1. Packaging & Distribution
| Công Cụ | Khi Nào Dùng | Lợi Ích |
|---------|-------------|---------|
| Helm 📦 | Ứng dụng phức tạp, nhiều resources, cần versioning | Templating, rollback, dependency management |
| Kustomize 🎨 | Customize manifests cho nhiều môi trường (dev/staging/prod) | No templating language, native kubectl support |

### 2. RBAC & Security
*   Nguyên tắc least privilege: Chỉ grant permissions tối thiểu cần thiết.
*   ServiceAccount riêng cho mỗi controller/operator.
*   Validate input từ CRDs để tránh injection attacks.

yaml # Ví dụ: RBAC tối giản cho Database Operator apiVersion: rbac.authorization.k8s.io/v1 kind: Role metadata:   name: database-operator rules:   - apiGroups: ["database.example.com"]     resources: ["postgresqlclusters"]     verbs: ["get", "list", "watch", "update", "patch"]   - apiGroups: [""]     resources: ["pods", "services"]     verbs: ["create", "get", "delete"] 

### 3. Observability: Logging, Metrics, Tracing
*   Structured logging: Dùng JSON logs để dễ parse và query.
*   Metrics: Export Prometheus metrics cho control loop latency, error rates, reconciliation counts.
*   Tracing: Dùng OpenTelemetry để trace request qua nhiều components.

go // Ví dụ: Export metrics cho controller var (     reconciliationsTotal = prometheus.NewCounterVec(         prometheus.CounterOpts{             Name: "controller_reconciliations_total",             Help: "Total number of reconciliation attempts",         },         []string{"controller", "result"}, // result: success, error     ) )  func (r *Reconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {     start := time.Now()     err := r.doReconcile(ctx, req)          reconciliationsTotal.WithLabelValues(r.Name, resultLabel(err)).Inc()     reconcileDuration.WithLabelValues(r.Name).Observe(time.Since(start).Seconds())          return ctrl.Result{}, err } 

---

## ✨ Key Takeaways (Bài Cốt Lõi)

1.  Native > Hosted: Programming Kubernetes là xây ứng dụng hiểu K8s, không chỉ chạy trên K8s.
2.  Control Loop là trái tim: READ → CHANGE → UPDATE là pattern cốt lõi cho mọi automation.
3.  Operators mã hóa tri thức nghiệp vụ: Biến "cách vận hành thủ công" thành code tự động, tái sử dụng được.
4.  Go + client-go là combo mạnh nhất: Tận dụng ecosystem chính thống của Kubernetes.
5.  Mở rộng có chiến lược: CRDs cho đa số use cases, Custom API Servers cho edge cases, Webhooks cho validation/mutation.
6.  Production-ready cần 3 trụ: Packaging (Helm/Kustomize) + Security (RBAC) + Observability (logs/metrics/traces).
7.  Think declaratively: Bạn mô tả desired state, controller lo phần how — đó là sức mạnh thực sự của Kubernetes.

---

## 🧭 Lộ Trình Học Programming Kubernetes

Giai đoạn 1: Foundation (Tuần 1-2) ✅ Hiểu Kubernetes API basics: Resources, Verbs, Watch ✅ Cài đặt Go + client-go, viết script list/get pods đơn giản ✅ Đọc source code của một controller đơn giản (ví dụ: sample-controller repo)  Giai đoạn 2: Build Controller (Tuần 3-4) ✅ Implement control loop cơ bản: watch → reconcile → update status ✅ Thêm logging và metrics để debug và monitor ✅ Test với kind/minikube trước khi deploy thật  Giai đoạn 3: Operator & CRDs (Tuần 5-6) ✅ Định nghĩa CRD cho ứng dụng của bạn ✅ Viết controller quản lý lifecycle của custom resource ✅ Áp dụng RBAC tối thiểu, đóng gói với Helm/Kustomize  Giai đoạn 4: Production Polish (Tuần 7+) ✅ Thêm validating/mutating webhooks nếu cần ✅ Implement graceful shutdown, leader election cho high availability ✅ Setup CI/CD pipeline để test và deploy controller tự động

---

> 🎯 Programming Kubernetes không phải là học một framework mới — đó là học cách tư duy declaratively, xây dựng systems tự heal, self-manage, và portable across clouds. Bạn không chỉ viết code; bạn đang mã hóa tri thức vận hành thành phần mềm.

---
Hãy bắt đầu nhỏ: Viết một controller đơn giản watch pods và log khi có pod mới. Từ đó, bạn đã bước chân vào thế giới của Kubernetes-native development. Chúc bạn xây dựng những hệ thống tự động, thông minh, và đáng tin cậy! 🚀☸️🔧