import resend
import os

resend.api_key = os.getenv("RESEND_API_KEY")


def send_email(to_email, summary):

    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": [to_email],
        "subject": "Sales Insight Summary",
        "html": f"<pre>{summary}</pre>"
    })