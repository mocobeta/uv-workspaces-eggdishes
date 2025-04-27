[uv workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/) のtoy exampleです。

```
# 環境セットアップ
$ git clone https://github.com/mocobeta/uv-workspaces-eggdishes.git
$ cd uv-workspaces-eggdishes/
$ uv venv
$ uv sync --package eggdishes-main

# 動作テスト
$ uv run eggdishes --help
Usage: eggdishes [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  recipe  Show the recipe for an egg dish.

$ uv run eggdishes recipe --help
Usage: eggdishes recipe [OPTIONS]
                        [[boiled|poached|scrambled|sunnysideup|fresh]]

  Show the recipe for an egg dish.

Options:
  --help  Show this message and exit.

$ uv run eggdishes recipe boiled
Recipe for Boiled Egg:

1. 卵を常温に戻す
    冷蔵庫から出したばかりの卵はヒビが入りやすいので、10〜20分ほど室温に置きます。
2. 鍋に卵を並べる
    卵同士がぶつからないように注意しながら鍋に並べます。
3. 水を入れる
    卵がしっかり浸るくらいまで水を注ぎます。
4. 火にかける
    中火で加熱し、沸騰させます。
5. 茹で時間を調整する
    沸騰したらタイマーをセット！お好みの仕上がりに合わせて茹で時間を変えます。
    - 半熟（とろとろ）：6〜7分
    - 半熟（ねっとり）：8〜9分
    - 固ゆで（しっかり）：10〜12分
6. 冷水にとる
    茹で上がったらすぐに冷水（または氷水）に移して冷やします。殻がむきやすくなります。
完成！

$ uv run eggdishes recipe sunnysideup
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
