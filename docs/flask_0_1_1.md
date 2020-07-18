# ver 0.11 対応: Flask command line を扱えるようにする

## flask command line を扱う merit

- flask command を使うことで application が起動できるようになりましたので、server.py を使わず application 起動するのが可能になった。
- その他にも、flask command を使用する前提での library (Flask-migrate)なども扱えるようになります。
- 今回は、まずは flask command を扱えるようにして、server.py がなくても application を起動できるようにしてみます。

### この proj では

#### FLASK_APP

- FLASK_APP 環境変数を指定するだけで application の起動が可能になります。

```bash
export FLASK_APP=flask_blog
```

- それでは、application を起動してみます。
  - 以下のコマンドで application を起動する

```bash
flask run
```

#### FLASK_ENV

- develop mode に設定

```bash
export FLASK_ENV=development
```
