from spark_optimisation import Config, main


def test_config_reads_properties():
    config = Config()
    assert isinstance(config.name, str)
    assert isinstance(config.version, str)
    assert len(config.name) > 0
    assert len(config.version) > 0


def test_config_initialization():
    config = Config()
    project_config = config.pyproject["project"]
    assert project_config is not None
    assert "name" in project_config
    assert "version" in project_config


def test_main():
    main()
    assert True
