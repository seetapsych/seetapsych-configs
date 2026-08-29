# SeetaPsych Configs

Official recommended configuration files for SeetaPsych.

For the full list of distributed configs with download links and homepages, see [CONFIGS.md](CONFIGS.md).

## Install via Manager

After installing `seetapsych-lib`, use the manager CLI to download and install all configs from this package:

```sh
seetapsych-manager download
```

This copies the configuration files into the active config directory so `seetapsych-lib` can discover and load the modules.

Use `-f` / `--force` to overwrite any existing installed configs:

```sh
seetapsych-manager download -f
```

## Update Configs

To pull in the latest module definitions, first upgrade the package itself, then re-download the configs:

```sh
uv pip compile --upgrade-package seetapsych-configs
seetapsych-manager download -f
```

If you are using pip instead of uv:

```sh
pip install --upgrade seetapsych-configs
seetapsych-manager download -f
```

## Dependencies

Downloading the configuration files with `seetapsych-manager download` does **not** automatically install the runtime dependencies (Python libraries) required by every module.

There are two ways to install dependencies:

- **Install dependencies for all modules at once** — run the manager's `setup` command:

  ```sh
  seetapsych-manager setup
  ```

- **Install on demand per workflow** — when building a pipeline programmatically, call `install_requirements()` to resolve only the packages needed for that specific run:

  ```python
  pipeline.solve()
  pipeline.install_requirements()
  ```

The WebUI also triggers on-demand dependency installation automatically when a module is first used.
