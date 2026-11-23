---
name: deliverability-checker
description: "Check email deliverability and DNS configuration by hand with dig. Use when: diagnosing email delivery issues; setting up new email domains; auditing email authentication; checking SPF/DKIM/DMARC; troubleshooting spam folder issues"
license: MIT
metadata:
  author: ClawFu
  version: 1.0.0
  note: "Hub 0 Mkt, 2026-10-20: the original scripts/main.py commands do not exist here; replaced by manual dig steps. Original kept in _arquivo/mescladas/r15b-email/."
---

# Email Deliverability Checker

> Diagnose email deliverability issues by checking SPF, DKIM, DMARC, and MX records - find why your emails land in spam.

## When to Use This Skill

- **Delivery troubleshooting** - Emails landing in spam
- **New domain setup** - Configure email authentication
- **Migration audit** - Verify email config after domain change
- **Client onboarding** - Check client email health
- **Compliance check** - Ensure proper authentication

## What Claude Does vs What You Decide

| Claude Does | You Decide |
|-------------|------------|
| Reads the DNS output you paste and explains each record | Which sending services are allowed on the domain |
| Spots missing or malformed SPF, DKIM, DMARC records | Whether to move DMARC from `p=none` to `quarantine` or `reject` |
| Writes the corrected TXT values | Who edits the DNS zone and when |
| Orders fixes by impact | Acceptable risk during the change |

Claude cannot query DNS from here. You run the commands below and paste the output.

## How to Check (manual, no script)

Replace `example.com` with the domain. Any machine with `dig` works.

### MX
```bash
dig +short MX example.com
```

### SPF
```bash
dig +short TXT example.com | grep "v=spf1"
```
Look for: exactly one `v=spf1` record, every sending service included, and an ending of `~all` or `-all`. More than 10 DNS lookups (`include:`, `a`, `mx`, `redirect`) makes SPF fail.

### DKIM
```bash
dig +short TXT google._domainkey.example.com
dig +short TXT selector1._domainkey.example.com
```
Try the selector of each provider (table below). An empty answer means that selector does not exist for the domain.

### DMARC
```bash
dig +short TXT _dmarc.example.com
```
Minimum to start: `v=DMARC1; p=none; rua=mailto:dmarc@example.com`.

## Reading the Result

| Finding | Meaning | Fix |
|---------|---------|-----|
| No `_dmarc` record | No policy and no reports (critical) | Add TXT on `_dmarc.example.com` with `p=none` and an `rua` address |
| SPF ends in `~all` | Soft fail; acceptable while testing | Move to `-all` once every sender is listed |
| Two `v=spf1` records | SPF is invalid | Merge into one record |
| DKIM empty for a selector | That provider is not signing | Publish the key the provider gives you |
| Missing MX | Cannot receive replies | Add the provider's MX records |

## Email Authentication Records

| Record | Purpose | Location |
|--------|---------|----------|
| **SPF** | Authorize sending servers | `TXT` on root domain |
| **DKIM** | Cryptographic signature | `TXT` on `selector._domainkey` |
| **DMARC** | Policy and reporting | `TXT` on `_dmarc` subdomain |
| **MX** | Mail delivery servers | `MX` on root domain |

## Common SPF Includes

| Provider | SPF Include |
|----------|-------------|
| Google Workspace | `include:_spf.google.com` |
| Microsoft 365 | `include:spf.protection.outlook.com` |
| SendGrid | `include:sendgrid.net` |
| Mailchimp | `include:servers.mcsv.net` |
| Amazon SES | `include:amazonses.com` |

## DKIM Selectors by Provider

| Provider | Common Selector |
|----------|-----------------|
| Google Workspace | `google` |
| Microsoft 365 | `selector1`, `selector2` |
| SendGrid | `s1`, `s2` |
| Mailchimp | `k1` |

## Deliverability Score Factors

Weights come from the original script's scoring and are a rule of thumb, not an industry standard.

| Factor | Weight | Impact |
|--------|--------|--------|
| Valid MX | 20% | Can't receive replies |
| Valid SPF | 25% | Server authorization |
| Valid DKIM | 25% | Message integrity |
| Valid DMARC | 30% | Policy enforcement |

## Related

- [dns-zonefile-config.md](dns-zonefile-config.md) - Zone files for SPF, DKIM, DMARC (French).
- [deliverability.md](deliverability.md) - Reputation, IP warm-up, list hygiene.
