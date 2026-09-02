import os
import sys
from datetime import datetime

from seetapsych_configs import ConfigInfo, configs

TEMPLATE_NAME = "template_doc_configs.md"
OUTPUT_NAME = "CONFIGS.md"

SLOT_TABLE = "{{CONFIGS_TABLE}}"
SLOT_COUNT = "{{CONFIGS_COUNT}}"
SLOT_GENERATED_AT = "{{GENERATED_AT}}"


def _escape_md(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def _format_attributes(provides: list[str]) -> str:
    if not provides:
        return ""
    return "<br>".join(f"&nbsp;&nbsp;`{p}`" for p in provides)


def _packages_cell(cfg: ConfigInfo) -> str:
    packages = cfg.get("packages") or []
    if not packages:
        return "—"
    items: list[str] = []
    for pkg in packages:
        segments = pkg["name"].split("-")
        joined = "**<br>**-".join(segments)
        name_md = f"**{joined}**"
        attrs = _format_attributes(pkg.get("provides", []))
        suffix = f"<br>{attrs}" if attrs else ""
        items.append(f"{name_md}:{suffix}")
    return "<br>".join(items)


def _homepage_cell(cfg: ConfigInfo) -> str:
    return f"[Homepage]({cfg['homepage']})" if cfg["homepage"] else "-"


def _download_cell(cfg: ConfigInfo) -> str:
    return f"[Download]({cfg['download_url']})"


def render_table(cfgs: list[ConfigInfo]) -> str:
    active = [c for c in cfgs if not c.get("disabled", False)]
    disabled = [c for c in cfgs if c.get("disabled", False)]

    lines: list[str] = [
        "| Name | Version | Description | Packages | Download | Homepage |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for cfg in active:
        lines.append(
            "| {name} | {version} | {desc} | {pkgs} | {dl} | {hp} |".format(
                name=_escape_md(cfg["name"]),
                version=_escape_md(cfg["version"]),
                desc=_escape_md(cfg["description"]),
                pkgs=_packages_cell(cfg),
                dl=_download_cell(cfg),
                hp=_homepage_cell(cfg),
            )
        )
    if not disabled:
        return "\n".join(lines)

    lines.append("")
    lines.append(
        f"> **Deprecated configs ({len(disabled)}):** "
        "reserved for historical reference; download is skipped by default."
    )
    lines.append("")
    lines.append("| Name | Version | Description | Packages | Download | Homepage |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for cfg in disabled:
        lines.append(
            "| {name} | {version} | {desc} | {pkgs} | {dl} | {hp} |".format(
                name=f"~~{_escape_md(cfg['name'])}~~",
                version=f"~~{_escape_md(cfg['version'])}~~",
                desc=f"~~{_escape_md(cfg['description'])}~~",
                pkgs=f"~~{_packages_cell(cfg)}~~",
                dl=_download_cell(cfg),
                hp=_homepage_cell(cfg),
            )
        )
    return "\n".join(lines)


def load_template(scripts_dir: str) -> str:
    tpl_path = os.path.join(scripts_dir, TEMPLATE_NAME)
    with open(tpl_path, encoding="utf-8") as f:
        return f.read()


def render_md(cfgs: list[ConfigInfo], template: str) -> str:
    return (
        template.replace(SLOT_TABLE, render_table(cfgs))
        .replace(SLOT_COUNT, str(len(cfgs)))
        .replace(SLOT_GENERATED_AT, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )


def main() -> int:
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(scripts_dir)

    template = load_template(scripts_dir)
    content = render_md(configs, template)

    output_path = os.path.join(project_root, OUTPUT_NAME)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    rel = os.path.relpath(output_path, os.getcwd())
    total_pkgs = sum(len(c.get("packages") or []) for c in configs)
    print(f"Wrote {len(configs)} config entries ({total_pkgs} packages total) -> {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
