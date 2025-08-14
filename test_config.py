import pytest
import tempfile
import os
from unittest.mock import patch, mock_open
from main import Config


class TestConfig:
    """Test cases for the Config class."""

    def test_config_initialization(self):
        """Test that Config initializes and reads config correctly."""
        config = Config()
        assert config.config is not None
        assert isinstance(config.config, dict)

    def test_name_property(self):
        """Test that the name property returns the correct project name."""
        config = Config()
        assert config.name == "spark-optimisation"

    def test_version_property(self):
        """Test that the version property returns the correct version."""
        config = Config()
        assert config.version == "0.1.0"

    def test_read_config_with_valid_toml(self):
        """Test read_config method with valid TOML content."""
        # Mock TOML content
        mock_toml_content = """
[project]
name = "test-project"
version = "1.0.0"
description = "Test project"
"""
        mock_config_data = {
            "project": {
                "name": "test-project",
                "version": "1.0.0", 
                "description": "Test project"
            }
        }
        
        with patch("builtins.open", mock_open(read_data=mock_toml_content.encode())):
            with patch("tomllib.load", return_value=mock_config_data):
                config = Config()
                result = config.read_config()
                
                assert result["name"] == "test-project"
                assert result["version"] == "1.0.0"
                assert result["description"] == "Test project"

    def test_read_config_file_not_found(self):
        """Test read_config method when pyproject.toml file is not found."""
        with patch("builtins.open", side_effect=FileNotFoundError("File not found")):
            with pytest.raises(FileNotFoundError):
                Config()

    def test_read_config_invalid_toml(self):
        """Test read_config method with invalid TOML content."""
        with patch("builtins.open", mock_open(read_data=b"invalid toml content")):
            with patch("tomllib.load", side_effect=Exception("Invalid TOML")):
                with pytest.raises(Exception):
                    Config()

    def test_read_config_missing_project_section(self):
        """Test read_config method when TOML is missing project section."""
        mock_config_data = {
            "other_section": {
                "key": "value"
            }
        }
        
        with patch("builtins.open", mock_open()):
            with patch("tomllib.load", return_value=mock_config_data):
                with pytest.raises(KeyError):
                    Config()

    def test_config_properties_with_mocked_data(self):
        """Test that properties work correctly with mocked config data."""
        mock_config_data = {
            "project": {
                "name": "mocked-project",
                "version": "2.0.0"
            }
        }
        
        with patch("builtins.open", mock_open()):
            with patch("tomllib.load", return_value=mock_config_data):
                config = Config()
                assert config.name == "mocked-project"
                assert config.version == "2.0.0"

    def test_config_reads_actual_file(self):
        """Test that Config can read the actual pyproject.toml file."""
        # This test uses the real file system
        config = Config()
        
        # Verify it reads from the actual pyproject.toml
        assert "name" in config.config
        assert "version" in config.config
        assert config.name is not None
        assert config.version is not None

    def test_config_object_attributes(self):
        """Test that Config object has expected attributes."""
        config = Config()
        
        assert hasattr(config, 'config')
        assert hasattr(config, 'name')
        assert hasattr(config, 'version')
        assert hasattr(config, 'read_config')
        
        # Verify that name and version are properties, not methods
        assert isinstance(config.name, str)
        assert isinstance(config.version, str)