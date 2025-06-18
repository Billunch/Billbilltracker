from bill_parser import parse_bills
from grok_summary import summarize_bill
from notifier import send_notification
from pdf_fetcher import fetch_pdf_link  # ✅ 正確寫法，去掉 .py

def run_tracker():
    bills = parse_bills()
    count = 0

    for bill in bills:
        summary = summarize_bill(bill)
        pdf_link = fetch_pdf_link(bill)
        send_notification(bill, summary, pdf_link)
        count += 1

    return f"✅ Tracker finished. {count} bills processed."
