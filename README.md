# OrangeHRM Web Application – Automation Testing Framework

##  Project Overview

This project is an **automated testing framework for the OrangeHRM web application**, developed using **Python, Playwright, Pytest, Page Object Model (POM), and Data-Driven Testing**.

The framework automates OrangeHRM functionalities by simulating real user actions and validating the expected application behavior. It is designed with a modular structure so that test cases, page objects, test data, utilities, and reports are maintained separately.

**Application under test:**
[https://opensource-demo.orangehrmlive.com/](https://opensource-demo.orangehrmlive.com/)


## 🎯 Project Objectives

The main objectives of this project are:

* Automate functional testing of the OrangeHRM web application.
* Validate important application modules and user workflows.
* Use **Playwright with Python** for browser automation.
* Use **Pytest** as the test execution framework.
* Implement the **Page Object Model (POM)** design pattern.
* Implement **Data-Driven Testing** using Excel test data.
* Reuse common page and utility methods.
* Execute tests on Chromium-based browsers, including **Microsoft Edge**.
* Generate detailed HTML execution reports.
* Store test results and actual results back into Excel.

## 🏗️ Framework Architecture

The project follows a layered automation framework:

Test Cases
    ↓
Page Object Classes
    ↓
Playwright
    ↓
OrangeHRM Web Application

Test Data
    ↓
Excel Utility
    ↓
Pytest Test Cases

Test Execution
    ↓
Pytest HTML Reports
    ↓
Browser Reports


## 📂 Project Structure

```text
Project2_OrangeHRM/
│
├── .venv/
│
├── chrome_reports/
│   ├── assets/
│   ├── Claim_TC#10_report.html
│   ├── different_user_login_TC#1_report.html
│   ├── Home_url_TC#2_report.html
│   ├── Login_field_TC#3_TC#4_report.html
│   ├── My_info_TC#8_report.html
│   ├── New_user_forgot_password_TC#5_TC#6_TC#7_report.html
│   └── TC#9_report.html
│
├── edge_browser_reports/
│   ├── assets/
│   ├── TC#1_report.html
│   ├── TC#2_report.html
│   ├── TC#3andTC#4_report.html
│   ├── TC#5andTC#6andTC#7_report.html
│   ├── TC#8_report.html
│   ├── TC#9_report.html
│   └── TC#10_report.html
│
├── Pages/
│   ├── __init__.py
│   ├── Adminpage.py
│   ├── Basepage.py
│   ├── Claimpage.py
│   ├── dashboard_user.py
│   ├── Dashboardpage.py
│   ├── ForgotPasswordPage.py
│   ├── Leavepage.py
│   ├── login_user.py
│   ├── Loginpage.py
│   └── Myinfopage.py
│
├── test_data/
│   ├── __init__.py
│   └── Data.xlsx
│
├── tests/
│   ├── __init__.py
│   ├── test_assignleave.py
│   ├── test_claim.py
│   ├── test_createnewuser.py
│   ├── test_homeurl_validation.py
│   ├── test_login_differentuser.py
│   ├── test_loginfield_validation.py
│   └── test_myinfo_verification.py
│
├── Utils/
│   ├── config.py
│   └── excel_utils.py
│
└── conftest.py



# 🌐 Browser Automation with Playwright

Playwright is used to automate browser interactions.

The framework can be configured to execute tests in browsers such as:

* Chromium
* Microsoft Edge

# 🧱 Page Object Model (POM)

The framework follows the **Page Object Model** design pattern.

Instead of placing locators and browser actions directly inside test cases, page-specific functionality is maintained inside page classes.

Structure of POM

Test Case
    ↓
Page Object
    ↓
Locators + Methods
    ↓
Playwright
    ↓
Application
```

### Advantages

* Better code reusability
* Reduced code duplication
* Easier maintenance
* Cleaner test cases
* Centralized locators
* Easier application changes
* Improved readability

---

# 🧪 Pytest Framework

Pytest is used as the test execution framework.

The tests are organized under:

```text
tests/
```

Pytest provides:

* Test discovery
* Fixtures
* Assertions
* Parameterization
* Test execution
* HTML reporting
* Failure information

---

The reports contain information such as:

* Test execution status
* Passed tests
* Failed tests
* Test duration
* Test names
* Failure details
* Execution environment information

# 🔍 Test Result Management

The framework maintains test results in both:

### HTML Reports

Used for detailed execution analysis.

### Excel

Used for storing:

* Test result
* Actual result



# 🔐 Application Credentials

The project uses the OrangeHRM demo application.

Application URL:

```text
https://opensource-demo.orangehrmlive.com/
```

Test credentials should be maintained in the project's test-data/configuration mechanism rather than hardcoded throughout individual test cases.

---

# 📈 Framework Benefits

This framework provides:

* ✅ Automated functional testing
* ✅ Python + Playwright automation
* ✅ Pytest-based execution
* ✅ Page Object Model architecture
* ✅ Data-driven testing
* ✅ Excel-based test data management
* ✅ Reusable fixtures
* ✅ Reusable page methods
* ✅ HTML test reports
* ✅ Test-result tracking
* ✅ Chrome/Edge execution support

---

# 📌 Key Design Principles

The project follows these automation principles:

### Separation of Concerns

Test logic, page actions, test data, configuration, and reporting are maintained separately.

### Reusability

Common browser operations and page methods are reused across multiple tests.

### Maintainability

Locators are maintained within page classes, making application changes easier to manage.

### Data Independence

Test input is maintained in Excel rather than being tightly coupled with test implementation.

### Reporting

Both HTML and Excel-based results are maintained for test analysis.

---

# 🏁 Conclusion

The **OrangeHRM Automation Testing Project** demonstrates a structured Selenium/Playwright-style automation framework implemented using **Python + Playwright + Pytest + POM + Data-Driven Testing**.

The framework provides a scalable foundation for automating OrangeHRM workflows while maintaining test data separately, reusing page objects, executing tests through Pytest, and generating HTML execution reports.

It can be further enhanced by adding CI/CD integration, screenshots and videos on failure, parallel execution, logging, environment-specific configuration, and richer reporting.
