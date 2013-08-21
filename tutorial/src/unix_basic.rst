.. contents::
    :local:
    :depth: 2
    :backlinks: none


#############
Unix 基本操作
#############

主要參考 `鳥哥的 Linux 私房菜`__ 的基礎教學流程。

希望大家之後能自己行完成：

- 第一部份：計算機概論、Linux 是什麼（第零、一章）
- 第二部份：全（第六、七、八、九章）
- 第三部份：重要，但非必要（第十、十一、十二、十三章）

__ http://linux.vbird.org/linux_basic/

----

########
第一部份
########

第零章、計算機概論
==================

有什麼看不懂的嗎 XD


第一章、Linux 是什麼
====================

當故事看吧

----

########
第二部份
########

第六章、Linux檔案權限與目錄配置
===============================

觀念蠻重要的，但可以先不要學怎麼給不同檔案正確的權限。

目標
----

- 看得懂 ``ls -alF`` 每行分別代表檔案、連結、資料夾
- 以及每個檔案 User, Group, Others 的權限各有 ``r/w/x`` 哪些


第七章、Linux 檔案與目錄管理
============================

重要指令
--------

.. code-block:: bash

    $ <any command> [--help|-h]

    $ cd .
    $ cd ..

    $ pwd
    $ ls [-altF]

    $ mkdir [-p]

    $ cp [-urf] 
    $ mv

    $ rm [-rf]      # 注意要知道自己在做什麼！


**查看檔案內容**

.. code-block:: bash

    $ cat
    $ head [-n x]
    $ tail [-n x]

    $ less
    $ more

    $ touch

**搜尋**

.. code-block:: bash

    $ which

    $ locate
    $ find <path> -name xxx

目標
----

- 相對 / 絕對路徑的意思，如何得到每個目錄的絕對路徑
- 自由地在 Server 上切換路徑，而且 **不需要用視窗的檔案總管**
- 知道自己在哪裡
- 列出某一目錄底下的檔案、滿足某個 pattern 的檔案 (ex. ``*.zip``, ``Sample_*``, ...)
- 照時間排序列出檔案

- 建立資料夾
- 移動、複製檔案與資料夾
- 檔案/資料夾更名
- 刪除檔案

- 查看檔案內容，大檔案時只查看部份內容


第八章、Linux 磁碟與檔案系統管理
================================

重要指令
--------

.. code-block:: bash

    $ du -sh ./*
    $ df -h

目標
----

- 當前目錄下每個檔案/資料夾的大小
- 各硬碟掛載位置，剩餘容量


第九章、檔案與檔案系統的壓縮與打包
==================================

.. code-block:: bash

    $ tar zxvf *.tar.gz
    $ tar zcvf newzipped.tar.gz <your files and dirs>

    $ tar jxvf *.tar.bz

    $ gzip
    $ gunzip

目標
----

- 檔案的(解)壓縮

----

########
第三部份
########

第十章、vim 程式編輯器
======================

這章主要在學 Vim 的操作。基本上 Server 已經把 Vim 的環境設定好了，所以設定的部份可以跳過。

主要要學習的 Vim 各種模式的使用，這可能要花點時間，但建議盡量適應，以後在伺服器上開發才不需要多開一個圖形介面。

Server 上 Vim 使用
------------------

因為 Server 上的 Vim 已經安裝好許多外掛，使用上會更為方便：

**Normal Mode**

==============   ===============================
     指令                    說明
==============   ===============================
  ``Ctrl+b``     檔案總管 (NERDTree)
  ``Tab``        程式源碼的結構 (Tagbar)
  ``U + m``      最近使用過的檔案與目錄 (Unite)
  ``U + k``      所有設定的指令與快速鍵 (Unite)
  ``,pp``        paste mode
  ``,ss``        拼字檢查 
 ``,<Enter>``    清除搜尋
==============   =============================== 


**Insert Mode**

==============   ===============================
     指令                    說明
==============   ===============================
 ``Ctrl+f``      源碼補完
==============   =============================== 


.. code-block:: bash

    $ vimtutor


第十一章、認識與學習 BASH 
=========================

用到的時候再來仔細看這章的內容。

現在應該先以了解何謂 `pipeline`__

__ http://linux.vbird.org/linux_basic/0320bash.php#pipe

.. code-block:: bash

    $ wc -l  sometxtfile                    # 計算總行數
    $ head -n xxx txtfile > txtfile.part    # 只取用部份檔案

    $ run commandA && run commandB          # 連續執行兩個程式

    $ ... > ...
    $ ... >> ...
    $ ... | ... | ...

目標
----

- 了解 BASH pipeline 的使用


第十二章、正規表示法與文件格式化處理
====================================

知道有這樣的東西，我們先學 `Python 的正規表示套件`__

__ http://docs.python.org/3/library/re.html


####
補充
####

Screen 使用
===========

未進入 screen 之前
------------------

.. code-block:: bash

    $ screen -ls            # 查看現在有開啟多少個 screen
    $ screen -t MyTitle     # 建立一個名為 MyTitle 的 screen
    $ screen -R             # 只有一個 Detached screen 自動連接，不然建立新的
    $ screen -r <pid...>    # 連接其中一個 detached screen
    $ screen -x <pid...>    # 強迫連至一個　Attached screen


進入 screen 之後
----------------

所有的動作都是以 ``Ctrl+a`` 開始，關閉一個 terminal 一樣使用 ``exit`` 或 ``Ctrl+D``

======  ======
 指令    功能
======  ======
 ``c``   增加一個新的 terminal
 ``d``   detach 當前的 screen
 ``"``   查看現在的 screen 所有的 terminal 並切換
 ``[``   加上下、 ``Ctrl+U/F`` 可以瀏覽先前 terminal 的內容 
 ``a``   切換至最近開啟的一個 terminal
======  ======
