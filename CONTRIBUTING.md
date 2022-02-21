# How to contribute

## Dependencies

We use `pip` to manage the dependencies.
Also the project is fully containerized, to operate it there is a make command to facilitate it.

```bash
make build
```

## Codestyle

After the installation you may execute code formatting and linting .

```bash
make black isort flake8
```

### Before submitting

Before submitting your code please do the following steps:

1. Add any changes you want
1. Add tests for the new changes
1. Edit documentation if you have changed something significant
1. Run `make black isort` to format your changes.
1. Run `make flake8` to proper code linting.

## Other help

You can contribute by spreading a word about this project.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.