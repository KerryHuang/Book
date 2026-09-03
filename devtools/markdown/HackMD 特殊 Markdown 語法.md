---
kind: original
---

HackMD特殊MarkDown語法
===

這邊要跟大家介紹非常好用功能:內建目錄
打上\[TOC]會自動建立目錄

目錄
===
`[TOC]`以下為TOC特殊語法
[TOC]

```md
目錄
===
[TOC]
```

---

## 區塊標籤標註
>[name=MingRay] [time=now] [color=#B40431]
>>[name=MingRay] [time=now] [color=#333333]
```md
>[name=MingRay] [time=now] [color=#B40431]
>>[name=MingRay] [time=now] [color=#333333]
```

---

## emoji
:accept: :satisfied: :+1: 

```
:accept: :satisfied: :+1: 
```


---

## 標籤

###### tags: `HackMD新手教學`

```
###### tags: `HackMD新手教學` (主標籤) `教學` 副標籤
```

---

## 註腳

註腳1[^1].
註腳2[^2].
行內註腳[^行內註腳]定義
重複的註腳2[^2].

[^1]:註腳1  定義
[^2]:註腳2: 定義
重複的註腳2: 定義
[^行內註腳]: 行內註腳: 定義

```md
註腳1[^1].
註腳2[^2].
行內註腳[^行內註腳]定義
重複的註腳2[^2].

[^1]:註腳1  定義
[^2]:註腳2: 定義
    重複的註腳2: 定義
        
[^行內註腳]: 行內註腳: 定義

```

---


## 外部媒體

### Youtube

```
{%youtube 1G4isv_Fylg %}
{%youtube v=?後的id %}
```

### Vimeo

```
{%vimeo 124148255 %}
{%vimeo 網址最後的數字id %}
```

### Gist

```
{%gist MingRay98/0b4d70945b5259a209b72e486bc2a1e3%}
{%gist github後的連結/%}
```

### PDF
**注意：請使用 https 的網址，否則可能會被您的瀏覽器阻擋載入**


```
{%pdf https://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf %}
{%pdf pdf的連結 %}
```

## MathJax

使用 **MathJax** 語法 來產生 *LaTeX* 數學表達式，
但是開始的 `$` 後面以及結尾的 `$` 前面不能有空白：

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}.
$$

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

```
The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}.
$$

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$
```