# ALL-TOOLS-BUG-BOUNTY-GUI

**ALL-TOOLS-BUG-BOUNTY-GUI** is a lightweight graphical frontend that bundles and orchestrates popular open-source bug-bounty and reconnaissance tools into a single, easy-to-use interface.  
It is intended to speed up triage and recon workflows by exposing common operations (scan, fuzz, extract, test) as simple GUI actions while preserving the power and flexibility of the underlying CLI tools.

<p align="center">
  <img src="images/demo.png" alt="Demo GUI screenshot" width="900">
</p>

---

## What *ALL-TOOLS-BUG-BOUNTY-GUI* Means (detailed explanation)

**ALL-TOOLS-BUG-BOUNTY-GUI** is a descriptive name with three parts:

- **ALL-TOOLS** — indicates the project aggregates many CLI tools commonly used by security researchers and bug bounty hunters, providing a single place to run and manage them.
- **BUG-BOUNTY** — the domain: recon, scanning, verification and PoC generation workflows used in bug bounty programs.
- **GUI** — a graphical interface: it wraps CLI tools with a user-friendly UI so less CLI overhead is required and workflows become reproducible.

The GUI acts as an orchestrator: it executes canonical commands under the hood, manages outputs (endpoints lists, scan results, PoC files), and provides a single control panel to run, monitor and export results.

---

## Included / Supported Tools

This project is designed to integrate with (or make it easy to use) the following tools:

- **ffuf** — fast web fuzzer for directory & parameter discovery  
- **nuclei** — templated vulnerability scanner for CVEs and misconfigurations  
- **LinkFinder** — JavaScript endpoint extractor  
- **katana / hakrawler** — web crawlers for asset discovery  
- **sqlmap** — automated SQL injection testing (use responsibly and ONLY with permission)  
- **httpx / curl** — HTTP probing and header checks  
- Optional integrations: `amass`, `subfinder`, `gobuster`, `httpx`, `burpsuite` hook, etc.

Each tool is executed with safe defaults from the GUI; the raw commands are logged and saved for reproducibility.

---

## Features & Benefits

- One-click recon flows: crawl JS → extract endpoints → fuzz → scan.  
- Artifact management: per-target output folders (endpoints.txt, nuclei_results.txt, cors_results.txt, PoC HTML).  
- Safe presets & WAF tamper guidance for staging vs production.  
- Extensible: add new tool integrations and map them to GUI actions.  
- Exportable reports: generate Markdown/ZIP reports ready for bug-bounty reports.

---

## Installation (example)

```bash
git clone https://github.com/viaz2016/ALL-TOOLS-BUG-BOUNTY-GUI.git
cd ALL-TOOLS-BUG-BOUNTY-GUI

# Create and activate a python venv
python3 -m venv venv
source venv/bin/activate

# Install Python requirements (if provided)
pip install -r requirements.txt

# Ensure external CLI tools are installed separately:
# ffuf, nuclei, linkfinder (python), katana, sqlmap, httpx, etc.

# Run the GUI
python3 src/main.py

Quick start / Example workflow :

⦁	Enter a target URL in the target field (e.g. https://example.com).
⦁	Click Crawl to fetch JavaScript assets.
⦁	Run LinkFinder to extract endpoints from JS.
⦁	Run ffuf to fuzz candidate endpoints.
⦁	Run nuclei on the discovered endpoints for vulnerabilities.
⦁	Use the CORS checker to detect misconfigurations.
⦁	Export the project folder (report.zip) with all artifacts for reporting.

Example commands (what runs under the hood) :
⦁	ffuf -u https://target.com/FUZZ -w /path/wordlist.txt -fc 404
⦁	python3 linkfinder.py -i https://target.com/static/app.js -o cli
⦁	nuclei -l endpoints.txt -t ./nuclei-templates/http/api/ -o nuclei_results.txt
⦁	curl -sI -H "Origin: https://evil.com" https://target.com/api/endpoint

Responsible Use & Legal Notice

This project is intended for authorized security testing only. Always obtain written permission before testing systems you do not own. Unauthorized scanning or exploitation is illegal and unethical.

Contribution

Contributions are welcome: feature integrations, UI improvements, documentation, and tests. See CONTRIBUTING.md for details.
