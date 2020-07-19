# Flask tutorial

## 開発環境の構築

- [開発環境の設定](./docs/dev.md)

## How to run test code

```bash
python test_flask_blog.py
```

## Run test via coverage

```bash
coverage run -m unittest
```

## test coverage の計測

```bash
coverage report -m
```

- Atrributes

| attribute | body                                    |
| --------- | --------------------------------------- |
| name      | test 対象の file                        |
| Stmts     | file における test 対象となる code 行数 |
| Miss      | Test されていない code 行数             |
| Cover     | Test coverage                           |

## Appendix

- [blueprint](./docs/blueprint.md)
- [flask 0.11 対応](docs/flask_0_1_1.md)
- [flask 1.0 対応](docs/flask_1_0.md)

## Link

- [github](https://github.com/chaingng)
