import os
import logging
import tempfile
import shutil
import pytest
from app import logs

@pytest.fixture
def temp_log_dir():
    dirpath = tempfile.mkdtemp()
    yield dirpath
    shutil.rmtree(dirpath)

def test_setup_logger_creates_log_file_and_logs_info(temp_log_dir, capsys):
    log_file = os.path.join(temp_log_dir, "test.log")
    logs.setup_logger(log_file)
    test_message = "This is an info message"
    logs.log_info(test_message)

    # Check file exists
    assert os.path.exists(log_file)

    # Check message in log file
    with open(log_file, encoding="utf-8") as f:
        content = f.read()
    assert test_message in content
    assert "[INFO]" in content

    # Check message in stdout
    captured = capsys.readouterr()
    assert test_message in captured.out

def test_log_error_logs_error_message(temp_log_dir, capsys):
    log_file = os.path.join(temp_log_dir, "error.log")
    logs.setup_logger(log_file)
    error_message = "This is an error"
    logs.log_error(error_message)

    with open(log_file, encoding="utf-8") as f:
        content = f.read()
    assert error_message in content
    assert "[ERROR]" in content

    captured = capsys.readouterr()
    assert error_message in captured.out

def test_setup_logger_creates_directory_if_not_exists(tmp_path):
    log_dir = tmp_path / "logs"
    log_file = log_dir / "app.log"
    logs.setup_logger(str(log_file))
    assert log_dir.exists()
    assert log_file.exists()