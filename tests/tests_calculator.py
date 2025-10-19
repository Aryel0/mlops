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
