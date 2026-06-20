# Introduction

StreamViewer is a Python package for real-time data visualization. It comprises data-source and visualization modules, as well as some useful widgets to connect and configure those modules. It is intended for integration into applications for real-time monitoring and visualization of streaming data, especially data from [lab streaming layer (LSL)](https://labstreaminglayer.readthedocs.io/index.html) streams.

Additionally, StreamViewer comes with several pre-made applications, including a well-featured GUI for monitoring LSL streams and visualizing data.

![LSLViewer Main gif](img/stream_viewer-main.gif)

## Getting Started

### Installation

This project uses `uv` as the default installation and environment manager.

Install `uv`:

- macOS and Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

Then install the pinned project Python version and sync the environment:

```bash
uv python install
uv sync --locked
```

`uv` manages the Python version for this project using [.python-version](</mnt/c/Users/Zachs/Desktop/Sage/2_support/Temple/stream_viewer/.python-version:1>), which is currently pinned to Python `3.12`.

### Platform runtime dependencies

`uv` installs the Python dependencies for StreamViewer, but some platforms also require native runtime libraries.

On Linux, Qt/OpenGL support may require additional system packages. If startup fails with an error like `libEGL.so.1: cannot open shared object file`, install:

```bash
sudo apt-get update
sudo apt-get install -y libegl1
```

StreamViewer also depends on `liblsl` in addition to the Python `pylsl` package.

- Ubuntu 24.04 CI currently uses `liblsl` `v1.17.7`: `liblsl-1.17.7-noble_amd64.deb`
- macOS CI currently uses `liblsl-1.17-Darwin-universal.pkg`
- Windows CI currently uses `liblsl-1.17.7-Win_amd64.zip`

If `pylsl` cannot find `liblsl`, refer to the upstream `pylsl` and `liblsl` installation guidance.

### Running the provided applications

Run the main application with:

```bash
uv run python -m stream_viewer.applications.main
```

Applications in the `applications` module can be run with:

```bash
uv run python -m stream_viewer.applications.{application_name}
```

Additionally, several console entry points are installed into the project environment:

* `lsl_viewer`
* `lsl_status`
* `lsl_switching`
* `lsl_viewer_custom`

You can run those with `uv run`, for example:

```bash
uv run lsl_viewer
```

`lsl_viewer` and `lsl_switching_viewer` make use of an `.ini` file. The default ini file is expected at `~/.stream_viewer/{application_name}.ini`, but the path can also be provided as a command-line argument.

`lsl_viewer_custom` also makes use of command-line arguments to specify stream predicates and renderer name.

## Documentation

Start at the [outline/overview](outline/overview.md).

## Acknowledgments

StreamViewer is developed by [Intheon](https://intheon.io) and was funded in part by the Army Research Laboratory under Cooperative Agreement Number W911NF-10-2-0022 as part of the [Lab Streaming Layer project](https://github.com/sccn/labstreaminglayer/).
