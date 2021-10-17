# python-package-template

インストール
```sh
$ pip install .
```

開発用に編集モードでインストール
```sh
$ pip install -e .
```

アンインストール
```sh
$ pip uninstall mypackage
```

実行
```sh
$ mypackage
```

インポート
```sh
import mypackage
```

## toxを利用した自動テスト

1. pyenvを用いてPython 3.7, 3.8, 3.9をインストール
1. リポジトリのディレクトリに`.python-version`を作成し，pyenvで利用可能なPythonバージョンを記載する
    ```sh
    $ vi .python-version
    3.9.6
    3.8.11
    3.7.11
    ```
1. toxをインストール
    ```sh
    $ pip install tox
    ```
1. Python 3.7, 3.8, 3.9のそれぞれでリントとテストを実行し，コードに問題がないことを確認する
    - 以前の結果に引きづられてテストが失敗する場合は`--recreate (-r)`オプションで解決できます
    - `.tox/`以下にxml形式のテストレポートを出力します
    ```sh
    $ tox -e py37-lint,py38-lint,py39-lint  # black, isort, flake8, pylint, mypy, banditが実行されます
    $ tox -e py37-test,py38-test,py39-test  # pytest, pytest-covが実行されます
    ```

## pre-commitを利用したコミット前自動チェック

`git commit`時にフォーマットチェックを実行する
```sh
$ pip install pre-commit
$ pre-commit install  # .git/hooks/pre-commitを設定する
$ pre-commit autoupdate  # .pre-commit-config.yamlのパッケージバージョンを最新にする
```
