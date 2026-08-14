# Memo Teardown — Adobe Photoshop

**Nhóm:** K4-Lab16

| Vai trò | Họ tên | MSSV |
|---|---|---|
| Thành viên 1 | Nguyễn Quy Dũng | 2A202601200 |
| Thành viên 2 | Trần Thị Kiều Trang | 2A202601498 |
| Thành viên 3 | Vũ Đình Huy | 2A202601288 |
| Thành viên 4 | Lê Đình Việt | 2A202601528 |
| Thành viên 5 | Nguyễn Minh Quân | 2A202601478 |

**Vì sao chọn sản phẩm này:** Adobe Photoshop là sản phẩm tiêu biểu cho cuộc chuyển mình từ công cụ chỉnh sửa đồ họa chuyên nghiệp truyền thống sang tích hợp AI/ML toàn diện (từ Adobe Sensei đến Generative Fill với Firefly). Phân tích Photoshop giúp làm rõ cách một ứng dụng hàng đầu nhúng AI trực tiếp vào workflow sẵn có mà không làm đứt gãy thói quen người dùng.

---

## §1. Timeline các cập nhật lớn

| # | Thời điểm | Cập nhật | Context lúc đó | Nguyên lý | Người đào |
|---|---|---|---|---|---|
| 1 | 12/04/2010 | Adobe ra mắt [Content-Aware Fill trên Photoshop CS5 (v12.0)](https://en.wikipedia.org/wiki/Adobe_Photoshop#CS5_(version_12)), tự động phân tích và điền bối cảnh xung quanh vùng ảnh bị xóa. | Việc xóa khuyết điểm hay vật thể thừa trước đây yêu cầu kỹ thuật viên dặm vá thủ công bằng Clone Stamp hoặc Patch Tool rất tốn thời gian. | **AI nhúng vào workflow sẵn có:** tự động hóa tác vụ lặp lại mà không làm thay đổi hay đứt gãy thói quen chọn vùng của người dùng. | Nguyễn Quy Dũng |
| 2 | 23/01/2018 | Adobe tích hợp [Select Subject (Adobe Sensei) vào Photoshop CC 2018 (v19.1)](https://en.wikipedia.org/wiki/Adobe_Photoshop#CC_2018_(version_19)), cho phép tách chủ thể tự động chỉ với 1-click. | Tách chủ thể người hoặc sản phẩm ra khỏi background phức tạp yêu cầu dùng Pen Tool tỉ mỉ từng pixel, tốn 15–30 phút cho mỗi bức ảnh. | **Nguyên lý x10 bằng AI:** nén thời gian thao tác từ hàng chục phút xuống 1 cú click (giảm 90% thời gian) nhờ mô hình Machine Learning Adobe Sensei. | Nguyễn Quy Dũng |
| 3 | 20/10/2020 | Adobe đưa [Neural Filters vào Photoshop 22.0](https://blog.adobe.com/en/publish/2020/10/05/photoshop-now-the-worlds-most-advanced-ai-application-for-creatives), biến Skin Smoothing, Smart Portrait, Colorize… thành workspace AI có output tiếp tục chỉnh bằng layer/mask. | Nhu cầu sản xuất nội dung vẫn tăng khi đội sáng tạo phải làm việc từ xa; Adobe nhấn mạnh nhu cầu tăng hiệu suất tại [Adobe MAX 2020](https://blog.adobe.com/en/publish/2020/10/08/maxoverview). Hợp tác Adobe–NVIDIA và tăng tốc GPU giúp Neural Filters đủ nhanh cho workflow thương mại. | **x10 bằng AI trong workflow có sẵn:** giảm quy trình nhiều bước xuống vài giây nhưng không lấy mất quyền tinh chỉnh của chuyên gia. | Trần Thị Kiều Trang |
| 4 | 23/05/2023 | Adobe đưa [**Generative Fill (beta) vào Photoshop**](https://blog.adobe.com/en/publish/2023/05/23/future-of-photoshop-powered-by-adobe-firefly), lần đầu tích hợp model Firefly trực tiếp vào workflow Photoshop — user chọn vùng, gõ prompt text và AI tạo/thay nội dung ảnh ngay trên layer mới. | Midjourney v5 ra tháng 3/2023, DALL·E tích hợp Bing. Generative AI bùng nổ nhưng nằm ngoài các công cụ chỉnh sửa chuyên nghiệp — user phải tạo ảnh ở app riêng rồi import vào Photoshop. Adobe vừa ra mắt [Firefly beta (03/2023)](https://news.adobe.com/news/news-details/2023/adobe-unveils-firefly-a-family-of-new-creative-generative-ai), cần chứng minh model hoạt động trong workflow thật. | **Wrapper — nhúng GenAI vào workflow có sẵn:** thay vì xây app mới, Adobe đặt Firefly vào đúng nơi user đã quen (chọn vùng → điền nội dung), biến text-to-image thành một bước chỉnh sửa chứ không phải app riêng. | Vũ Đình Huy |
| 5 | 09/2023 | Generative Fill ra mắt chính thức trong Photoshop (v25.0), dựa trên model Firefly — sinh nội dung ảnh mới từ mô tả văn bản. Nguồn: [Adobe — trang sản phẩm Generative Fill](https://www.adobe.com/products/photoshop/generative-fill.html) | ChatGPT vừa gây sốt cuối 2022, cả ngành sáng tạo đua tích hợp generative AI; Midjourney/DALL-E đã chứng minh nhu cầu "gõ chữ ra ảnh" | Chuyển từ "tự động hoá thao tác có sẵn" (Content-Aware) sang "tạo nội dung hoàn toàn mới từ ngôn ngữ tự nhiên" → hạ rào cản kỹ năng, mở rộng Photoshop sang tệp không chuyên. | Vũ Đình Huy |
| 6 | 13/09/2023 | Adobe phát hành thương mại [Generative Fill/Expand trong Photoshop và đưa generative credits vào Creative Cloud](https://news.adobe.com/news/news-details/2023/adobe-unleashes-new-era-of-creativity-for-all-with-the-commercial-release-of-generative-ai); Firefly mặc định có Content Credentials và enterprise có thể mua indemnification cho workflow đủ điều kiện. | Sau beta, Adobe phải đồng thời đưa GenAI vào sản xuất thật, phân bổ chi phí suy luận và giảm lo ngại về nguồn gốc/quyền sử dụng output. | **Monetize tại điểm workflow + trust:** credits đóng gói chi phí AI trong thuê bao; tích hợp Photoshop giảm ma sát; provenance và indemnification tăng khả năng dùng thương mại. | Lê Đình Việt |
| 7 | 07/2024 | Adobe ra mắt [**Generate Image** trong Photoshop 25.11](https://news.adobe.com/news/news-details/2024/new-adobe-photoshop-with-advanced-generative-fill-and-generate-image-brings-new-superpowers-to-all), cùng Reference Image, Generate Similar, Generate Background — tất cả chạy trên **Firefly Image 3** (nhanh gấp 4× model cũ). Lần đầu text-to-image generation được nhúng trực tiếp vào canvas Photoshop. | Midjourney, DALL·E 3, Stable Diffusion XL bùng nổ ngoài Adobe. User phải rời Photoshop để tạo ảnh AI rồi import ngược. Tính đến thời điểm này, user đã tạo hơn 7 tỷ ảnh bằng Firefly. | **Wrapper/moat:** "bọc" model Firefly vào workflow Photoshop (layers, masks, selections), biến generation thành một bước chỉnh sửa thay vì app riêng. | Nguyễn Minh Quân |
| 8 | 25/02/2025 | Adobe ra mắt [**Photoshop trên iPhone miễn phí**](https://news.adobe.com/news/2025/02/photoshop-mobile-web), lần đầu mang Photoshop desktop-grade (layers, masks, Generative Fill, Generative Expand) lên mobile với free tier. Android phát hành 06/2025. Premium $7.99/tháng. | Canva (260 triệu MAU), Picsart, CapCut chiếm casual creator trên mobile. Google Photos Magic Editor miễn phí, Apple Clean Up có sẵn trên iPhone. Thế hệ creator Gen Z chỉnh ảnh trên điện thoại, không ngồi desktop. | **Mở rộng segment:** hạ rào cản (giá = 0, nền tảng = mobile) để kéo "next generation of creators" vào hệ sinh thái; lực Habit sẽ giữ họ lại và upsell lên plan trả phí. | Nguyễn Minh Quân |

**Vì sao chọn những mốc này:** Tám mốc tạo thành chuỗi thay đổi rõ: tự động hóa một thao tác (2010) → nhận diện bằng Sensei (2018) → workspace AI có feedback (2020) → nhúng GenAI vào workflow Photoshop qua Generative Fill beta (05/2023) → phát hành thương mại + hạ rào cản kỹ năng (09/2023) → đóng gói credits, trust và indemnification (09/2023) → text-to-image nhúng vào canvas (07/2024) → mở rộng segment qua mobile miễn phí (02/2025).

**Mốc bị loại và lý do:**

- **Landscape Mixer, Color Transfer & Harmonization (26/10/2021, Trần Thị Kiều Trang):** cập nhật mở rộng bộ Neural Filters, không phải quyết định sản phẩm lớn riêng biệt; nguyên lý "vòng lặp học có human feedback" đã được thể hiện qua mốc Neural Filters 2020.
- **Firefly for Enterprise (08/06/2023, Lê Đình Việt):** thông báo kế hoạch enterprise, chưa phải sản phẩm ship đến user; giá trị trust, dữ liệu được cấp phép và indemnification đã được phản ánh trong mốc phát hành thương mại 13/09/2023.

---

## §2. Tệp user & JTBD

| | Early adopters | Tệp hiện tại |
|---|---|---|
| Đặc điểm | **Professional Graphic Designers, Digital Retouchers, Commercial Photographers tại các agency/studio sáng tạo, thành thạo công cụ Photoshop truyền thống (Pen Tool, Layer Mask, Channels, Color Spaces).** | **Content creators, social media marketers, in-house marketing teams, photographer bán chuyên và small business owners cần visual content đa kênh.** Nhiều người mới tiếp cận Photoshop qua Generative Fill hoặc Photoshop Mobile miễn phí — không nhất thiết thành thạo layer/mask/selection truyền thống nhưng biết dùng prompt text để tạo và chỉnh ảnh. |
| JTBD chính | **Khi phải retouch hoặc dựng nhiều phương án trong thời gian ngắn, tôi muốn có một first pass đủ tốt chỉ trong vài giây để dành thời gian cho quyết định sáng tạo và tinh chỉnh cuối, nhưng vẫn giữ layer/mask để kiểm soát chất lượng trước khi giao khách hàng.** | **Khi cần sản xuất nhiều visual (ảnh sản phẩm, banner, social media post) trong thời gian ngắn mà không có ngân sách thuê designer, tôi muốn dùng AI tạo ảnh, xóa/thay nền, mở rộng canvas chỉ bằng mô tả văn bản, nhằm giao nội dung đúng hạn với chất lượng chuyên nghiệp hơn Canva nhưng không cần kỹ năng Photoshop truyền thống.** |
| Trước đó họ làm bằng cách nào | Retouch bằng selection/mask, Healing/Clone, Dodge & Burn, adjustment layers và Liquify; đồng bộ màu bằng Match Color/Curves/Color Balance; ghép ảnh bằng nhiều layer, mask và chỉnh ánh sáng thủ công. Neural Filters và Select Subject rút ngắn bước tạo first pass, không thay thế bước kiểm tra cuối. [Match Color](https://helpx.adobe.com/photoshop/desktop/adjust-color/selective-color-adjustments/match-color-between-two-images.html) · [Adjustment layers](https://helpx.adobe.com/photoshop/desktop/create-manage-layers/color-adjustment-fill-layers/create-adjustment-layers.html) · [Dodge and Burn](https://helpx.adobe.com/photoshop/desktop/repair-retouch/adjust-light-tone/dodge-or-burn-image-areas.html) | Dùng Canva, Picsart hoặc app ảnh mobile (Snapseed, VSCO) để tạo visual nhanh; thuê designer freelance/agency cho nội dung quan trọng; tìm stock ảnh trên Unsplash/Shutterstock rồi chỉnh sửa cơ bản; dùng DALL-E/Midjourney tạo ảnh AI nhưng phải export rồi chỉnh lại trên tool khác; dùng [remove.bg](https://www.remove.bg/), [Photoroom](https://www.photoroom.com/) để xóa nền — mỗi tác vụ một app riêng, không có workflow thống nhất. |

**Dịch chuyển tệp:** *(Nguyễn Minh Quân phân tích)*

Hai mốc gây ra sự dịch chuyển rõ nhất từ **professional designer → creator/marketer/team rộng hơn**:

1. **Generate Image + Firefly Image 3 (07/2024):** Trước mốc này, mọi tính năng AI trong Photoshop (Content-Aware Fill, Select Subject, Neural Filters) đều phục vụ workflow chỉnh sửa — vẫn đòi hỏi user biết dùng layer/mask/selection. Generate Image lần đầu cho phép **tạo ảnh từ prompt text** ngay trong canvas, mở cửa cho người không biết vẽ cũng có thể tạo content. Adobe quảng bá rõ: *"brings new superpowers to **all**"* — không giới hạn ở designer. ([Adobe Newsroom 07/2024](https://news.adobe.com/news/news-details/2024/new-adobe-photoshop-with-advanced-generative-fill-and-generate-image-brings-new-superpowers-to-all))

2. **Photoshop Mobile miễn phí (02/2025):** Đây là mốc dịch chuyển segment rõ ràng nhất. Adobe chủ ý dùng từ *"next generation of creators"* và ra app **miễn phí trên iPhone** — lần đầu Photoshop không yêu cầu subscription để bắt đầu. Forrester phân tích Adobe đang chuyển chiến lược từ "creator tools" sang ["creative participation"](https://www.forrester.com/blogs/shifting-from-creator-tools-to-creative-participation-adobe-max-takeaways/) — cho phép marketer, nhân viên, người không chuyên cũng tham gia sáng tạo, không chỉ designer chuyên nghiệp.

Kết hợp hai mốc: Generate Image hạ rào cản kỹ năng (không cần biết vẽ), Photoshop Mobile hạ rào cản giá + nền tảng (miễn phí, trên điện thoại). Tệp user mở rộng từ "pro designer ngồi desktop" sang "bất kỳ ai cần tạo visual content trên mọi thiết bị".

**Switching cost (map 4 forces):**

**Push/Pull — Lê Đình Việt phân tích:**

- **Push:** cách làm cũ chậm ở các bước tách nền, mở rộng canvas, xóa/thêm vật thể và tạo biến thể; nhu cầu nội dung đa kênh tăng nhanh hơn nhân lực; ideation bằng tool GenAI rời rồi nhập lại Photoshop gây mất ngữ cảnh, sai khác màu/phong cách và thêm thao tác quản lý file; tìm stock hoặc chụp bổ sung kéo dài vòng lặp.
- **Pull:** Generative Fill/Expand tạo first pass nhanh nhưng vẫn cho tinh chỉnh bằng selection, layer và mask; AI nằm ngay trong Photoshop/Creative Cloud nên giảm chi phí học và chuyển file; Content Credentials, nguồn dữ liệu được cấp phép và indemnification theo điều kiện hợp đồng giúp tổ chức có cơ sở quản trị; credits dùng chung quan hệ thuê bao hiện có nên dễ thử nghiệm và mở rộng.
- **Nhận định moat:** model có thể bị thay thế nhanh, còn lợi thế bền hơn của Adobe là chuỗi **dữ liệu/quyền sử dụng → PSD/layer workflow → Creative Cloud → provenance/trust → phân phối và thanh toán enterprise**. Với cá nhân, lực kéo mạnh là tốc độ trong workflow quen thuộc; với doanh nghiệp, lực kéo khác biệt là khả năng quản trị và sử dụng thương mại có căn cứ.

**Habit/Anxiety — Nguyễn Minh Quân phân tích:**

**Habit — điều gì giữ user ở lại Photoshop?**

1. **File PSD và tài sản sáng tạo tích lũy:** User chuyên nghiệp có hàng năm file PSD với layers, masks, smart objects, adjustment layers. Định dạng PSD là proprietary — export sang tool khác thì layers không dịch đúng, effects bị flatten, fonts mất. Một designer đã xây library gồm brushes, actions, presets, templates thì bỏ đi đồng nghĩa mất "vốn nghề". ([Koder.ai — How Adobe Built High Switching Costs](https://koder.ai/blog/how-adobe-built-high-switching-costs-creative-workflows))
2. **Plugin ecosystem:** Nik Collection, Luminar, Topaz… không chạy trên Canva hay Picsart. Workflow gắn chặt với plugin cụ thể — đổi tool = xây lại pipeline.
3. **Shortcut và muscle memory:** Ctrl+J, Ctrl+T, pen tool, clone stamp — user pro đã nhúng thao tác Photoshop vào phản xạ tay. Học lại shortcut app khác giảm năng suất ngay lập tức.
4. **Quy trình nhóm và Creative Cloud:** Trong team agency/enterprise, quy trình chuẩn hóa xung quanh Photoshop: file chia sẻ qua Creative Cloud Libraries, font sync qua Adobe Fonts, handoff qua XD/Illustrator cùng hệ. [98% Fortune 500 dùng Adobe, 30 triệu+ subscriber](https://bizmodelmastery.substack.com/p/inside-adobes-176b-subscription-machine) — một cá nhân muốn đổi tool phải thuyết phục cả team, cả công ty.
5. **Danh tiếng nghề nghiệp:** "Thành thạo Photoshop" là yêu cầu trong JD hầu hết vị trí design/photo. Đổi tool không chỉ mất kỹ năng mà còn mất giá trị CV.

> **Lực Habit mạnh nhất:** File PSD + Creative Cloud ecosystem — đây không phải thói quen cá nhân (có thể thay đổi) mà là **tài sản tích lũy + quy trình tổ chức** (rất tốn kém để thay). Nếu lực này biến mất — ví dụ một chuẩn file mở được các tool lớn đồng loạt hỗ trợ, hoặc AI tự convert PSD sang format khác không mất chất lượng — rào cản chuyển đổi sẽ giảm mạnh.

**Anxiety — điều gì khiến user ngại chuyển đổi hoặc ngại dùng AI?**

1. **Chi phí subscription leo thang:** Adobe tăng giá Creative Cloud lên đến 50% vào tháng 6/2025 ([TSG — Adobe Creative Cloud 2025 Price Hikes](https://thesiegroup.com/blog/adobe-creative-cloud-2025-pricing-changes-cost-savings-guide)). User phải trả thêm cho generative credits khi dùng hết — anxiety kép: sợ lock-in giá cao + không biết chi phí AI sẽ tăng bao nhiêu.
2. **Chất lượng AI output chưa ổn định:** Generative Fill/Generate Image đôi khi tạo artifacts, ngón tay thừa, chi tiết sai. User pro lo "đủ tốt cho draft nhưng không đủ cho final delivery" — phải chỉnh lại thủ công, tốn thời gian hơn không dùng AI.
3. **Lo ngại bản quyền và IP:** Dù Adobe tuyên bố Firefly "commercial-safe" và có IP indemnification, cộng đồng vẫn lo: Adobe Stock chứa tới 62% nội dung do AI tạo, contributor gốc không đồng ý rõ ràng cho việc train AI trên ảnh của họ. Content Credentials chỉ là "nhãn dinh dưỡng", không phải đảm bảo pháp lý hoàn toàn. ([Adobe Community — Firefly copyright concerns](https://community.adobe.com/questions-404/how-is-firefly-safe-for-commercial-use-adobe-stock-now-contains-62-unsafe-generative-ai-ip-etc-1478640))
4. **Mất kiểm soát sáng tạo:** AI tạo output ngẫu nhiên — designer chuyên nghiệp quen kiểm soát từng pixel nay phải trust vào black box. Đặc biệt với photographer/retoucher coi mỗi chi tiết là dấu ấn cá nhân.
5. **Độ khó học AI workflow mới:** Prompt engineering không phải kỹ năng truyền thống của designer. Reference Image giảm gánh nặng nhưng vẫn là thêm bước nhận thức trong workflow.

> **Anxiety lớn nhất:** Chi phí + bản quyền — user vừa trả tiền cao hơn, vừa không chắc output AI có an toàn pháp lý để dùng thương mại. Nối với mốc Photoshop Mobile miễn phí (02/2025): Adobe đang cố giảm anxiety chi phí cho casual creator bằng free tier, nhưng lại tăng anxiety cho pro user khi giá desktop tăng — phân mảnh trải nghiệm giữa 2 segment.

---

## §3. Ba dự đoán hướng đi (6–12 tháng tới)

**Dự đoán 1** *(Trần Thị Kiều Trang — mô hình kiếm tiền)*
- **Dự đoán:** Trong giai đoạn 08/2026–08/2027, Adobe sẽ đưa Shared Credits/pool credit xuống Creative Cloud Teams hoặc ra add-on tương đương, để admin nhóm nhỏ phân ngân sách và mua thêm lượt dùng model premium trong Photoshop.
- **Lập luận:** Mốc Neural Filters (2020) cho thấy Adobe đưa AI vào workflow chuyên nghiệp rồi cải thiện từ usage/feedback (§1), trong khi early adopters cần throughput ổn định để giao việc đúng hạn (§2). Hiện [partner models và tác vụ tốn compute dùng premium credits](https://helpx.adobe.com/creative-cloud/apps/generative-ai/creative-cloud-generative-ai-features.html), Photoshop đã cho [theo dõi/mua thêm credits](https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html), nhưng [Shared Credits yêu cầu điều kiện enterprise/ETLA](https://helpx.adobe.com/enterprise/using/generative-credit-pool.html). Mở xuống Teams là bước kiếm tiền theo usage mà không làm đứt workflow studio nhỏ.

**Dự đoán 2** *(Nguyễn Quy Dũng — mở rộng tính năng)*
- **Dự đoán:** Adobe sẽ tích hợp công cụ Multi-modal Real-time Canvas AI Control (điều khiển AI thời gian thực kết hợp nét cọ phác thảo + prompt ngôn ngữ tự nhiên) trực tiếp trên giao diện Canvas của Photoshop trong 6–12 tháng tới.
- **Lập luận:** Dẫn ngược từ mốc Select Subject (2018) và Generative Fill (2023) ở §1, cùng nhu cầu kiểm soát pixel-perfect của Early Adopters ở §2. Sau khi tự động hóa việc chọn vùng và tạo ảnh tĩnh, bước tiếp theo để giữ chân chuyên gia là tương tác điều chỉnh AI theo thời gian thực (real-time feedback loop).

**Dự đoán 3** *(Nguyễn Minh Quân — đe dọa Big Tech / sản phẩm AI-native)*
- **Dự đoán:** Trong 6–12 tháng tới, Photoshop sẽ mất phần lớn nhóm casual creator trên mobile vào tay Google Photos (Magic Editor/Magic Eraser miễn phí), Apple Intelligence (Clean Up, Image Playground) và Canva (260 triệu MAU, vừa mua Affinity, AI tích hợp sẵn). Adobe sẽ buộc phải tập trung giữ nhóm professional bằng cách mở rộng tích hợp model bên thứ ba (đã bắt đầu với FLUX.2 Pro, Gemini 3 trong Generative Fill) và nâng cao workflow chuyên sâu (Harmonize, Generative Upscale) thay vì chạy đua free tier.
- **Lập luận:** Mốc Photoshop Mobile miễn phí (02/2025) cho thấy Adobe ĐÃ nhận ra đe dọa và cố giành casual creator. Nhưng [Canva vẫn là AI tool tạo ảnh phổ biến nhất (51% influencer dùng Canva vs 36.4% Photoshop)](https://electroiq.com/stats/adobe-photoshop-vs-canva-statistics/). Google Photos Magic Editor đã miễn phí cho mọi user, Apple Clean Up có sẵn trên iPhone — cả hai KHÔNG cần download thêm app, trong khi Photoshop Mobile vẫn phải cạnh tranh với thứ đã CÓ SẴN trong máy. Mốc Generate Image + Firefly 3 (07/2024) cho thấy sức mạnh thực sự của Photoshop là wrapper/moat — nhúng AI vào workflow layers/masks/selections — thế mạnh chỉ phát huy với user CẦN workflow chuyên sâu, không phải casual creator chỉ muốn xóa nền hay thêm filter. Phân tích Habit cho thấy rào cản thoát của pro user (PSD, plugin, quy trình nhóm) vẫn rất cao → Adobe an toàn ở segment này; nhưng casual creator KHÔNG có Habit → không có gì giữ họ lại nếu có tool miễn phí, dễ hơn. *(Giả định rủi ro: Dự đoán sai nếu Adobe biến Photoshop Mobile thành "gateway" — user casual tích lũy file/kỹ năng rồi upgrade. Nhưng lịch sử freemium creative tools cho thấy tỷ lệ conversion thường rất thấp.)*

**Dự đoán bị loại và lý do:**

- **Photoshop làm aggregator AI đa model (Vũ Đình Huy):** insight về multi-model routing (nhúng Gemini/FLUX vào Generative Fill) đã được phản ánh trong phân tích moat/Push-Pull ở §2 và trong lập luận dự đoán 3; giữ thêm sẽ trùng góc nhìn Big Tech.

---

## §4. AI Log

| Việc | AI làm hay nhóm làm? | Nhóm kiểm chứng/phán đoán lại thế nào? |
|---|---|---|
| Cào dữ liệu lịch sử phiên bản từ Wikipedia & Adobe HelpX | AI thực hiện tự động qua script Python `source/crawl.py` | Nguyễn Quy Dũng đối chiếu file HTML gốc và ngày phát hành trên trang chính thức Adobe HelpX |
| Tổng hợp 2 mốc ứng viên AI nền tảng (CS5 Content-Aware Fill & Sensei Select Subject) | Nguyễn Quy Dũng nghiên cứu và ghi nhận | Dũng tự mở link Wikipedia & Adobe Release Notes để đối chiếu ngày phát hành và bối cảnh tính năng |
| Phân tích tệp Early Adopters (Đặc điểm & JTBD) | Nguyễn Quy Dũng xác định đặc điểm; nhóm chốt chung | Dũng đối chiếu với quy trình làm việc thực tế của photo retoucher/designer trước khi có AI |
| Dự đoán 2 (Multi-modal Real-time Canvas AI Control) | Nguyễn Quy Dũng đề xuất và lập luận | Nhóm kiểm tra tính khả thi công nghệ và khả năng dẫn ngược từ §1 và §2 |
| Tìm nguồn và tổng hợp hai mốc Neural Filters 2020 | AI (Codex) tìm, mở và đối chiếu nguồn Adobe/NVIDIA/OpenAI | **Trang cần tự mở từng link**, kiểm tra ngày và xác nhận nguồn hỗ trợ đúng nhận định; cả nhóm quyết định chọn/loại từng mốc |
| Revert mốc Neural Filters về nguyên lý `x10` | AI đề xuất mapping và viết bản nháp | Trang giải thích lại bằng lời của mình; nhóm đối chiếu tên nguyên lý với nội dung đã học và sửa nếu cần |
| Xây dựng JTBD và mô tả cách làm cũ của early adopters | AI tổng hợp từ đối tượng/workflow được Adobe mô tả | Trang đối chiếu với early adopters do Nguyễn Quy Dũng chốt; nhóm sửa nếu hai phần không cùng một tệp user |
| Viết dự đoán 1 — Shared Credits cho Teams | AI tổng hợp chính sách credits hiện tại và đưa ra suy luận | Nhóm kiểm tra Shared Credits chưa có sẵn cho Teams tại ngày nộp, phản biện giả định nhu cầu premium models rồi quyết định chọn/loại |
| Viết nội dung slide và speaker notes "AI trước Generative Fill" | AI viết bản nháp trong `member-2.md` | Trang rút gọn theo template Canva của nhóm, tự tập nói và chỉ giữ các nhận định có thể bảo vệ khi thảo luận |
| Audit link cuối memo | Trang và nhóm thực hiện | Mở lại toàn bộ link sau khi ghép; loại link hỏng, sai ngày hoặc không trực tiếp chứng minh nhận định |
| Viết mốc Generative Fill commercial (09/2023) và context ChatGPT/Midjourney | Vũ Đình Huy nghiên cứu và ghi nhận | Huy tự mở link Adobe sản phẩm Generative Fill, kiểm tra ngày phát hành chính thức (v25.0) và đối chiếu bối cảnh DALL-E/Midjourney |
| Viết dự đoán aggregator AI đa model (bị loại) | Vũ Đình Huy đề xuất từ phân tích mốc Generative Fill và switching cost | Nhóm kiểm tra tính khả thi, đối chiếu với model routing hiện có (Gemini/FLUX trong Generative Fill) và phản biện giả định Big Tech |
| Bổ sung mốc Generative Fill beta (05/2023) cho Vũ Đình Huy | AI (Claude) tìm nguồn Adobe Blog và Adobe Newsroom; Nguyễn Minh Quân yêu cầu bổ sung vì Huy thiếu 1 mốc | **Huy cần tự mở [link Adobe Blog 23/05/2023](https://blog.adobe.com/en/publish/2023/05/23/future-of-photoshop-powered-by-adobe-firefly)**, kiểm tra ngày và xác nhận context Midjourney v5/Firefly beta phù hợp |
| Điền cột "Tệp hiện tại" trong §2 (Đặc điểm, JTBD, Cách làm cũ) | AI (Claude) viết thay vì Vũ Đình Huy chưa hoàn thành; Nguyễn Minh Quân yêu cầu bổ sung để memo đủ nội dung | **Huy cần đọc lại và xác nhận** nội dung "Tệp hiện tại" khớp với phân tích Generative Fill và segment shift; nhóm đối chiếu với early adopters ở cột bên trái |
| Tổng hợp hai mốc Firefly for Enterprise (bị loại) và phát hành thương mại GenAI | AI (Codex) mở nguồn Adobe và viết bản nháp cho Lê Đình Việt | Việt tự mở lại từng link, phân biệt thông báo kế hoạch với tính năng đã phát hành và không diễn giải "commercially safe" thành an toàn bản quyền tuyệt đối |
| Phân tích wrapper/moat và hai lực Push/Pull | AI đề xuất cấu trúc; Lê Đình Việt chịu trách nhiệm phán đoán | Việt đối chiếu với user/JTBD do nhóm chốt và yêu cầu Nguyễn Minh Quân bổ sung Habit/Anxiety trước khi kết luận lực mạnh nhất |
| Đồng bộ deck Canva của nhóm | AI giữ nguyên trang 1–3 đã có và thay các trang template 4–10 bằng nội dung bám memo | Việt rà font, độ tương phản, lỗi chính tả, đối chiếu memo–slide, xuất `slides.pdf`; Nguyễn Minh Quân kiểm tra file PDF cuối |
| Tìm nguồn và tổng hợp 2 mốc Generate Image (07/2024) & Photoshop Mobile (02/2025) | AI (Claude) tìm kiếm, tổng hợp và đối chiếu nguồn Adobe Newsroom, Adobe Blog, TechCrunch, Forbes, VentureBeat | Quân tự mở từng link nguồn gốc (Adobe Newsroom & Adobe Blog), kiểm tra ngày phát hành và xác nhận nội dung khớp với nhận định đưa vào timeline |
| Phân tích Habit & Anxiety (4 forces) cho §2 | AI tổng hợp dữ liệu switching cost từ nhiều nguồn (Koder.ai, BizModelMastery, Adobe Community); Quân xác định cấu trúc và lập luận | Quân đối chiếu với trải nghiệm thực tế workflow Photoshop, loại bỏ nhận định không có nguồn hỗ trợ, xác nhận lực mạnh nhất dựa trên đánh giá cá nhân |
| Viết dự đoán 3 (đe dọa Big Tech) | AI đề xuất bản nháp dựa trên dữ liệu thị phần Canva, Google Photos, Apple Intelligence; Quân chỉnh sửa và bổ sung giả định rủi ro | Quân kiểm tra số liệu thị phần (Canva 260M MAU, 51% influencer) từ nguồn ElectroIQ và DemandSage; đối chiếu lập luận với 2 mốc đã đào; nhóm cần phản biện bằng 3 câu hỏi trước khi chọn |
| Tìm bằng chứng segment shift (pro → creator) | AI tổng hợp từ Forrester, Adobe Newsroom, Adobe Blog | Quân mở nguồn Forrester ("Shifting From Creator Tools To Creative Participation") và Adobe Newsroom ("Empower next generation of creators"), xác nhận nhận định phù hợp với 2 mốc timeline |
| Chốt 8 mốc, 3 dự đoán và hoàn thiện memo cuối | AI (Claude) đề xuất loại 2 mốc + 1 dự đoán, viết lý do; Nguyễn Minh Quân duyệt và chốt | Nhóm đọc lại memo trước khi nộp; đối chiếu nội dung đã loại có bị mất insight quan trọng không |
