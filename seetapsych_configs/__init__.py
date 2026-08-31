import os
from typing import TypedDict

import yaml

__all__ = [
    "ConfigPackageInfo",
    "ConfigInfo",
    "configs",
]


class ConfigPackageInfo(TypedDict):
    name: str
    provides: list[str]


class ConfigInfoRequired(TypedDict):
    name: str
    version: str
    description: str
    download_url: str
    homepage: str


class ConfigInfo(ConfigInfoRequired, total=False):
    packages: list[ConfigPackageInfo]
    disabled: bool


def _load_configs() -> list[ConfigInfo]:
    yml_path = os.path.join(os.path.dirname(__file__), "configs.yml")
    with open(yml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    raw_list = data.get("configs", []) if isinstance(data, dict) else []
    result: list[ConfigInfo] = []
    for item in raw_list:
        entry: ConfigInfo = ConfigInfo(
            name=str(item["name"]),
            version=str(item["version"]),
            description=str(item["description"]),
            download_url=str(item["download_url"]),
            homepage=str(item.get("homepage", "")),
        )
        raw_packages = item.get("packages")
        if isinstance(raw_packages, list):
            packages: list[ConfigPackageInfo] = []
            for raw_pkg in raw_packages:
                if not isinstance(raw_pkg, dict):
                    continue
                pkg_name = str(raw_pkg.get("name", ""))
                raw_provides = raw_pkg.get("provides", [])
                provides = [str(x) for x in raw_provides] if isinstance(raw_provides, list) else []
                if not pkg_name:
                    continue
                packages.append(ConfigPackageInfo(name=pkg_name, provides=provides))
            if packages:
                entry["packages"] = packages
        raw_disabled = item.get("disabled")
        if isinstance(raw_disabled, bool):
            entry["disabled"] = raw_disabled
        result.append(entry)
    return result


configs: list[ConfigInfo] = _load_configs()


def _load_version() -> str | None:
    try:
        from ._version import __version__  # type: ignore[import-not-found]

        return __version__.strip() or None
    except Exception:
        return None


__version__ = _load_version() or "0.0.0.dev0"
