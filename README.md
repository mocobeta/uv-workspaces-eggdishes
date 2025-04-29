[uv workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/) + [pluggy](https://pluggy.readthedocs.io/en/latest/) のtoy exampleです。

解説記事はこちら: [uv workspacesでスッキリ作るPythonモノレポ (@mocobeta)](https://blog.mocobeta.dev/posts/20250427-entry-monorepo-with-uv-workspaces/)

## セットアップ

```
$ git clone https://github.com/mocobeta/uv-workspaces-eggdishes.git
$ cd uv-workspaces-eggdishes/
$ uv venv

# 動作テスト (プラグインなし)
$ uv sync --package eggdishes-main
$ uv run eggdishes list
Available egg dish recipes:
- fresh

$ uv run eggdishes recipe fresh
Recipe for 採れたて卵:
ご飯に新鮮な卵とかつお節をのせて、醤油をかけて召し上がれ！

$ uv run eggdishes recipe spam
No recipe found for spam.
```

## ビルドと動作テスト（プラグインあり）

```
$ uv build --all-packages
...
Successfully built dist/eggdishes_boiled-0.2.0.tar.gz
Successfully built dist/eggdishes_boiled-0.2.0-py2.py3-none-any.whl
Successfully built dist/eggdishes_core-0.2.0.tar.gz
Successfully built dist/eggdishes_core-0.2.0-py2.py3-none-any.whl
...
```

適当なディレクトリに環境を作り，ビルドしたすべてのパッケージをインストールする

```
$ mkdir -p ~/temp/eggdishes-test
$ cd ~/temp/eggdishes-test
$ python -m venv .venv
$ . .venv/bin/activate
$ pip install <path-to-eggdishes-repo>/dist/*.whl

$ eggdishes list
Available egg dish recipes:
- fresh
- sunnysideup
- poached
- boiled
- scrambled

$ eggdishes recipe sunnysideup
Recipe for Sunny Side Up Egg:

1. フライパンを温める
    中火でフライパンを軽く温め、油かバターを入れて広げます。
2. 卵をそっと割り入れる
    黄身が割れないように優しく！できれば小さい器に一度割ってからフライパンへ流し込むと安心。
3. 弱火にして水を加える
    卵の白身が広がったら、すぐに火を弱火にしてフライパンの端から水を加えます。
4. すぐふたをする
    加えた水が蒸気になって卵を包み込みます。ふたをして、約1〜2分蒸し焼きに。
5. 様子を見ながら火を止める
    白身が固まって、黄身がまだぷるんぷるんしていたらOK！
    早めに火を止めて余熱で少しだけ火を通すと、絶妙な半熟に仕上がります。
6. 塩・こしょうで味付けする
完成！
```