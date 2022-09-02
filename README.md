# Selenium Python Test Automation Boilerplate

## Setup

1. Fork the repository.
2. Clone the repository.
    ```bash
    git clone https://github.com/<your_username>/selenium-python-test-automation-boilerplate.git
    ```
3. Move to the `selenium-python-test-automation-boilerplate` directory.
    ```bash
    cd selenium-python-test-automation-boilerplate
    ```
4. Install all the dependencies.
    ```bash
    make install
    ```
5. Run the `login_test`.
    ```bash
    make test f=tests/login_test.py
    ```

## Architecture

```
selenium-python-test-automation-boilerplate/
    helper/
        configuration_manager.py
        csv_parser.py
        webdriver_manager.py
        
    pages/
        base_page.py
        login_page.py
        products_page.py
        
    resources/
        test_data/
            login.csv
        config.properties
        
    tests/
        base_test.py
        login_test.py
        
    .gitignore
    Makefile
    README.md
    requirements.txt
```