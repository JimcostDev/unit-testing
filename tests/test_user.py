import pytest
from faker import Faker
from src.user import User
from src.bank_account import BankAccount
import copy


@pytest.fixture
def setup_user():
    """Fixture para crear un usuario con Faker."""
    fake = Faker(locale="es")
    user = User(name=fake.name(), email=fake.email())
    return user

def test_user_creation(setup_user):
    """Prueba que verifica la creación de un usuario."""
    user = copy.deepcopy(setup_user)  # Crear una copia independiente
    assert user.name == setup_user.name
    assert user.email == setup_user.email
    
    
def test_multiple_accounts(setup_user):
    """Prueba que verifica la creación de múltiples cuentas."""
    fake = Faker(locale="es")
    for _ in range(3):
        account = BankAccount(fake.random_int(min=100, max=2000, step=50))
        setup_user.add_account(account)
        
        expected_balance = setup_user.get_total_balance()
        value = sum(account.get_balance() for account in setup_user.accounts)
        print(f"Balance esperado: {expected_balance}, Balance actual: {value}")
        assert value == expected_balance
        