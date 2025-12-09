#!/usr/bin/env python3
"""
Email domain checker for Polza test task.

Usage:
    python check_emails.py emails.txt

The script accepts ANY formatting of email list:
- one per line
- separated by commas
- separated by spaces
- mixed formatting

Output statuses:
- «домен валиден»
- «домен отсутствует»
- «MX-записи отсутствуют или некорректны»
"""

import sys
import re
import dns.resolver


def extract_domain(email: str) -> str | None:
    """Extract domain from email, return None if invalid."""
    if "@" not in email:
        return None
    try:
        local, domain = email.rsplit("@", 1)
        domain = domain.strip()
        return domain if domain else None
    except ValueError:
        return None


def check_domain(domain: str) -> str:
    """
    Check MX records for domain.

    Returns one of:
    - "домен валиден"
    - "домен отсутствует"
    - "MX-записи отсутствуют или некорректны"
    """
    try:
        # Attempt MX lookup
        answers = dns.resolver.resolve(domain, 'MX', lifetime=3)
        if answers:
            return "домен валиден"
        else:
            return "MX-записи отсутствуют или некорректны"

    except dns.resolver.NXDOMAIN:
        return "домен отсутствует"
    except (dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.exception.Timeout):
        return "MX-записи отсутствуют или некорректны"
    except Exception:
        return "MX-записи отсутствуют или некорректны"


def parse_emails_from_file(path: str) -> list[str]:
    """Read file and extract emails from any formatting."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by commas, spaces, tabs, newlines
    raw_items = re.split(r"[,\s]+", content)
    emails = [item.strip() for item in raw_items if item.strip()]
    return emails


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_emails.py <emails_file>")
        sys.exit(1)

    path = sys.argv[1]
    emails = parse_emails_from_file(path)

    for email in emails:
        domain = extract_domain(email)
        if not domain:
            print(f"{email} — MX-записи отсутствуют или некорректны")
            continue

        status = check_domain(domain)
        print(f"{email} — {status}")


if __name__ == "__main__":
    main()
