import os
from typing import TypedDict

import yaml

__all__ = [
    "ConfigInfo",
    "configs",
]


class ConfigInfo(TypedDict):
    name: str
    version: str
    description: str
    download_url: str
    homepage: str


def _load_configs() -> list[ConfigInfo]:
    yml_path = os.path.join(os.path.dirname(__file__), "configs.yml")
    with open(yml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    raw_list = data.get("configs", []) if isinstance(data, dict) else []
    result: list[ConfigInfo] = []
    for item in raw_list:
        result.append(
            ConfigInfo(
                name=item["name"],
                version=item["version"],
                description=item["description"],
                download_url=item["download_url"],
                homepage=item.get("homepage", ""),
            )
        )
    return result


configs: list[ConfigInfo] = _load_configs()


def _load_version() -> str | None:
    try:
        from ._version import __version__  # type: ignore[import-not-found]

        return __version__.strip() or None
    except Exception:
        return None


__version__ = _load_version() or "0.0.0.dev0"
