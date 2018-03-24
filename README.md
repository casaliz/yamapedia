# yamapedia
ディープラーニングを使って10種類の花画像を分類する。以下のフォルダ構成でterminalから
```
> python check.py test1.png
```
でtest1の種類を推定する。

version
----------------------------------
- Python 3.6.3（Anacondaでインストール）
- tensorflow 1.6.0
- Keras 2.1.5

directory
----------------------------------
```
10types_test/
  ┃
  ┣　train.py
  ┃
  ┣　check.py
  ┃
  ┣　model_structure.json
  ┃
  ┣　model.h5
  ┃
  ┣　test1.png
  ┃
  ┣  test2.png
  ┃
  ┣  test3.png
  ┃
  ┗　10types_images/
      ┣　hakusansyajin
      ┃   ┣　.png
      ┃   ┃    ︙
      ┃   ┗　.png
      ┣　hakusansyakunage
      ┃   ┣　.png
      ┃   ┃    ︙
      ┃   ┗　.png
      ┃        ︙
      ┃        ︙
      ┃        ︙
      ┣　iwametsumekusa
      ┃   ┣　.png
      ┃   ┃    ︙
      ┃   ┗　.png
      ┗ 　iwaougi
          ┣　.png
          ┃    ︙
          ┗　.png

```
  
