import re

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================

def process_pdf_data(raw_json: dict) -> dict:
    # Bước 1: Làm sạch nhiễu (Header/Footer) khỏi văn bản
    raw_text = raw_json.get("extractedText", "")

    # Dùng re.sub để xóa 'HEADER_PAGE_X' và 'FOOTER_PAGE_X'
    cleaned_content = re.sub(r'(HEADER|FOOTER)_PAGE_\d+', '', raw_text).strip()

    # Bước 2: Map dữ liệu thô sang định dạng chuẩn của UnifiedDocument
    return {
        "document_id": raw_json.get("docId", ""),
        "source_type": "PDF",
        "author": raw_json.get("authorName", "").strip(),
        "category": raw_json.get("docCategory", ""),
        "content": cleaned_content,
        "timestamp": raw_json.get("createdAt", ""),
    }

def process_video_data(raw_json: dict) -> dict:
    # Map dữ liệu thô từ Video sang định dạng chuẩn (giống PDF)
    return {
        "document_id": raw_json.get("video_id", ""),
        "source_type": "Video",
        "author": raw_json.get("creator_name", ""),
        "category": raw_json.get("category", ""),
        "content": raw_json.get("transcript", ""),
        "timestamp": raw_json.get("published_timestamp", ""),
    }
