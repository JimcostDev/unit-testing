from datetime import datetime
import pytest
import os
from src.bank_account import BankAccount
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError
from unittest.mock import patch

@pytest.fixture
def setup_account():
    # Crear la cuenta con un archivo de log específico
    account = BankAccount(balance=1000, log_file='transaction_log.txt')
    yield account  # Cede el control para la prueba
    # Teardown: elimina el archivo de log después de cada prueba
    if os.path.exists(account.log_file):
        os.remove(account.log_file)

def test_deposit(setup_account):
    new_balance = setup_account.deposit(250)
    assert new_balance == 1250  # Balance inicial (1000) + depósito (250)
    
def test_withdraw(setup_account):
    setup_account.deposit(4000)  # 1000 + 4000 = 5000
    new_balance = setup_account.withdraw(2000)
    assert new_balance == 3000  # Balance esperado después de retirar
    
def test_get_balance(setup_account):
    assert setup_account.get_balance() == 1000  # Verifica el balance inicial

def test_transaction_log(setup_account):
    # Verifica que el archivo de log existe después de una operación
    setup_account.deposit(100)
    assert os.path.exists('transaction_log.txt') is True


def test_count_transactions(setup_account):
    assert setup_account._count_lines() == 1  # Revisa que haya una línea en el log
    setup_account.deposit(500)  # Genera otra línea
    assert setup_account._count_lines() == 2  # Ahora debe haber dos líneas
    
def test_account_type(setup_account):
    assert isinstance(setup_account, BankAccount) 

def test_withdraw_insufficient_funds(setup_account):
    # Intenta retirar más de lo que hay en la cuenta
    with pytest.raises(InsufficientFundsError, match="Withdrawal of 2000 exceeds balance 1000"):
        setup_account.withdraw(2000) 
        
    
# saltar pruebas
@pytest.mark.skip(reason="Trabajo en progreso")
def test_deposit_skip():
    # Esta prueba será omitida
    result = 1000 + 250
    assert result == 1250

import sys
@pytest.mark.skipif(sys.platform == "win32", reason="No se ejecuta en Windows")
def test_withdra_skip():
    # Esta prueba solo se ejecutará en plataformas que no sean Windows
    result = 1000 - 250
    assert result == 750


@pytest.mark.skipunless(sys.platform == "linux", reason="Solo se ejecuta en Linux")
def test_linux_only_feature():
    # Esta prueba solo se ejecutará en sistemas Linux
    assert 1 + 1 == 2
    
@patch("src.bank_account.datetime")
def test_withdraw_disallow_before_bussines_hours(mock_datetime, setup_account):
    mock_datetime.now.return_value.hour = 10
    # Verifica que se lanza la excepción al intentar retirar fuera del horario permitido
    with pytest.raises(WithdrawalTimeRestrictionError):
       setup_account.withdraw(100)
       