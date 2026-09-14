"""
Day 25 - File Upload Vulnerability & Magic Bytes Validator
Validates the true binary signature of an uploaded file, independent
of its filename/extension, to prevent extension-spoofing bypasses.
"""

ALLOWED_SIGNATURES = {
    "PNG": b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A",
    "JPEG": b"\xFF\xD8\xFF",
    "GIF": b"GIF89a",
    "PDF": b"%PDF-",
}


def validate_magic_bytes(file_path: str) -> bool:
    try:
        with open(file_path, "rb") as f:
            file_header = f.read(16)
        for file_type, signature in ALLOWED_SIGNATURES.items():
            if file_header.startswith(signature):
                print(f"[+] VALIDATION PASSED: {file_path} matches {file_type} magic bytes.")
                return True
        print(f"[-] SECURITY EXCEPTION: {file_path} has an invalid/disallowed signature. Possible malicious upload.")
        return False
    except FileNotFoundError:
        print(f"[!] Error: File not found - {file_path}")
        return False


def _generate_test_samples():
    """
    Creates two local demo files at runtime (not shipped in the package,
    so nothing signature-matchable sits at rest in the zip):
    - a real PNG-signature file
    - a text file disguised with a .png extension, to prove the magic-bytes
      check catches a mismatched file type regardless of its name
    """
    with open("sample_real.png", "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + b"\x00" * 20)

    with open("sample_disguised.png", "w") as f:
        f.write("This is plain text content, not a real PNG file.\n")


if __name__ == "__main__":
    _generate_test_samples()
    for f in ["sample_real.png", "sample_disguised.png"]:
        validate_magic_bytes(f)
