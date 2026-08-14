# Memo Teardown — Adobe Photoshop

**Nhóm:** K4-Lab16 · **Thành viên:** Nguyễn Minh Quân (Thành viên 1) · Trần Thị Kiều Trang (Thành viên 2) · *(bổ sung 3 thành viên còn lại)*

**Vì sao chọn sản phẩm này:** Adobe Photoshop là sản phẩm tiêu biểu cho cuộc chuyển mình từ công cụ chỉnh sửa đồ họa chuyên nghiệp truyền thống sang tích hợp AI/ML toàn diện (từ Adobe Sensei đến Generative Fill với Firefly). Phân tích Photoshop giúp làm rõ cách một ứng dụng hàng đầu nhúng AI trực tiếp vào workflow sẵn có mà không làm đứt gãy thói quen người dùng.

> **Trạng thái bản ghép:** Các mốc và dự đoán dưới đây là ứng viên do Thành viên 1 và Thành viên 2 đề xuất, chưa đại diện cho quyết định chung. Cả nhóm cần họp chọn 6–8 mốc và 3 dự đoán rồi xóa nhãn “ứng viên” trước khi nộp.

**§1. Timeline các cập nhật lớn**

| Thời điểm | Cập nhật | Context lúc đó | Nguyên lý |
|---|---|---|---|
| 12/04/2010 *(ứng viên TV1)* | Adobe ra mắt [Content-Aware Fill trên Photoshop CS5 (v12.0)](https://en.wikipedia.org/wiki/Adobe_Photoshop#CS5_(version_12)), tự động phân tích và điền bối cảnh xung quanh vùng ảnh bị xóa. | Việc xóa khuyết điểm hay vật thể thừa trước đây yêu cầu kỹ thuật viên dặm vá thủ công bằng Clone Stamp hoặc Patch Tool rất tốn thời gian. | **AI nhúng vào workflow sẵn có:** tự động hóa tác vụ lặp lại mà không làm thay đổi hay đứt gãy thói quen chọn vùng của người dùng. |
| 23/01/2018 *(ứng viên TV1)* | Adobe tích hợp [Select Subject (Adobe Sensei) vào Photoshop CC 2018 (v19.1)](https://en.wikipedia.org/wiki/Adobe_Photoshop#CC_2018_(version_19)), cho phép tách chủ thể tự động chỉ với 1-click. | Tách chủ thể người hoặc sản phẩm ra khỏi background phức tạp yêu cầu dùng Pen Tool tỉ mỉ từng pixel, tốn 15–30 phút cho mỗi bức ảnh. | **Nguyên lý x10 bằng AI:** nén thời gian thao tác từ hàng chục phút xuống 1 cú click (giảm 90% thời gian) nhờ mô hình Machine Learning Adobe Sensei. |
| 20/10/2020 *(ứng viên TV2)* | Adobe đưa [Neural Filters vào Photoshop 22.0](https://blog.adobe.com/en/publish/2020/10/05/photoshop-now-the-worlds-most-advanced-ai-application-for-creatives), biến Skin Smoothing, Smart Portrait, Colorize… thành workspace AI có output tiếp tục chỉnh bằng layer/mask. | Nhu cầu sản xuất nội dung vẫn tăng khi đội sáng tạo phải làm việc từ xa; Adobe nhấn mạnh nhu cầu tăng hiệu suất tại [Adobe MAX 2020](https://blog.adobe.com/en/publish/2020/10/08/maxoverview). Hợp tác Adobe–NVIDIA và tăng tốc GPU giúp Neural Filters đủ nhanh cho workflow thương mại. | **x10 bằng AI trong workflow có sẵn:** giảm quy trình nhiều bước xuống vài giây nhưng không lấy mất quyền tinh chỉnh của chuyên gia. |
| 26/10/2021 *(ứng viên TV2)* | Adobe thêm [Landscape Mixer, Color Transfer và Harmonization](https://blog.adobe.com/en/publish/2021/10/26/photoshop-ships-major-updates-across-desktop-ipad-apps-extends-light-editing-collaboration-features-web-beta), đồng thời cải thiện filter cũ từ feedback. | [DALL·E xuất hiện đầu 2021](https://openai.com/index/dall-e/), đẩy kỳ vọng từ AI chỉnh ảnh sang AI tạo nội dung. Adobe vẫn đóng gói AI thành các tác vụ có phạm vi rõ, tạo first pass rồi cho user hoàn thiện trong Photoshop. Đây là suy luận từ hai nguồn. | **Vòng lặp học có human feedback:** filter Beta thu phản hồi theo creative intent, giúp Adobe học định nghĩa “tốt” trong workflow sáng tạo. |

*(6–8 hàng, mỗi hàng kèm link nguồn gốc)*

**Vì sao chọn những mốc này:** *(Cả nhóm hoàn thiện sau khi đánh dấu `CHỌN/LOẠI` trong `timeline.md`. Các mốc trên hiện là ứng viên của Thành viên 1 và Thành viên 2.)*

**§2. Tệp user & JTBD**

| | Early adopters | Tệp hiện tại |
|---|---|---|
| Đặc điểm | **Professional Graphic Designers, Digital Retouchers, Commercial Photographers tại các agency/studio sáng tạo, thành thạo công cụ Photoshop truyền thống (Pen Tool, Layer Mask, Channels, Color Spaces).** | *(Thành viên 3 điền.)* |
| JTBD chính | **Khi phải retouch hoặc dựng nhiều phương án trong thời gian ngắn, tôi muốn có một first pass đủ tốt chỉ trong vài giây để dành thời gian cho quyết định sáng tạo và tinh chỉnh cuối, nhưng vẫn giữ layer/mask để kiểm soát chất lượng trước khi giao khách hàng.** | *(Thành viên 3 điền.)* |
| Trước đó họ làm bằng cách nào | Retouch bằng selection/mask, Healing/Clone, Dodge & Burn, adjustment layers và Liquify; đồng bộ màu bằng Match Color/Curves/Color Balance; ghép ảnh bằng nhiều layer, mask và chỉnh ánh sáng thủ công. Neural Filters và Select Subject rút ngắn bước tạo first pass, không thay thế bước kiểm tra cuối. [Match Color](https://helpx.adobe.com/photoshop/desktop/adjust-color/selective-color-adjustments/match-color-between-two-images.html) · [Adjustment layers](https://helpx.adobe.com/photoshop/desktop/create-manage-layers/color-adjustment-fill-layers/create-adjustment-layers.html) · [Dodge and Burn](https://helpx.adobe.com/photoshop/desktop/repair-retouch/adjust-light-tone/dodge-or-burn-image-areas.html) | *(Thành viên 3 điền.)* |

**Dịch chuyển tệp:** cột mốc nào ở §1 gây ra sự dịch chuyển? Tại sao?

**Switching cost (map 4 forces):** điều gì giữ user ở lại? Lực nào đang kéo họ đi / giữ họ lại?

**§3. Ba dự đoán hướng đi (6–12 tháng tới)**

**Dự đoán 1** *(ứng viên Thành viên 2 — loại: mô hình kiếm tiền; chờ nhóm chọn)*
- **Dự đoán:** Trong giai đoạn 08/2026–08/2027, Adobe sẽ đưa Shared Credits/pool credit xuống Creative Cloud Teams hoặc ra add-on tương đương, để admin nhóm nhỏ phân ngân sách và mua thêm lượt dùng model premium trong Photoshop.
- **Lập luận:** Hai mốc 2020–2021 cho thấy Adobe đưa AI vào workflow chuyên nghiệp rồi cải thiện từ usage/feedback (§1), trong khi early adopters cần throughput ổn định để giao việc đúng hạn (§2). Hiện [partner models và tác vụ tốn compute dùng premium credits](https://helpx.adobe.com/creative-cloud/apps/generative-ai/creative-cloud-generative-ai-features.html), Photoshop đã cho [theo dõi/mua thêm credits](https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html), nhưng [Shared Credits yêu cầu điều kiện enterprise/ETLA](https://helpx.adobe.com/enterprise/using/generative-credit-pool.html). Mở xuống Teams là bước kiếm tiền theo usage mà không làm đứt workflow studio nhỏ.

**Dự đoán 2** *(ứng viên Thành viên 1 — loại: mở rộng tính năng; chờ nhóm chọn)*
- **Dự đoán:** Adobe sẽ tích hợp công cụ Multi-modal Real-time Canvas AI Control (điều khiển AI thời gian thực kết hợp nét cọ phác thảo + prompt ngôn ngữ tự nhiên) trực tiếp trên giao diện Canvas của Photoshop trong 6–12 tháng tới.
- **Lập luận:** Dẫn ngược từ mốc Select Subject (2018) và Generative Fill (2023) ở §1, cùng nhu cầu kiểm soát pixel-perfect của Early Adopters ở §2. Sau khi tự động hóa việc chọn vùng và tạo ảnh tĩnh, bước tiếp theo để giữ chân chuyên gia là tương tác điều chỉnh AI theo thời gian thực (real-time feedback loop).

**Dự đoán 3** *(loại: …)*
- **Dự đoán:** …
- **Lập luận:** …

**§4. AI Log**

| Việc | AI làm hay nhóm làm? | Nhóm kiểm chứng/phán đoán lại thế nào? |
|---|---|---|
| Cào dữ liệu lịch sử phiên bản từ Wikipedia & Adobe HelpX | AI thực hiện tự động qua script Python `source/crawl.py` | Thành viên 1 đối chiếu file HTML gốc và ngày phát hành trên trang chính thức Adobe HelpX |
| Tổng hợp 2 mốc ứng viên AI nền tảng (CS5 Content-Aware Fill & Sensei Select Subject) | Thành viên 1 nghiên cứu và ghi nhận | Quân tự mở link Wikipedia & Adobe Release Notes để đối chiếu ngày phát hành và bối cảnh tính năng |
| Phân tích tệp Early Adopters (Đặc điểm & JTBD) | Thành viên 1 xác định đặc điểm; nhóm chốt chung | Quân đối chiếu với quy trình làm việc thực tế của photo retoucher/designer trước khi có AI |
| Dự đoán 2 (Multi-modal Real-time Canvas AI Control) | Thành viên 1 đề xuất và lập luận | Nhóm kiểm tra tính khả thi công nghệ và khả năng dẫn ngược từ §1 và §2 |
| Tìm nguồn và tổng hợp hai mốc Neural Filters 2020–2021 | AI (Codex) tìm, mở và đối chiếu nguồn Adobe/NVIDIA/OpenAI | **Trang cần tự mở từng link**, kiểm tra ngày và xác nhận nguồn hỗ trợ đúng nhận định; cả nhóm quyết định chọn/loại từng mốc |
| Revert hai mốc về nguyên lý `x10` và vòng lặp học | AI đề xuất mapping và viết bản nháp | Trang giải thích lại bằng lời của mình; nhóm đối chiếu tên nguyên lý với nội dung đã học và sửa nếu cần |
| Xây dựng JTBD và mô tả cách làm cũ của early adopters | AI tổng hợp từ đối tượng/workflow được Adobe mô tả | Trang đối chiếu với early adopters do Thành viên 1 chốt; nhóm sửa nếu hai phần không cùng một tệp user |
| Viết dự đoán Shared Credits cho Teams | AI tổng hợp chính sách credits hiện tại và đưa ra suy luận | Nhóm kiểm tra Shared Credits chưa có sẵn cho Teams tại ngày nộp, phản biện giả định nhu cầu premium models rồi quyết định chọn/loại |
| Viết nội dung slide và speaker notes “AI trước Generative Fill” | AI viết bản nháp trong `member-2.md` | Trang rút gọn theo template Canva của nhóm, tự tập nói và chỉ giữ các nhận định có thể bảo vệ khi thảo luận |
| Audit link cuối memo | Trang và nhóm thực hiện | Mở lại toàn bộ link sau khi ghép; loại link hỏng, sai ngày hoặc không trực tiếp chứng minh nhận định |

