from main import main
from main import Config


def test_config_reads_properties():
    config = Config()
    assert isinstance(config.name, str)
    assert isinstance(config.version, str)
    assert len(config.name) > 0
    assert len(config.version) > 0


def test_config_initialization():
    config = Config()
    project_setting = config.pyproject["project"]
    assert project_setting is not None
    assert "name" in project_setting
    assert "version" in project_setting


def test_main():
    main()
    assert True
