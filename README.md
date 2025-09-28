# ALL-TOOLS-BUG-BOUNTY-GUI

**ALL-TOOLS-BUG-BOUNTY-GUI** is a lightweight graphical frontend that bundles and orchestrates popular open-source bug-bounty and reconnaissance tools into a single, easy-to-use interface.  
It is intended to speed up triage and recon workflows by exposing common operations (scan, fuzz, extract, test) as simple GUI actions while preserving the power and flexibility of the underlying CLI tools.

<p align="center">
  <img src="images/demo.png" alt="Demo GUI screenshot" width="900">
</p>

---

## What *ALL-TOOLS-BUG-BOUNTY-GUI* Means (detailed explanation)

**ALL-TOOLS-BUG-BOUNTY-GUI** is a descriptive name with three parts:

- **ALL-TOOLS** — indicates the project is an aggregator: instead of forcing users to memorize and run multiple command-line binaries one-by-one, this project integrates many of the most commonly used tools for reconnaissance and testing into one cohesive package. It focuses on the *tools* that bug bountiers use most often (fuzzers, scanners, crawlers, extractors, and lightweight exploit testers).

- **BUG-BOUNTY** — the intended domain: workflows and tasks common to bug-bounty hunters and security researchers (asset discovery, endpoint enumeration, vulnerability scanning, preliminary verification, and proof-of-concept generation).

- **GUI** — a graphical interface: the project wraps CLI tools with a user interface (desktop or web) that reduces friction for repetitive tasks, enables safe presets, and makes it easier to share workflows with teammates or less-CLI-savvy collaborators.

In practice, the GUI acts as an orchestrator: it runs canonical commands under the hood, manages output and artifacts (logs, HTTP responses, PoC files), and gives the user a single panel to launch, monitor, and export results. That keeps repeatable recon methodology, saves time and reduces manual mistakes.

---

## Included / Supported Tools (what they are and how GUI uses them)

> *The list below describes common tools that this GUI bundles or is designed to integrate with. Your repo may include a subset — adapt to what you ship.*

### `ffuf` — Fast web fuzzer
- **What it is:** A fast HTTP fuzzing tool used for directory, parameter, and content discovery.
- **Common GUI uses:** run endpoint enumeration against `/api/FUZZ` paths, show live results table with status code and content-length, export discovered endpoints to a file for follow-up scanning.

### `nuclei`
- **What it is:** A fast vulnerability scanner that runs templated checks (CVE, misconfig, exposures).
- **Common GUI uses:** select template sets (http/api/exposures) and run them against discovered endpoints; provide severity filtering and store findings with template references.

### `LinkFinder`
- **What it is:** A JavaScript link/endpoint extractor (scans JS for hard-coded API endpoints).
- **Common GUI uses:** fetch remote JS files, extract URLs and endpoints, add candidates to a queue or endpoint list for brute-force and nuclei scanning.

### `katana` / `hakrawler` (crawlers)
- **What they are:** Link crawlers that traverse a website and collect assets (JS, paths).
- **Common GUI uses:** crawl a domain with configurable depth/timeouts, show collected asset list, optionally pass JS assets to LinkFinder.

### `sqlmap`
- **What it is:** An automated SQL injection and database testing tool.
- **Common GUI uses (safe):** detect SQLi vulnerabilities with controlled tests (time-based or boolean), store detection logs, and allow responsible, non-destructive fingerprinting. **(Only use with explicit permission.)**

### `httpx` / `curl`
- **What they are:** HTTP probing and ad-hoc request tools.
- **Common GUI uses:** quick endpoint probes, collecting headers (CORS, cookies), and lightweight response comparisons (production vs staging).

### `others` (optional)
- `subfinder` / `amass` — subdomain discovery
- `shodan` / `wayback` integration — passive intelligence
- `gobuster` — alternative brute-force
- `burpsuite` integration hook — for sending items to active scanner

---

## Features & Benefits

- **One-click runs:** pre-configured runs for common recon flows (JS extraction → endpoint list → nuclei scan).
- **Artifact management:** keep per-target folders of outputs (endpoints.txt, nuclei_results.txt, cors_results.txt, PoC HTML).
- **Safe defaults:** conservative timeouts, optional WAF tamper presets and guidance for staging vs production.
- **Extensible:** add new CLI tools and map them to GUI actions.
- **Exportable reports:** generate markdown/zip reports of findings for bug-bounty submission.

---

## Installation (example)

> This example assumes a Unix-like environment and that you have the required CLI tools installed (or you will install them separately). Adjust for Windows if needed.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# Create and activate a python venv (recommended)
python3 -m venv venv
source venv/bin/activate

# Install Python requirements (if provided)
pip install -r requirements.txt

# Ensure external tools are installed:
# ffuf, nuclei, sqlmap, katana, httpx, etc.
# e.g. on Debian/Ubuntu you might use apt / snap / or prebuilt binaries.

# Run the GUI
python3 src/main.py
