.. contents::
    :local:
    :depth: 2
    :backlinks: none

#################################
在 Windows 上安裝 Python 常用套件
#################################

大部份的套件其實可以透過 ``pip install somepackage`` 來完成。

不過一些針對運算作優化的程式，例如 `Numpy`__ 為了加速計算，
常常引入一些加速矩陣計算的套件，有時這些套件的編譯並不是很簡單能完成，
它們可以依賴更多像 Fortran、其他函式庫…，使得安裝這類科學類的套件這件事，
常常成為使用他們的最大障礙。

__ http://www.numpy.org/

加之，多數套件可能都是針對 Unix* 系統開發，Windows 上可能要建立出一個類 Unix 的環境，
也非易事。所以就有一些朋友有把這類套件預先在 Windows 上包裝好，再釋出給其他人安裝，
使用上容易許多。 

http://www.lfd.uci.edu/~gohlke/pythonlibs/ 即是一個非官方的 Windows Python 套件集散地。
以下即使他提供的 Windows 版本來示範。

使用 Python 3.3 on Winows 7 (64bit) 環境作示範。

Visual C++ 2010
===============

照說明，Python 2.7 與 3.3 使用官方安裝檔安裝完畢後，
需要再安裝 Visual C++ 2008/2010 可轉發套件，
並選擇自己的平台（以 64bit 為例），至 `對應連結`__ 下載。

__ http://www.microsoft.com/en-us/download/details.aspx?id=14632

Scipy-stack
===========

`Scipy-stack`__ 算以懶人包的形式，把科學計算、資料分析常用的套件都包在一起安裝。
主要有以下幾個套件：

- numpy-MKL
- scipy
- matplotlib
- ipython
- pandas

網站上 Win XP 可能會有一點問題。
如果安裝失敗，也可以試著將這個懶人包的所有套件，獨立安裝完成，功能上兩者不會有差別。

__ http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy-stack

我們可以隨意測試一些套件的正確性

.. code-block:: powershell

    > ipython3 notebook     # 開啟一個 IPython notebook 並打開瀏覽器
