import pytest
from main import Config


def test_config_reads_properties():
    """Test that config can be created and properties work."""
    config = Config()
    assert isinstance(config.name, str)
    assert isinstance(config.version, str)
    assert len(config.name) > 0
    assert len(config.version) > 0


def test_config_initialization():
    """Test that Config initializes without errors."""
    config = Config()
    assert config.config is not None
    assert "name" in config.config
    assert "version" in config.config