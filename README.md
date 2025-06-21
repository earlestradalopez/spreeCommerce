Project Structure
`
project/
│
├── tests/
│   ├── test_login.py
│   └── test_order.py
│   └── test_signup.py
│   └── conftest.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── main_page.py
│
├── utils/
│   └── helpers.py
│
├── requirements.txt
└── pytest.ini
`

⚙️ Step-by-Step Implementation
1. Install Playwright for Python
bash
Copy
Edit
pip install playwright pytest
playwright install

2. Run Automation
`pytest -q`
