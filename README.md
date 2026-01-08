# **Liver Diseases Detection**

## A Flask-based web application for liver diseases prediction from histopathology images.

## Dataset: https://universe.roboflow.com/roboflow-100/liver-disease

## Cấu trúc dataset: 3976 ảnh
|  | Train | Valid | Test |
|---|---|---|---|
| Ballooning | 698 | 198 | 100 |
| Fibrosis | 694 | 198 | 100 |
| Inflammation | 688 | 196 | 100 |
| Steatosis | 693 | 198 | 99 |
| null | 8 | 4 | 0 |

## Tài liệu tham khảo: 
## https://docs.roboflow.com/datasets/dataset-versions/image-preprocessing
## https://docs.roboflow.com/datasets/dataset-versions/image-augmentation
## https://docs.roboflow.com/annotate/use-roboflow-annotate#mark-null



## **Link demo:** [![Render](https://img.shields.io/badge/Render-Live_App-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://breastcancer-detection-4o3g.onrender.com/)

## **Flowchart:**
```mermaid
flowchart TD

    subgraph Initialization [Khởi tạo Hệ thống]
        LoadWeight[Load file trọng số best_model.pt <br> vào RAM]
    end

    subgraph Client [Xử lý yêu cầu]
        A(Bắt đầu: User chọn ảnh) --> B[JS: tạo formData cho file ảnh];
        B --> C[JS: gửi Fetch API 'POST' đến /api/predict];
        G[JS: Nhận response JSON] --> H[JS: Gán chuỗi Base64 vào img Data URL];
        H --> I[Hiển thị ảnh đã bounding box và text kết quả];
        I --> J(Kết thúc: User thấy kết quả);
        
    end

    subgraph "Backend"
        C --> D[Flask: /api/predict nhận request];
        D --> E[Chuyển đổi dữ liệu ảnh bytes sang định dạng PIL Image. <br>Gọi model YOLOv8 để phát hiện đối tượng];
        E --> F[Sử dụng .plot của Ultralytics để tự động vẽ bounding box và gán nhãn lên ảnh];
        F --> G[Gửi response JSON lên frontend<br>Gồm ảnh kết quả đã được encoded Base64 và kết quả chứa tên lớp và độ tin cậy];

    end

    
