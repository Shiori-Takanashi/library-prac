from pytest import CaptureFixture

from core.presenter.presenter import show_info, transform_info


def test_transform_info() -> None:
    info = [{"a": "1", "b": "2"}]
    assert transform_info(info) == [["1", "2"]]


def test_show_info_stdout(capsys: CaptureFixture[str]) -> None:
    info = [{"x": "10", "y": "20"}]
    show_info(info)
    captured = capsys.readouterr().out.strip()
    assert captured == "10, 20"
