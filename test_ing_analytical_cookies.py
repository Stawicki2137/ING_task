import pytest 
from playwright.sync_api import Page, expect

PAGE_URL = "https://www.ing.pl"
CONSENT_STATE_COOKIE_NAME = "cookiePolicyGDPR"
EXPECTED_COOKIE_VALUE = "3"

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "locale": "pl-PL",
        "timezone_id": "Europe/Warsaw",
    }

def test_ing_cookies_acceptance(page: Page):
    page.goto(PAGE_URL,timeout=60000)
    page.wait_for_load_state("networkidle")

    if page.locator("text=Jestem człowiekiem").is_visible():
        print("\n[WARNING] hCaptcha detected! Test cannot proceed on this environment.")
        return
    
  
    dostosuj_btn = page.get_by_role("button", name="Dostosuj")
    expect(dostosuj_btn).to_be_visible(timeout=10000)
    dostosuj_btn.click()
    
    cookies_analityczne_toggle = page.get_by_role("heading", name="Cookies analityczne")
    expect(cookies_analityczne_toggle).to_be_visible()
    cookies_analityczne_toggle.click()

    zaakceptuj_btn = page.get_by_role("button", name="Zaakceptuj zaznaczone")
    expect(zaakceptuj_btn).to_be_visible()
    zaakceptuj_btn.click()

    expect(zaakceptuj_btn).not_to_be_visible()

    cookies = page.context.cookies()
    gdpr_cookie = next((cookie for cookie in cookies if cookie["name"] == CONSENT_STATE_COOKIE_NAME), None)
    assert gdpr_cookie is not None, f"Error: {CONSENT_STATE_COOKIE_NAME} cookie not found!"
    
    print(f"\nCookie '{CONSENT_STATE_COOKIE_NAME}' value: {gdpr_cookie['value']}")

    assert gdpr_cookie["value"] == EXPECTED_COOKIE_VALUE, f"Expected value '{EXPECTED_COOKIE_VALUE}', but received '{gdpr_cookie['value']}'"
    print("\n[SUCCESS] Test completed: Cookies saved correctly.")

