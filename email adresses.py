import re
def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    valid_emails = [email for email in emails if re.match(email_pattern, email)]
    return valid_emails
text_sample = "Please contact support@example.com for assistance or info@company.com for more information."
result = extract_emails(text_sample)
print("Extracted Email Addresses:",result)
