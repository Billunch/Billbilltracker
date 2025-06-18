def fetch_pdf_link(bill):
    return f"https://www.congress.gov/bill/{bill['congress']}/congressional-bill/{bill['bill_type']}{bill['number']}/text"
