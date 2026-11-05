import pandas as pd
import re

# Load CSV
df = pd.read_csv("support_tickets.csv")

def redact_sensitive_data(text):
    if pd.isna(text):
        return text

    # Redact email addresses
    text = re.sub(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        '[EMAIL_REDACTED]',
        text
    )

    # Redact phone numbers
    text = re.sub(
        r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        '[PHONE_REDACTED]',
        text
    )

    return text

# Apply redaction
df["comments"] = df["comments"].apply(redact_sensitive_data)

# Save output
df.to_csv("support_tickets_redacted.csv", index=False)

print("Redaction completed.")