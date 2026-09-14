"""
Day 21 - Cross-Site Scripting (XSS) Payload Sanitizer
Encodes and strips dangerous tokens from untrusted input before display.
"""
import html
import re


def sanitize_user_input(raw_payload: str) -> str:
    encoded_string = html.escape(raw_payload)
    stripped_output = re.sub(r"(?i)script|onerror|onload|javascript:", "[PROHIBITED_TOKEN]", encoded_string)
    return stripped_output


ADVERSARIAL_TESTS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "<svg onload=alert('xss')>",
    "javascript:alert(document.cookie)",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<a href=\"javascript:alert('href-xss')\">click</a>",
    "<body onload=alert('body')>",
    "<div onmouseover=\"alert('hover')\">hover me</div>",
    "'><script>alert(String.fromCharCode(88,83,83))</script>",
    "Plain safe text with no payload",
]

if __name__ == "__main__":
    for payload in ADVERSARIAL_TESTS:
        print(f"Raw Input      : {payload}")
        print(f"Neutralized    : {sanitize_user_input(payload)}\n")
