import builtins
from src.calculator import calculator


def test_addition_flow(monkeypatch, capsys):
    inputs = iter(["1", "2", "3", "n"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    calculator()
    captured = capsys.readouterr()

    assert "Result: 5.0" in captured.out
    assert "Goodbye" in captured.out or "Exiting calculator" in captured.out


def test_invalid_choice(monkeypatch, capsys):
    inputs = iter(["9", "5"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    calculator()
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out


def test_divide_by_zero(monkeypatch, capsys):
    # Simulate user choosing divide, then entering 10 and 0, then quitting
    inputs = iter(["4", "10", "0", "n"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    calculator()
    captured = capsys.readouterr()
    assert "Error: Division by zero is not allowed." in captured.out


def test_non_numeric_input(monkeypatch, capsys):
    # Simulate user entering letters instead of numbers
    inputs = iter(["1", "a", "b", "n"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    calculator()
    captured = capsys.readouterr()
    assert "Invalid input" in captured.out


def test_repeat_calculation(monkeypatch, capsys):
    # User does addition, then chooses to calculate again
    inputs = iter(["1", "2", "3", "y", "2", "5", "3", "n"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    calculator()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out  # First calculation
    assert "Result: 2.0" in captured.out  # Second calculation (subtract)