---
kind: reprint
---

###  SQL Server 2019 Standard 繁體中文標準版安裝

SQL Server 軟硬體需求
https://docs.microsoft.com/zh-tw/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server?view=sql-server-ver15

SQL Server 2019 Standard/Enterprise 至少需要 1GB RAM
(加上 MS-Windows 本身，建議至少 4GB )

SQL Server 2019 (15.x) 需要 .NET Framework 4.6.2。
https://www.microsoft.com/download/details.aspx?id=53344

Windows Server 2019 Datacenter
Windows Server 2019 Standard 
Windows Server 2019 Essentials 
Windows Server 2016 Datacenter 
Windows Server 2016 Standard 
Windows Server 2016 Essentials
(似乎不支援 Windows 10，Windows 8.1 和 Windows 10似乎只能裝些 Client 端程式，x86 能安裝的更少)

以下在 Windows Server 2019 繁體中文標準版上安裝 SQL Server 2019 Standard 繁體中文標準版。(兩者目前都只有 x64 版)

[![img](https://1.bp.blogspot.com/-XX-BJ9yqVpg/XcI1Z5U1fvI/AAAAAAAA1jc/FfdXAVZ09C8yszjGgWSU13mHVnJXql3VQCLcBGAsYHQ/s1600/001.png)](https://1.bp.blogspot.com/-XX-BJ9yqVpg/XcI1Z5U1fvI/AAAAAAAA1jc/FfdXAVZ09C8yszjGgWSU13mHVnJXql3VQCLcBGAsYHQ/s1600/001.png)

[![img](https://1.bp.blogspot.com/-iA9YMX866iQ/XcI1Zvrh_rI/AAAAAAAA1jY/Sqht_XzfLZ4mc2-EMkMNaKHkdJZSjoVmACLcBGAsYHQ/s1600/002.png)](https://1.bp.blogspot.com/-iA9YMX866iQ/XcI1Zvrh_rI/AAAAAAAA1jY/Sqht_XzfLZ4mc2-EMkMNaKHkdJZSjoVmACLcBGAsYHQ/s1600/002.png)

[![img](https://1.bp.blogspot.com/-QkXs5_6dyRc/XcI1ZmF0MSI/AAAAAAAA1jU/7nnlxLjzrEQB-JhzhP-PmJy8pu5SOuFYwCLcBGAsYHQ/s1600/003.png)](https://1.bp.blogspot.com/-QkXs5_6dyRc/XcI1ZmF0MSI/AAAAAAAA1jU/7nnlxLjzrEQB-JhzhP-PmJy8pu5SOuFYwCLcBGAsYHQ/s1600/003.png)

[![img](https://1.bp.blogspot.com/-s7Yw1tmOYDk/XcI1auEplFI/AAAAAAAA1jg/gLM8oDnnWyYLvlkm0Cwev4RcPqq-yoedgCLcBGAsYHQ/s1600/004.png)](https://1.bp.blogspot.com/-s7Yw1tmOYDk/XcI1auEplFI/AAAAAAAA1jg/gLM8oDnnWyYLvlkm0Cwev4RcPqq-yoedgCLcBGAsYHQ/s1600/004.png)

[![img](https://1.bp.blogspot.com/-yu7zIx5lVuA/XcI1ayNENtI/AAAAAAAA1jk/Jg2S9ihTcNoeeeqFMhiLbXVRBuoi15u1gCLcBGAsYHQ/s1600/005.png)](https://1.bp.blogspot.com/-yu7zIx5lVuA/XcI1ayNENtI/AAAAAAAA1jk/Jg2S9ihTcNoeeeqFMhiLbXVRBuoi15u1gCLcBGAsYHQ/s1600/005.png)

[![img](https://1.bp.blogspot.com/-v6g0OMCEqKk/XcI1bL6OhCI/AAAAAAAA1jo/eTH9FqtPcTgi8F481mNmrp_UNNHgMlJ_ACLcBGAsYHQ/s1600/006.png)](https://1.bp.blogspot.com/-v6g0OMCEqKk/XcI1bL6OhCI/AAAAAAAA1jo/eTH9FqtPcTgi8F481mNmrp_UNNHgMlJ_ACLcBGAsYHQ/s1600/006.png)


(下圖)
**機器學習可能需要手動安裝 Python、Java (敝人沒測試)**

SQL Server Standard 安裝的 PolyBase 預設不是 Server，只是 Client，後面畫面要改設定，除非你另外有 PolyBase Server，否則可能安裝不下去 (過往經驗，這次沒測)

SQL Server Enterprise / Developer 安裝的 PolyBase 預設是 PolyBase Server。

[![img](https://1.bp.blogspot.com/-nobi7Oh5zzM/XcI1bX7yDGI/AAAAAAAA1js/Gjji2A7C-5cryEK85l1YuwnqWM54hmIMwCLcBGAsYHQ/s1600/007.png)](https://1.bp.blogspot.com/-nobi7Oh5zzM/XcI1bX7yDGI/AAAAAAAA1js/Gjji2A7C-5cryEK85l1YuwnqWM54hmIMwCLcBGAsYHQ/s1600/007.png)

[![img](https://1.bp.blogspot.com/-60t9uLqSQv4/XcI1bhmxjtI/AAAAAAAA1jw/iaTUUNdlxJ0VAc2I4APmQ0jN049KGhWzQCLcBGAsYHQ/s1600/008.png)](https://1.bp.blogspot.com/-60t9uLqSQv4/XcI1bhmxjtI/AAAAAAAA1jw/iaTUUNdlxJ0VAc2I4APmQ0jN049KGhWzQCLcBGAsYHQ/s1600/008.png)

[![img](https://1.bp.blogspot.com/-RPmN3fvmPSQ/XcI1b8TNOLI/AAAAAAAA1j0/0WOJFPbOo5UeyWw4swYvEObk1NmQDE3swCLcBGAsYHQ/s1600/009.png)](https://1.bp.blogspot.com/-RPmN3fvmPSQ/XcI1b8TNOLI/AAAAAAAA1j0/0WOJFPbOo5UeyWw4swYvEObk1NmQDE3swCLcBGAsYHQ/s1600/009.png)

[![img](https://1.bp.blogspot.com/-8gXr0F7xDag/XcI1cKdfo_I/AAAAAAAA1j4/3mW0A2nNoZQVDzYKjcA6MqLJ9eTfn5xBwCLcBGAsYHQ/s1600/010.png)](https://1.bp.blogspot.com/-8gXr0F7xDag/XcI1cKdfo_I/AAAAAAAA1j4/3mW0A2nNoZQVDzYKjcA6MqLJ9eTfn5xBwCLcBGAsYHQ/s1600/010.png)

[![img](https://1.bp.blogspot.com/-Wj10D1mCLQI/XcI1cY2oj6I/AAAAAAAA1j8/HpNPZuOik-8-JAqj5If3_ZHUnZd24e-BQCLcBGAsYHQ/s1600/011.png)](https://1.bp.blogspot.com/-Wj10D1mCLQI/XcI1cY2oj6I/AAAAAAAA1j8/HpNPZuOik-8-JAqj5If3_ZHUnZd24e-BQCLcBGAsYHQ/s1600/011.png)

[![img](https://1.bp.blogspot.com/-4l62mFo7f6w/XcI1ch5V_-I/AAAAAAAA1kA/pC5yT3rGPLAaUzFEIoezCrm3f9jfaq4pwCLcBGAsYHQ/s1600/012.png)](https://1.bp.blogspot.com/-4l62mFo7f6w/XcI1ch5V_-I/AAAAAAAA1kA/pC5yT3rGPLAaUzFEIoezCrm3f9jfaq4pwCLcBGAsYHQ/s1600/012.png)

[![img](https://1.bp.blogspot.com/-YetP736vmKo/XcI1dNlabDI/AAAAAAAA1kE/sGWXtwH_0S8C-EuvmzmmcywHZqhUiIgUQCLcBGAsYHQ/s1600/013.png)](https://1.bp.blogspot.com/-YetP736vmKo/XcI1dNlabDI/AAAAAAAA1kE/sGWXtwH_0S8C-EuvmzmmcywHZqhUiIgUQCLcBGAsYHQ/s1600/013.png)

[![img](https://1.bp.blogspot.com/-yVqHA3I4SRQ/XcI1dWH-vSI/AAAAAAAA1kI/53fHNYtj64UTs6f8ZDQjjb56YGqilVBHgCLcBGAsYHQ/s1600/014.png)](https://1.bp.blogspot.com/-yVqHA3I4SRQ/XcI1dWH-vSI/AAAAAAAA1kI/53fHNYtj64UTs6f8ZDQjjb56YGqilVBHgCLcBGAsYHQ/s1600/014.png)

[![img](https://1.bp.blogspot.com/-whsG2n_T0Kg/XcI1dhzkCRI/AAAAAAAA1kM/wdNtvZxxuoEQu016G09LkwbF9uGAo9BSgCLcBGAsYHQ/s1600/015.png)](https://1.bp.blogspot.com/-whsG2n_T0Kg/XcI1dhzkCRI/AAAAAAAA1kM/wdNtvZxxuoEQu016G09LkwbF9uGAo9BSgCLcBGAsYHQ/s1600/015.png)

[![img](https://1.bp.blogspot.com/-Y3R5M5kJ0UY/XcI1d2bJfmI/AAAAAAAA1kQ/Gw5yYPZVk1kz9auF74QX5vxibgxneYW9wCLcBGAsYHQ/s1600/016.png)](https://1.bp.blogspot.com/-Y3R5M5kJ0UY/XcI1d2bJfmI/AAAAAAAA1kQ/Gw5yYPZVk1kz9auF74QX5vxibgxneYW9wCLcBGAsYHQ/s1600/016.png)

[![img](https://1.bp.blogspot.com/-nzAv4r8Gg1E/XcI1eB5QtmI/AAAAAAAA1kU/6MB4CEQxKAsPTZglfSmvC7nf3TWWKzyCQCLcBGAsYHQ/s1600/017.png)](https://1.bp.blogspot.com/-nzAv4r8Gg1E/XcI1eB5QtmI/AAAAAAAA1kU/6MB4CEQxKAsPTZglfSmvC7nf3TWWKzyCQCLcBGAsYHQ/s1600/017.png)

[![img](https://1.bp.blogspot.com/-gzgxTyONlzg/XcI1eWfEHDI/AAAAAAAA1kY/ERBkIMoveCsqxqyO1qm4_tWUA4Pb2ywHACLcBGAsYHQ/s1600/018.png)](https://1.bp.blogspot.com/-gzgxTyONlzg/XcI1eWfEHDI/AAAAAAAA1kY/ERBkIMoveCsqxqyO1qm4_tWUA4Pb2ywHACLcBGAsYHQ/s1600/018.png)

[![img](https://1.bp.blogspot.com/-fqycWRRyvsY/XcI1ewy7Q8I/AAAAAAAA1kc/r6lG7FCynccBLn2zgoGDJNt7UcOo-yI2QCLcBGAsYHQ/s1600/019.png)](https://1.bp.blogspot.com/-fqycWRRyvsY/XcI1ewy7Q8I/AAAAAAAA1kc/r6lG7FCynccBLn2zgoGDJNt7UcOo-yI2QCLcBGAsYHQ/s1600/019.png)

[![img](https://1.bp.blogspot.com/-BZi4Dy0exqM/XcI1e4Pt3WI/AAAAAAAA1kg/jJLifwoF4iIiDNkr0bIQ3TuNDF9BtZjzgCLcBGAsYHQ/s1600/020.png)](https://1.bp.blogspot.com/-BZi4Dy0exqM/XcI1e4Pt3WI/AAAAAAAA1kg/jJLifwoF4iIiDNkr0bIQ3TuNDF9BtZjzgCLcBGAsYHQ/s1600/020.png)

[![img](https://1.bp.blogspot.com/-XgjhOyjAkU4/XcI1fWM4gUI/AAAAAAAA1kk/m9_tC3iv-mY-4pfbO-J_Ko-QTWmCnzBvgCLcBGAsYHQ/s1600/021.png)](https://1.bp.blogspot.com/-XgjhOyjAkU4/XcI1fWM4gUI/AAAAAAAA1kk/m9_tC3iv-mY-4pfbO-J_Ko-QTWmCnzBvgCLcBGAsYHQ/s1600/021.png)

[![img](https://1.bp.blogspot.com/-dvM197fyGao/XcI1fpFcKwI/AAAAAAAA1ko/eStONaXXuiEBcYoD24n_TvBNlS5b3gyUACLcBGAsYHQ/s1600/022.png)](https://1.bp.blogspot.com/-dvM197fyGao/XcI1fpFcKwI/AAAAAAAA1ko/eStONaXXuiEBcYoD24n_TvBNlS5b3gyUACLcBGAsYHQ/s1600/022.png)

[![img](https://1.bp.blogspot.com/-6LP_OButiiE/XcI1f352KdI/AAAAAAAA1ks/eBQtV_StJVgDOR4TFLdeqtYDbu1ljcdJACLcBGAsYHQ/s1600/023.png)](https://1.bp.blogspot.com/-6LP_OButiiE/XcI1f352KdI/AAAAAAAA1ks/eBQtV_StJVgDOR4TFLdeqtYDbu1ljcdJACLcBGAsYHQ/s1600/023.png)

[![img](https://1.bp.blogspot.com/-hzBW82E9LqU/XcI1gG3Ml6I/AAAAAAAA1kw/DRJyUroJhT4vpKQd1LX_-AEjsm8cu2jYQCLcBGAsYHQ/s1600/024.png)](https://1.bp.blogspot.com/-hzBW82E9LqU/XcI1gG3Ml6I/AAAAAAAA1kw/DRJyUroJhT4vpKQd1LX_-AEjsm8cu2jYQCLcBGAsYHQ/s1600/024.png)

[![img](https://1.bp.blogspot.com/-MxxldFAcBNE/XcI1gi9y7OI/AAAAAAAA1k0/w7-ejjE6urIwaO5kaNsoeFpp6qq73FP2ACLcBGAsYHQ/s1600/025.png)](https://1.bp.blogspot.com/-MxxldFAcBNE/XcI1gi9y7OI/AAAAAAAA1k0/w7-ejjE6urIwaO5kaNsoeFpp6qq73FP2ACLcBGAsYHQ/s1600/025.png)

[![img](https://1.bp.blogspot.com/-nLX5ww23i44/XcI1gqefllI/AAAAAAAA1k4/Zf0ejxV6LVoPaBZ2I5lyahMw0FUBQjSzACLcBGAsYHQ/s1600/026.png)](https://1.bp.blogspot.com/-nLX5ww23i44/XcI1gqefllI/AAAAAAAA1k4/Zf0ejxV6LVoPaBZ2I5lyahMw0FUBQjSzACLcBGAsYHQ/s1600/026.png)

[![img](https://1.bp.blogspot.com/-aLAG4KtVbNE/XcI1g3IN3OI/AAAAAAAA1k8/nKXQ9X-eEM0xXYMQC_dLTAxfX-6q7vTNwCLcBGAsYHQ/s1600/027.png)](https://1.bp.blogspot.com/-aLAG4KtVbNE/XcI1g3IN3OI/AAAAAAAA1k8/nKXQ9X-eEM0xXYMQC_dLTAxfX-6q7vTNwCLcBGAsYHQ/s1600/027.png)

[![img](https://1.bp.blogspot.com/-PqOHXqd2vZ4/XcI1hVdZ9nI/AAAAAAAA1lA/NVjmYYfTcMAEeTvtZqQyrJUZbpFDRL6tACLcBGAsYHQ/s1600/028.png)](https://1.bp.blogspot.com/-PqOHXqd2vZ4/XcI1hVdZ9nI/AAAAAAAA1lA/NVjmYYfTcMAEeTvtZqQyrJUZbpFDRL6tACLcBGAsYHQ/s1600/028.png)

[![img](https://1.bp.blogspot.com/-Ds-WWERD_Xs/XcI1hWMOqbI/AAAAAAAA1lE/EV6YlC35fecuAAC_iMXazKt1RplNFMeuACLcBGAsYHQ/s1600/029.png)](https://1.bp.blogspot.com/-Ds-WWERD_Xs/XcI1hWMOqbI/AAAAAAAA1lE/EV6YlC35fecuAAC_iMXazKt1RplNFMeuACLcBGAsYHQ/s1600/029.png)

[![img](https://1.bp.blogspot.com/-XR245pTf4z4/XcI1hllHwpI/AAAAAAAA1lI/23FHFaiKctYgIsfbSR2YMbsOZo2KfpNAACLcBGAsYHQ/s640/030.png)](https://1.bp.blogspot.com/-XR245pTf4z4/XcI1hllHwpI/AAAAAAAA1lI/23FHFaiKctYgIsfbSR2YMbsOZo2KfpNAACLcBGAsYHQ/s1600/030.png)

[![img](https://1.bp.blogspot.com/-B7Ruxl2qohs/XcI1iLKnf9I/AAAAAAAA1lM/gQlrbTFsN1IMhaRaLRlfUAWZiPJtdCTAACLcBGAsYHQ/s640/031.png)](https://1.bp.blogspot.com/-B7Ruxl2qohs/XcI1iLKnf9I/AAAAAAAA1lM/gQlrbTFsN1IMhaRaLRlfUAWZiPJtdCTAACLcBGAsYHQ/s1600/031.png)

[![img](https://1.bp.blogspot.com/-9kTR2t-guSQ/XcI1ifTxifI/AAAAAAAA1lQ/-7qvkaL0_3MtG_CQBL-BtVpLjcEdOmXKgCLcBGAsYHQ/s1600/032.png)](https://1.bp.blogspot.com/-9kTR2t-guSQ/XcI1ifTxifI/AAAAAAAA1lQ/-7qvkaL0_3MtG_CQBL-BtVpLjcEdOmXKgCLcBGAsYHQ/s1600/032.png)

[![img](https://1.bp.blogspot.com/-lLTuTmDn_Lk/XcI1iWR7_7I/AAAAAAAA1lU/Yav2FTRM3IECFXqnC9DI0a5ULLIwBNDDACLcBGAsYHQ/s1600/033.png)](https://1.bp.blogspot.com/-lLTuTmDn_Lk/XcI1iWR7_7I/AAAAAAAA1lU/Yav2FTRM3IECFXqnC9DI0a5ULLIwBNDDACLcBGAsYHQ/s1600/033.png)

[![img](https://1.bp.blogspot.com/-1rprRdx6eH4/XcI1ixtN9WI/AAAAAAAA1lY/6HeswUjd2p4HxmoahV9o92NRRX69I5avQCLcBGAsYHQ/s640/034.png)](https://1.bp.blogspot.com/-1rprRdx6eH4/XcI1ixtN9WI/AAAAAAAA1lY/6HeswUjd2p4HxmoahV9o92NRRX69I5avQCLcBGAsYHQ/s1600/034.png)

[![img](https://1.bp.blogspot.com/-6YL2ZhcubHk/XcI1jFpk9UI/AAAAAAAA1lc/hO1E-urOBmMP9lpcXlSaQJKZ7Aqxsj0KgCLcBGAsYHQ/s1600/035.png)](https://1.bp.blogspot.com/-6YL2ZhcubHk/XcI1jFpk9UI/AAAAAAAA1lc/hO1E-urOBmMP9lpcXlSaQJKZ7Aqxsj0KgCLcBGAsYHQ/s1600/035.png)

[![img](https://1.bp.blogspot.com/-ZQ3ukmK7mmE/XcI1jHQhnXI/AAAAAAAA1lg/oFkBNqj3BGMLMIi272la032c0gPPlyLTQCLcBGAsYHQ/s1600/036.png)](https://1.bp.blogspot.com/-ZQ3ukmK7mmE/XcI1jHQhnXI/AAAAAAAA1lg/oFkBNqj3BGMLMIi272la032c0gPPlyLTQCLcBGAsYHQ/s1600/036.png)

[![img](https://1.bp.blogspot.com/-xwJs2jUE1u0/XcI1jqP10jI/AAAAAAAA1lk/_1WJaAOuiEUD0lSTCAIL8RfEbCsd7rbuACLcBGAsYHQ/s1600/037.png)](https://1.bp.blogspot.com/-xwJs2jUE1u0/XcI1jqP10jI/AAAAAAAA1lk/_1WJaAOuiEUD0lSTCAIL8RfEbCsd7rbuACLcBGAsYHQ/s1600/037.png)
