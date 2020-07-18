# Blueprint

## 使い方

- application の中に複数の機能があるとき、その機能を小さな application として独立されて構成することができる。
  - 例えば、今回の blog application の中に command 機能を追加して、command 機能についてもそれぞれ view や template, static file があるときに、その部分を分割りして構成することができる
  - このように、view, template, static file をまとめて独立した application にすることを、公式では divisional な構造化と呼んでいます。

- template や static file は共通で使っている場合に、view 飲みを分ける方法
  - 今回の blog application では、template や static file は全て共通で使っています。その中で entries に関する機能が存在しますので、これを functional な構造として分割してみます。

----------

## この application に対して

以下の file 中で url_for で entries view を参照していた部分を、url_for('entry.xxx') の形に変更します。

- templates/layout.html
- templates/entries/edit.html
- templates/entries/index.html
- templates/entries/new.html
- templates/entries/show.html
- views/views.py
