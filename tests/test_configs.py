import os
from typing import Any

import pytest
import yaml

from seetapsych_configs import ConfigInfo, __version__, configs


def _raw_configs_path() -> str:
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "seetapsych_configs",
        "configs.yml",
    )


def _load_raw_configs() -> list[dict[str, Any]]:
    with open(_raw_configs_path(), encoding="utf-8") as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict)
    raw = data.get("configs", [])
    assert isinstance(raw, list)
    return raw


class TestModuleBasics:
    def test_version_is_string(self) -> None:
        assert isinstance(__version__, str)
        assert len(__version__) > 0

    def test_configs_is_list_of_configinfo(self) -> None:
        assert isinstance(configs, list)
        for cfg in configs:
            assert isinstance(cfg, dict)
            assert set(ConfigInfo.__required_keys__).issubset(cfg.keys())


class TestConfigsContent:
    @pytest.mark.parametrize("cfg", configs, ids=lambda c: c.get("name", "?"))
    def test_each_config_required_fields_non_empty(self, cfg: ConfigInfo) -> None:
        assert cfg["name"], "name must be non-empty"
        assert cfg["version"], "version must be non-empty"
        assert cfg["description"], "description must be non-empty"
        assert cfg["download_url"], "download_url must be non-empty"

    @pytest.mark.parametrize("cfg", configs, ids=lambda c: c.get("name", "?"))
    def test_download_url_is_https(self, cfg: ConfigInfo) -> None:
        assert cfg["download_url"].startswith("https://"), f"{cfg['name']}: download_url must be HTTPS"

    @pytest.mark.parametrize("cfg", configs, ids=lambda c: c.get("name", "?"))
    def test_download_url_looks_like_raw_yml(self, cfg: ConfigInfo) -> None:
        url = cfg["download_url"]
        assert url.endswith(".yml") or url.endswith(".yaml"), (
            f"{cfg['name']}: download_url should point to a .yml/.yaml file"
        )

    def test_no_duplicate_config_names(self) -> None:
        names = [c["name"] for c in configs]
        assert len(names) == len(set(names)), "Config names must be unique"

    def test_config_count_matches_raw_yaml(self) -> None:
        raw = _load_raw_configs()
        assert len(configs) == len(raw), "Package configs count must match raw YAML entry count"

    def test_all_raw_entries_exported(self) -> None:
        raw = _load_raw_configs()
        raw_names = {r["name"] for r in raw}
        exported_names = {c["name"] for c in configs}
        assert exported_names == raw_names
