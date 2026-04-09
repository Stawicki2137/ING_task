# ING Cookie Consent Automation Task

Automated E2E test for the cookie consent flow on the **ing.pl** website, developed as a recruitment task.

## Project Overview
The test automates the following scenario:
1. Navigates to the ING home page.
2. Opens the cookie customization menu ("Dostosuj").
3. Consents to analytical cookies.
4. Verifies if the `cookiePolicyGDPR` cookie is correctly saved with the expected value.

## Prerequisites
- Python 3.8+
- [Playwright](https://playwright.dev/python/)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Stawicki2137/ING_task
   cd ING_task 
   ```
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Install browser engines**
   ```bash
    playwright install
   ```

## Running Test

1. **Cross browser execution**
```bash
pytest test_ing_analytical_cookies.py --browser chromium --browser firefox --browser webkit
```
2. **Headed mode**
```bash
pytest test_ing_analytical_cookies.py --headed --slowmo 600
```
3. **With console output**
```bash 
pytest test_ing_analytical_cookies.py -s
```

## Configuration Details
**The test is configured to ignore HTTPS errors to ensure stability across all browser engines, especially WebKit.**

## CI/CD Execution & Bot Protection
The automated tests currently **fail on GitHub Actions** while passing successfully on a **local environment**.

### Why is this happening?
The production website `ing.pl` employs an advanced **Web Application Firewall** and **hCaptcha** protection. 
- **CI/CD Run:** GitHub Actions runners use data center IP addresses (Azure), which are automatically flagged as "suspicious/bot traffic" by the bank's security systems, triggering a human verification challenge.

### My Approach (Diagnostic & Robustness)
Instead of ignoring the failure, the project includes several features:
1. **Diagnostic Logs:** The test includes a pre-condition check. If hCaptcha is detected, it prints a clear warning in the console instead of just failing on a missing element.
2. **Automated Artifacts:** The CI/CD pipeline is configured to capture screenshots **only on failure**, allowing for quick visual debugging of environmental blocks.
3. **Localization Handling:** The test forces the `pl-PL` locale and timezone to ensure consistent behavior regardless of the runner's physical location.
