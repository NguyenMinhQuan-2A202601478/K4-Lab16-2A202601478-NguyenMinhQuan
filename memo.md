# Memo Teardown — Adobe Photoshop

**Nhóm:** K4-Lab16 · **Thành viên:** Nguyễn Minh Quân (Thành viên 1) · Trần Thị Kiều Trang (Thành viên 2) · Vũ Đình Huy (Thành viên 3) · Lê Đình Việt (Thành viên 4) · *(bổ sung Thành viên 5)*

**Vì sao chọn sản phẩm này:** Adobe Photoshop là sản phẩm tiêu biểu cho cuộc chuyển mình từ công cụ chỉnh sửa đồ họa chuyên nghiệp truyền thống sang tích hợp AI/ML toàn diện (từ Adobe Sensei đến Generative Fill với Firefly). Phân tích Photoshop giúp làm rõ cách một ứng dụng hàng đầu nhúng AI trực tiếp vào workflow sẵn có mà không làm đứt gãy thói quen người dùng.

> **Trạng thái bản ghép:** Đã ghép phần của Thành viên 1–4. Các nhãn “ứng viên” vẫn được giữ để nhóm chốt 6–8 mốc và đúng 3 dự đoán; Thành viên 5 cần bổ sung phần được giao trước khi nộp.

**§1. Timeline các cập nhật lớn**

| Thời điểm | Cập nhật | Context lúc đó | Nguyên lý |
|---|---|---|---|
| 12/04/2010 *(ứng viên TV1)* | Adobe ra mắt [Content-Aware Fill trên Photoshop CS5 (v12.0)](https://en.wikipedia.org/wiki/Adobe_Photoshop#CS5_(version_12)), tự động phân tích và điền bối cảnh xung quanh vùng ảnh bị xóa. | Việc xóa khuyết điểm hay vật thể thừa trước đây yêu cầu kỹ thuật viên dặm vá thủ công bằng Clone Stamp hoặc Patch Tool rất tốn thời gian. | **AI nhúng vào workflow sẵn có:** tự động hóa tác vụ lặp lại mà không làm thay đổi hay đứt gãy thói quen chọn vùng của người dùng. |
| 23/01/2018 *(ứng viên TV1)* | Adobe tích hợp [Select Subject (Adobe Sensei) vào Photoshop CC 2018 (v19.1)](https://en.wikipedia.org/wiki/Adobe_Photoshop#CC_2018_(version_19)), cho phép tách chủ thể tự động chỉ với 1-click. | Tách chủ thể người hoặc sản phẩm ra khỏi background phức tạp yêu cầu dùng Pen Tool tỉ mỉ từng pixel, tốn 15–30 phút cho mỗi bức ảnh. | **Nguyên lý x10 bằng AI:** nén thời gian thao tác từ hàng chục phút xuống 1 cú click (giảm 90% thời gian) nhờ mô hình Machine Learning Adobe Sensei. |
| 20/10/2020 *(ứng viên TV2)* | Adobe đưa [Neural Filters vào Photoshop 22.0](https://blog.adobe.com/en/publish/2020/10/05/photoshop-now-the-worlds-most-advanced-ai-application-for-creatives), biến Skin Smoothing, Smart Portrait, Colorize… thành workspace AI có output tiếp tục chỉnh bằng layer/mask. | Nhu cầu sản xuất nội dung vẫn tăng khi đội sáng tạo phải làm việc từ xa; Adobe nhấn mạnh nhu cầu tăng hiệu suất tại [Adobe MAX 2020](https://blog.adobe.com/en/publish/2020/10/08/maxoverview). Hợp tác Adobe–NVIDIA và tăng tốc GPU giúp Neural Filters đủ nhanh cho workflow thương mại. | **x10 bằng AI trong workflow có sẵn:** giảm quy trình nhiều bước xuống vài giây nhưng không lấy mất quyền tinh chỉnh của chuyên gia. |
| 26/10/2021 *(ứng viên TV2)* | Adobe thêm [Landscape Mixer, Color Transfer và Harmonization](https://blog.adobe.com/en/publish/2021/10/26/photoshop-ships-major-updates-across-desktop-ipad-apps-extends-light-editing-collaboration-features-web-beta), đồng thời cải thiện filter cũ từ feedback. | [DALL·E xuất hiện đầu 2021](https://openai.com/index/dall-e/), đẩy kỳ vọng từ AI chỉnh ảnh sang AI tạo nội dung. Adobe vẫn đóng gói AI thành các tác vụ có phạm vi rõ, tạo first pass rồi cho user hoàn thiện trong Photoshop. Đây là suy luận từ hai nguồn. | **Vòng lặp học có human feedback:** filter Beta thu phản hồi theo creative intent, giúp Adobe học định nghĩa “tốt” trong workflow sáng tạo. |
| 09/2023 *(ứng viên TV3)* | Generative Fill ra mắt chính thức trong Photoshop (v25.0), dựa trên model Firefly — sinh nội dung ảnh mới từ mô tả văn bản. Nguồn: [Adobe — trang sản phẩm Generative Fill](https://www.adobe.com/products/photoshop/generative-fill.html) | ChatGPT vừa gây sốt cuối 2022, cả ngành sáng tạo đua tích hợp generative AI; Midjourney/DALL-E đã chứng minh nhu cầu "gõ chữ ra ảnh" | Chuyển từ "tự động hoá thao tác có sẵn" (Content-Aware) sang "tạo nội dung hoàn toàn mới từ ngôn ngữ tự nhiên" → hạ rào cản kỹ năng, mở rộng Photoshop sang tệp không chuyên |
| 08/06/2023 *(ứng viên TV4)* | Adobe công bố [Firefly for Enterprise](https://news.adobe.com/news/news-details/2023/adobe-brings-firefly-and-express-to-enterprises), dự kiến hỗ trợ custom training bằng tài sản thương hiệu và cho khách hàng cơ hội mua IP indemnification đối với một số workflow. | Doanh nghiệp cần tăng sản lượng nội dung nhưng còn vướng tính nhất quán thương hiệu, quyền dữ liệu và rủi ro pháp lý khi đưa GenAI vào sản xuất. | **Trust và hệ sinh thái là moat:** dữ liệu được cấp phép, workflow theo thương hiệu và bảo đảm theo hợp đồng khiến giải pháp khó thay thế hơn một model đơn lẻ. |
| 13/09/2023 *(ứng viên TV4)* | Adobe phát hành thương mại [Generative Fill/Expand trong Photoshop và đưa generative credits vào Creative Cloud](https://news.adobe.com/news/news-details/2023/adobe-unleashes-new-era-of-creativity-for-all-with-the-commercial-release-of-generative-ai); Firefly mặc định có Content Credentials và enterprise có thể mua indemnification cho workflow đủ điều kiện. | Sau beta, Adobe phải đồng thời đưa GenAI vào sản xuất thật, phân bổ chi phí suy luận và giảm lo ngại về nguồn gốc/quyền sử dụng output. | **Monetize tại điểm workflow + trust:** credits đóng gói chi phí AI trong thuê bao; tích hợp Photoshop giảm ma sát; provenance và indemnification tăng khả năng dùng thương mại. |

*(6–8 hàng, mỗi hàng kèm link nguồn gốc)*

**Vì sao chọn những mốc này:** Bảy mốc ứng viên hiện tại tạo thành chuỗi thay đổi rõ: tự động hóa một thao tác (2010) → nhận diện bằng Sensei (2018) → workspace AI có feedback (2020–2021) → GenAI hạ rào cản kỹ năng → đóng gói cho doanh nghiệp và thương mại hóa trong Creative Cloud (2023). Nhóm vẫn cần quyết định `CHỌN/LOẠI` sau khi nhận mốc của Thành viên 5; không coi danh sách này là quyết định thay cho cả nhóm.

**§2. Tệp user & JTBD**

| | Early adopters | Tệp hiện tại |
|---|---|---|
| Đặc điểm | **Professional Graphic Designers, Digital Retouchers, Commercial Photographers tại các agency/studio sáng tạo, thành thạo công cụ Photoshop truyền thống (Pen Tool, Layer Mask, Channels, Color Spaces).** | *(Thành viên 3 điền.)* |
| JTBD chính | **Khi phải retouch hoặc dựng nhiều phương án trong thời gian ngắn, tôi muốn có một first pass đủ tốt chỉ trong vài giây để dành thời gian cho quyết định sáng tạo và tinh chỉnh cuối, nhưng vẫn giữ layer/mask để kiểm soát chất lượng trước khi giao khách hàng.** | *(Thành viên 3 điền.)* |
| Trước đó họ làm bằng cách nào | Retouch bằng selection/mask, Healing/Clone, Dodge & Burn, adjustment layers và Liquify; đồng bộ màu bằng Match Color/Curves/Color Balance; ghép ảnh bằng nhiều layer, mask và chỉnh ánh sáng thủ công. Neural Filters và Select Subject rút ngắn bước tạo first pass, không thay thế bước kiểm tra cuối. [Match Color](https://helpx.adobe.com/photoshop/desktop/adjust-color/selective-color-adjustments/match-color-between-two-images.html) · [Adjustment layers](https://helpx.adobe.com/photoshop/desktop/create-manage-layers/color-adjustment-fill-layers/create-adjustment-layers.html) · [Dodge and Burn](https://helpx.adobe.com/photoshop/desktop/repair-retouch/adjust-light-tone/dodge-or-burn-image-areas.html) | *(Thành viên 3 điền.)* |

**Dịch chuyển tệp:** cột mốc nào ở §1 gây ra sự dịch chuyển? Tại sao?

**Switching cost (map 4 forces) — phần Push/Pull của Thành viên 4:**

- **Push:** cách làm cũ chậm ở các bước tách nền, mở rộng canvas, xóa/thêm vật thể và tạo biến thể; nhu cầu nội dung đa kênh tăng nhanh hơn nhân lực; ideation bằng tool GenAI rời rồi nhập lại Photoshop gây mất ngữ cảnh, sai khác màu/phong cách và thêm thao tác quản lý file; tìm stock hoặc chụp bổ sung kéo dài vòng lặp.
- **Pull:** Generative Fill/Expand tạo first pass nhanh nhưng vẫn cho tinh chỉnh bằng selection, layer và mask; AI nằm ngay trong Photoshop/Creative Cloud nên giảm chi phí học và chuyển file; Content Credentials, nguồn dữ liệu được cấp phép và indemnification theo điều kiện hợp đồng giúp tổ chức có cơ sở quản trị; credits dùng chung quan hệ thuê bao hiện có nên dễ thử nghiệm và mở rộng.
- **Nhận định moat:** model có thể bị thay thế nhanh, còn lợi thế bền hơn của Adobe là chuỗi **dữ liệu/quyền sử dụng → PSD/layer workflow → Creative Cloud → provenance/trust → phân phối và thanh toán enterprise**. Với cá nhân, lực kéo mạnh là tốc độ trong workflow quen thuộc; với doanh nghiệp, lực kéo khác biệt là khả năng quản trị và sử dụng thương mại có căn cứ. Phần Habit/Anxiety và kết luận lực mạnh nhất chờ Thành viên 5 ghép để tránh ghi thay.

**§3. Ba dự đoán hướng đi (6–12 tháng tới)**

**Dự đoán 1** *(ứng viên Thành viên 2 — loại: mô hình kiếm tiền; chờ nhóm chọn)*
- **Dự đoán:** Trong giai đoạn 08/2026–08/2027, Adobe sẽ đưa Shared Credits/pool credit xuống Creative Cloud Teams hoặc ra add-on tương đương, để admin nhóm nhỏ phân ngân sách và mua thêm lượt dùng model premium trong Photoshop.
- **Lập luận:** Hai mốc 2020–2021 cho thấy Adobe đưa AI vào workflow chuyên nghiệp rồi cải thiện từ usage/feedback (§1), trong khi early adopters cần throughput ổn định để giao việc đúng hạn (§2). Hiện [partner models và tác vụ tốn compute dùng premium credits](https://helpx.adobe.com/creative-cloud/apps/generative-ai/creative-cloud-generative-ai-features.html), Photoshop đã cho [theo dõi/mua thêm credits](https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html), nhưng [Shared Credits yêu cầu điều kiện enterprise/ETLA](https://helpx.adobe.com/enterprise/using/generative-credit-pool.html). Mở xuống Teams là bước kiếm tiền theo usage mà không làm đứt workflow studio nhỏ.

**Dự đoán 2** *(ứng viên Thành viên 1 — loại: mở rộng tính năng; chờ nhóm chọn)*
- **Dự đoán:** Adobe sẽ tích hợp công cụ Multi-modal Real-time Canvas AI Control (điều khiển AI thời gian thực kết hợp nét cọ phác thảo + prompt ngôn ngữ tự nhiên) trực tiếp trên giao diện Canvas của Photoshop trong 6–12 tháng tới.
- **Lập luận:** Dẫn ngược từ mốc Select Subject (2018) và Generative Fill (2023) ở §1, cùng nhu cầu kiểm soát pixel-perfect của Early Adopters ở §2. Sau khi tự động hóa việc chọn vùng và tạo ảnh tĩnh, bước tiếp theo để giữ chân chuyên gia là tương tác điều chỉnh AI theo thời gian thực (real-time feedback loop).

**Dự đoán 3** *(Ứng viên thành viên 3 - loại: đe dọa Big Tech)*
- **Dự đoán:** Trong 6–12 tháng tới, Photoshop sẽ tiếp tục mở thêm nhiều model AI bên thứ ba (Google Gemini/Nano Banana Pro, Black Forest Labs FLUX, và các lab khác) ngay trong Generative Fill/Firefly, thay vì chỉ dùng model Firefly độc quyền của Adobe — biến Photoshop thành lớp "giao diện/aggregator" AI thay vì tự đối đầu chạy đua model với Big Tech.
- **Lập luận:** Mốc gần nhất ở §1 cho thấy Adobe đã bắt đầu nhúng Gemini 3/Nano Banana Pro và FLUX.2 pro vào Generative Fill — tức chọn "hợp tác" thay vì "cạnh tranh trực diện" với các lab lớn. Điều này hợp lý vì lợi thế cạnh tranh của Adobe không nằm ở việc tự train model ảnh tốt nhất (thứ Google/OpenAI đang thắng), mà nằm ở switching cost cao của tệp user hiện tại — định dạng PSD chuẩn ngành, thói quen thao tác nhiều năm, tích hợp Creative Cloud (§2). Vì vậy Big Tech khó "cướp" trực tiếp user của Adobe dù có model AI tốt hơn, nên Adobe tận dụng bằng cách nhúng chính các model đó vào workflow độc quyền của mình. *(Cần đối chiếu lại với nội dung §2 khi nhóm điền xong phần switching cost.)*

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
| Tổng hợp hai mốc Firefly for Enterprise và phát hành thương mại GenAI | AI (Codex) mở nguồn Adobe và viết bản nháp cho Thành viên 4 | Việt tự mở lại từng link, phân biệt thông báo kế hoạch với tính năng đã phát hành và không diễn giải “commercially safe” thành an toàn bản quyền tuyệt đối |
| Phân tích wrapper/moat và hai lực Push/Pull | AI đề xuất cấu trúc; Thành viên 4 chịu trách nhiệm phán đoán | Việt đối chiếu với user/JTBD do nhóm chốt và yêu cầu Thành viên 5 bổ sung Habit/Anxiety trước khi kết luận lực mạnh nhất |
| Viết dự đoán lớp điều phối đa mô hình có quản trị | AI đề xuất từ timeline và switching forces | Nhóm kiểm tra khung 6–12 tháng, phản biện rủi ro chi phí/pháp lý và chỉ giữ nếu được chọn trong ba dự đoán cuối |
| Đồng bộ deck Canva của nhóm | AI giữ nguyên trang 1–3 đã có và thay các trang template 4–10 bằng nội dung bám memo | Việt rà font, độ tương phản, lỗi chính tả, đối chiếu memo–slide, xuất `slides.pdf`; Thành viên 5 kiểm tra file PDF cuối |

