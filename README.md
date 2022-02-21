# Python-20220216--Adrian-Diaz-Garcia

<div align="center">

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)]((https://github.com/GregAiven/Python-20220216--Adrian-Diaz-Garcia/))
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Python-20220216--Adrian-Diaz-Garcia

</div>

## ⚙ Features

### Development features

- Supports for `Python 3.9` and higher.
- [`Pip`](https://pypi.org/project/pip/) as the dependencies manager, requirements can be found in requirements.txt file.
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort).
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).

### Open source community features

- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).


## 🚀 Quick start

> Note: to see more details to execute tests, linting and other extras, see `Makefile usage` section

In order to build and execute the example main program (a.k.a. start monitor some websites defined in settings.py inside the monitor package ):

```
make build
make up
```

### How to configure regex and websites

Edit file in [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort).

> Requirements: you must have docker installed and running
> 
## 🖖Makefile usage

[`Makefile`](https://github.com/GregAiven/Python-20220216--Adrian-Diaz-Garcia/blob/master/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Building local images</summary>
<p>

```bash
make build
```

</p>
</details>

<details>
<summary>2. Tests</summary>
<p>

Running tests inside docker containers using pytest:

```bash
make test
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `isort` and `black`.

```bash
make black isort
```

Codestyle rewrite files and format them:


> Note: `check-codestyle` uses `isort`, `black` library
</details>

<details>
<summary>4. Linters</summary>
<p>

Current used linter is flake8

```bash
make flake8
```
</details>

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |



## 🛡 License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/GregAiven/Python-20220216--Adrian-Diaz-Garcia/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{Python-20220216--Adrian-Diaz-Garcia,
  author = {Adrian Diaz},
  title = {Python-20220216--Adrian-Diaz-Garcia},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/GregAiven/Python-20220216--Adrian-Diaz-Garcia}}
}
```