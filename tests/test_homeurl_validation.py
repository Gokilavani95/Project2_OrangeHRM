#Test-Case-2:Scenario: Verify that the home URL is accessible

def test_home(page):
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" in page.url.lower()
    print("success")

