from build_database import build_database


def pytest_configure():
    build_database()
