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
# Upgrade the installed seetapsych-configs package to the latest available version
# For plain pip: pip install --upgrade seetapsych-configs
uv pip install --upgrade seetapsych-configs
# Re-download the latest module definitions
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

## Distributed Configs

| Name | Version | Packages | Config | Source |
|---|---|---|---|---|
| SelectFace | 1.0 | <ul><li>SelectFace: `face/selection`, `face/detection`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-lib/main/seetapsych_lib/modules/face_selection.yml) | [repo](https://github.com/seetapsych/seetapsych-lib) |
| InsightFace's RetinaFace | 1.0 | <ul><li>FaceDetection-RetinaFace(InsightFace): `face/detection`, `face/landmarks`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-face-hub/main/seetapsych_face_hub/modules/insightface/retinaface.yml) | [repo](https://github.com/seetapsych/seetapsych-face-hub) |
| InsightFace's ArcFace | 1.0 | <ul><li>FaceFeature-ArcFace(InsightFace): `face/feature`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-face-hub/main/seetapsych_face_hub/modules/insightface/arcface.yml) | [repo](https://github.com/seetapsych/seetapsych-face-hub) |
| MediaPipe Face Detection & Face Mesh | 1.0 | <ul><li>FaceDetection-MediaPipe: `face/detection`</li><li>FaceMesh-MediaPipe: `face/mesh`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-face-hub/main/seetapsych_face_hub/modules/mediapipe.yml) | [repo](https://github.com/seetapsych/seetapsych-face-hub) |
| RetinaFace (PyTorch) | 1.0 | <ul><li>FaceDetection-RetinaFace(PyTorch): `face/detection`, `face/landmarks`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-face-hub/main/seetapsych_face_hub/modules/retinaface.yml) | [repo](https://github.com/seetapsych/seetapsych-face-hub) |
| SeetaDenseLandmarks | 1.0 | <ul><li>DenseLandmarks[280]-Seeta: `face/dense_landmarks`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-face-ex/main/seetapsych_face_ex/modules/dense_landmarks.yml) | [repo](https://github.com/seetapsych/seetapsych-face-ex) |
| Emotions (SeetaEmoNet) | 1.0 | <ul><li>Emotions-SeetaEmoNet: `face/action_units`, `face/expression`, `face/dimensional_affect`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-emo/main/seetapsych_emo/modules/emonet.yml) | [repo](https://github.com/seetapsych/seetapsych-emo) |
| AdaChrom | 1.0 | <ul><li>HeartRate-AdaChrom: `face/heart_rate`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-hertz/main/seetapsych_hertz/modules/ada-chrom.yml) | [repo](https://github.com/seetapsych/seetapsych-hertz) |
| SeetaHeartRateDetector | 1.0 | <ul><li>HeartRate-Seeta: `face/heart_rate`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-hertz/main/seetapsych_hertz/modules/seeta.yml) | [repo](https://github.com/seetapsych/seetapsych-hertz) |
| TinyHR | 1.0 | <ul><li>HeartRate-TinyHR: `face/heart_rate`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-hertz/main/seetapsych_hertz/modules/tiny-hr.yml) | [repo](https://github.com/seetapsych/seetapsych-hertz) |
| OpenGaze-AFFNet | 1.0 | <ul><li>GazeScreen-AFFNet(OpenGaze): `face/gaze_screen`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-gaze/main/seetapsych_gaze_screen/modules/affnet.yml) | [repo](https://github.com/seetapsych/seetapsych-gaze) |
| OpenGaze-ITrackerPlus | 1.0 | <ul><li>GazeScreen-ITrackerPlus(OpenGaze): `face/gaze_screen`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-gaze/main/seetapsych_gaze_screen/modules/itracker-plus.yml) | [repo](https://github.com/seetapsych/seetapsych-gaze) |
| OpenGaze-TdGazeNet | 1.0 | <ul><li>GazeScreen-TDGazeNet(OpenGaze): `face/gaze_screen`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-gaze/main/seetapsych_gaze_screen/modules/tdgazenet.yml) | [repo](https://github.com/seetapsych/seetapsych-gaze) |
| HeadDetection & HeadSelection (CoSI Gaze Follow) | 1.0 | <ul><li>HeadDetection-CoSIGaze: `head/detection`</li><li>HeadSelection: `head/selection`, `head/detection`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-gaze-follow/main/seetapsych_gaze_follow/modules/head_detection.yml) | [repo](https://github.com/seetapsych/seetapsych-gaze-follow) |
| Gaze Follow (CoSI Transformer) | 1.0 | <ul><li>SceneGazeFollow-CoSIGaze: `head/gaze_point`</li><li>SocialGaze-CoSIGaze: `head/social_gaze`</li></ul> | [raw](https://raw.githubusercontent.com/seetapsych/seetapsych-gaze-follow/main/seetapsych_gaze_follow/modules/cosi.yml) | [repo](https://github.com/seetapsych/seetapsych-gaze-follow) |
