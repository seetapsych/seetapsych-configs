# SeetaPsych Configs

> SeetaPsych 官方推荐配置文件集合。

简体中文 | [English](README.md)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](pyproject.toml)
[![License](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](LICENSE)

随包分发的完整配置清单（含下载链接与项目主页）见 [CONFIGS.md](CONFIGS.md)。

## 通过管理器安装

安装 `seetapsych-lib` 后，使用管理器 CLI 即可下载并安装本包的全部配置：

```sh
seetapsych-manager download
```

该命令会将配置文件复制到当前激活的配置目录，以便 `seetapsych-lib` 发现并加载模块。

使用 `-f` / `--force` 可覆盖任何已安装的现有配置：

```sh
seetapsych-manager download -f
```

## 更新配置

若要拉取最新的模块定义，请先升级本包自身，再重新下载配置：

```sh
# 将已安装的 seetapsych-configs 升级至最新可用版本
# 使用纯 pip 时：pip install --upgrade seetapsych-configs
uv pip install --upgrade seetapsych-configs
# 重新下载最新的模块定义
seetapsych-manager download -f
```

## 依赖

通过 `seetapsych-manager download` 下载配置文件**不会**自动安装每个模块所需的运行时依赖（Python 库）。

有两种安装依赖的方式：

- **一次性安装全部模块依赖** — 运行管理器的 `setup` 命令：

  ```sh
  seetapsych-manager setup
  ```

- **按工作流按需安装** — 以编程方式构建流水线时，调用 `install_requirements()` 仅解析该次运行所需的包：

  ```python
  pipeline.solve()
  pipeline.install_requirements()
  ```

WebUI 同样会在首次使用某个模块时自动触发按需依赖安装。

随包分发的模块配置目录见 [CONFIGS.md](CONFIGS.md)。
