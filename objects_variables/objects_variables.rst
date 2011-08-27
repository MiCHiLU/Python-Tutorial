オブジェクトと変数
------------------

ここで、ローカルの名前空間を空にするため、Pythonを再起動します。

.. include:: objects_variables_a.code

Pythonではすべてがオブジェクトであり、次の項目を持っています:

- 単一のID（メモリアドレス）
- 単一の値
- いくつかの属性
- 単一の型
- ひとつ、またはいくつかの名前（ひとつ以上の名前空間）
- ひとつ以上の基底クラス

.. include:: objects_variables_b.code

演習:

ローカルの名前空間を空にするため、Pythonを再起動します。

.. include:: objects_variables_c.code

辞書オブジェクト
----------------

.. include:: objects_variables_d.code

演習:

.. include:: objects_variables_e.code

ブロック、forループ
-------------------

.. include:: objects_variables_f.code

演習:

.. include:: objects_variables_g.code

高度な演習:

.. include:: objects_variables_h.code

イテレータ式、ジェネレータ式
----------------------------

- forループでは、反復可能オブジェクトを扱います。
- `iter()` 関数は、イテレータを生成します。
- StopIteration例外が送出されるまで、イテレータオブジェクトの `next()` メソッドが繰り返し呼び出されます。
- iter(foo) は、

    - `foo.__iter__()` が存在する場合、それが呼び出されます。
    - `foo.__getitem__` が存在する場合、ゼロからインデキシングし、
      `IndexError` 例外を補足して `StopIteration` 例外を送出します。

.. - Note: iter(callable, sentinel) behaves differently.

.. include:: objects_variables_i.code

演習:

.. include:: objects_variables_j.code
