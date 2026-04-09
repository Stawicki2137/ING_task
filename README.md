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