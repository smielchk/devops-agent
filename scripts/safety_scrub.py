import os
import re
import sys

# 常见的敏感信息模式
PATTERNS = [
    r'(?i)sk-[a-zA-Z0-9]{32,}',  # OpenAI
    r'(?i)ghp_[a-zA-Z0-9]{36}',   # GitHub
    r'(?i)password\s*[:=]\s*[^\s]+',
    r'(?i)api_key\s*[:=]\s*[^\s]+',
    r'(?i)client_secret\s*[:=]\s*[^\s]+',
]

def scan_file(filepath):
    found = []
    try:
        with open(filepath, 'r', errors='ignore') as f:
            for i, line in enumerate(f, 1):
                for pattern in PATTERNS:
                    if re.search(pattern, line):
                        found.append((i, pattern))
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return found

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 safety_scrub.py <file_or_dir>")
        sys.exit(1)

    target = sys.argv[1]
    issues_found = False

    if os.path.isfile(target):
        files = [target]
    else:
        files = []
        for root, _, filenames in os.walk(target):
            if '.git' in root: continue
            for f in filenames:
                files.append(os.path.join(root, f))

    for filepath in files:
        issues = scan_file(filepath)
        if issues:
            issues_found = True
            print(f"⚠️  SENSITIVE DATA FOUND in {filepath}:")
            for line_no, pattern in issues:
                print(f"  - Line {line_no}: Matches pattern {pattern}")

    if issues_found:
        print("\n❌ STOP: Sensitive data detected. Please move secrets to .env or use environment variables.")
        sys.exit(1)
    else:
        print("✅ No sensitive data detected.")
        sys.exit(0)

if __name__ == "__main__":
    main()
