import os

def send_notification(bill, summary, pdf_link):
    print("推播：")
    print(f"📌 {bill['title']}")
    print(f"📖 摘要：{summary}")
    print(f"📄 PDF：{pdf_link}")
