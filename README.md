# pytest-cleanuptotal

This plugin for [pytest](https://github.com/pytest-dev/pytest) and for [playwright-pytest](https://github.com/microsoft/playwright-pytest) helps simplify test cleanup. It does so by providing a systematic way to mark entities for deletion immediately after creation. This is particularly useful when tests involve creating complex structures, such as a bank account with an investment plan and a deposit. Without proper cleanup, attempting to delete the account may result in errors, such as a refusal due to the account not being empty. However, with **pytest-cleanuptotal**, entities are deleted in the correct order, ensuring that tests clean up after themselves and do not interfere with each other. Read more [here](https://www.linkedin.com/pulse/test-automation-cleanup-advanced-plugin-playwright-tzur-paldi-phd/?trackingId=8R68dOtBSHKrCH0cNAviIA%3D%3D).

## Installation

```
$ pip install pytest-cleanuptotal
```

## Usage

To use pytest-cleanuptotal, simply add the **cleanuptotal** fixture to the test method. This will include the cleanup functionality in your test. No further setup is required. Here's an example:

```python
def test_should_keep_things_tidy(cleanuptotal):
            # ...

            account_id = create_account("John Blow");
            amount = 1000000
            
            # usage of cleanuptotal with lambda function:
            cleanuptotal.add_cleanup(lambda: delete_account(account_id))

            add_investment_plan(account_id, "ModRisk");

            cleanuptotal.add_cleanup(lambda: remove_investment_plan(account_id))
            
            deposit(account_id, amount);

            def remove_deposit():
              url = f"https://api.example.com/user/{accountId}/withdraw"
              data = {"amount": amount}
              response = requests.post(url, json=data)
            
            # usage of cleanuptotal with regular function:
            cleanuptotal.add_cleanup(remove_deposit)

            # ...

        # Please note that the actual execution of the cleanup code would take palce AFTER test completion.
        # Execution order in cleanuptotal would be remove_deposit() -> remove_investment_plan(account_id) -> delete_account(account_id).
```

To use type hints follow this example:

```python
from pytest_cleanuptotal.cleanup import Cleanup

def test_should_keep_things_tidy(cleanuptotal:Cleanup):
            # ... your test code here
```

## Logging

To see all the *pytest-cleanuptotal* logging change the log level to 'DEBUG' (e.g., in your project's pytest.ini)

## Support

For any questions or suggestions contact me at: [tzur.paldi@outlook.com](mailto:tzur.paldi@outlook.com?subjet=pytest-cleanuptotal%20Support)

📬 Maintained by [Tzur Paldi](https://github.com/tzurp) — explore my GitHub profile for more tools.
