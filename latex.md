# LaTeX 常用公式与符号速查

> 说明：以下内容适用于 Markdown 中常见的 LaTeX/MathJax/KaTeX 写法。行内公式通常写作 `$...$`，独立公式通常写作 `$$...$$`。

## 1. 基础写法

| 用途 | LaTeX | 效果说明 |
| --- | --- | --- |
| 行内公式 | `$a+b=c$` | 在正文中显示公式 |
| 独立公式 | `$$a+b=c$$` | 单独成行显示公式 |
| 上标 | `x^2` | x 的平方 |
| 下标 | `a_n` | 第 n 项 |
| 分组 | `x^{n+1}` | 多字符上下标需用花括号 |
| 分数 | `\frac{a}{b}` | a 除以 b |
| 根号 | `\sqrt{x}` | 平方根 |
| n 次根 | `\sqrt[n]{x}` | n 次方根 |
| 省略号 | `\cdots`, `\ldots` | 居中/底部省略号 |
| 空格 | `\,`, `\quad`, `\qquad` | 小/中/大空格 |
| 文本 | `\text{if } x>0` | 公式中插入普通文本 |

## 2. 常用运算符

| 符号 | LaTeX | 说明 |
| --- | --- | --- |
| $+$ | `+` | 加法 |
| $-$ | `-` | 减法 |
| $\times$ | `\times` | 乘法 |
| $\div$ | `\div` | 除法 |
| $\cdot$ | `\cdot` | 点乘/乘号 |
| $\pm$ | `\pm` | 正负号 |
| $\mp$ | `\mp` | 负正号 |
| $=$ | `=` | 等于 |
| $\ne$ | `\ne` | 不等于 |
| $\approx$ | `\approx` | 约等于 |
| $\equiv$ | `\equiv` | 恒等于/同余 |
| $<$ | `<` | 小于 |
| $>$ | `>` | 大于 |
| $\le$ | `\le` | 小于等于 |
| $\ge$ | `\ge` | 大于等于 |
| $\ll$ | `\ll` | 远小于 |
| $\gg$ | `\gg` | 远大于 |
| $\propto$ | `\propto` | 正比于 |
| $\infty$ | `\infty` | 无穷大 |

## 3. 希腊字母

| 小写 | LaTeX | 大写 | LaTeX |
| --- | --- | --- | --- |
| $\alpha$ | `\alpha` | $A$ | `A` |
| $\beta$ | `\beta` | $B$ | `B` |
| $\gamma$ | `\gamma` | $\Gamma$ | `\Gamma` |
| $\delta$ | `\delta` | $\Delta$ | `\Delta` |
| $\epsilon$ | `\epsilon` | $E$ | `E` |
| $\varepsilon$ | `\varepsilon` | $E$ | `E` |
| $\zeta$ | `\zeta` | $Z$ | `Z` |
| $\eta$ | `\eta` | $H$ | `H` |
| $\theta$ | `\theta` | $\Theta$ | `\Theta` |
| $\vartheta$ | `\vartheta` | $\Theta$ | `\Theta` |
| $\iota$ | `\iota` | $I$ | `I` |
| $\kappa$ | `\kappa` | $K$ | `K` |
| $\lambda$ | `\lambda` | $\Lambda$ | `\Lambda` |
| $\mu$ | `\mu` | $M$ | `M` |
| $\nu$ | `\nu` | $N$ | `N` |
| $\xi$ | `\xi` | $\Xi$ | `\Xi` |
| $o$ | `o` | $O$ | `O` |
| $\pi$ | `\pi` | $\Pi$ | `\Pi` |
| $\varpi$ | `\varpi` | $\Pi$ | `\Pi` |
| $\rho$ | `\rho` | $P$ | `P` |
| $\varrho$ | `\varrho` | $P$ | `P` |
| $\sigma$ | `\sigma` | $\Sigma$ | `\Sigma` |
| $\varsigma$ | `\varsigma` | $\Sigma$ | `\Sigma` |
| $\tau$ | `\tau` | $T$ | `T` |
| $\upsilon$ | `\upsilon` | $\Upsilon$ | `\Upsilon` |
| $\phi$ | `\phi` | $\Phi$ | `\Phi` |
| $\varphi$ | `\varphi` | $\Phi$ | `\Phi` |
| $\chi$ | `\chi` | $X$ | `X` |
| $\psi$ | `\psi` | $\Psi$ | `\Psi` |
| $\omega$ | `\omega` | $\Omega$ | `\Omega` |

## 4. 集合与逻辑符号

| 符号 | LaTeX | 说明 |
| --- | --- | --- |
| $\in$ | `\in` | 属于 |
| $\notin$ | `\notin` | 不属于 |
| $\subset$ | `\subset` | 真子集 |
| $\subseteq$ | `\subseteq` | 子集 |
| $\supset$ | `\supset` | 真超集 |
| $\supseteq$ | `\supseteq` | 超集 |
| $\cup$ | `\cup` | 并集 |
| $\cap$ | `\cap` | 交集 |
| $\setminus$ | `\setminus` | 差集 |
| $\emptyset$ | `\emptyset` | 空集 |
| $\mathbb{N}$ | `\mathbb{N}` | 自然数集 |
| $\mathbb{Z}$ | `\mathbb{Z}` | 整数集 |
| $\mathbb{Q}$ | `\mathbb{Q}` | 有理数集 |
| $\mathbb{R}$ | `\mathbb{R}` | 实数集 |
| $\mathbb{C}$ | `\mathbb{C}` | 复数集 |
| $\forall$ | `\forall` | 对所有 |
| $\exists$ | `\exists` | 存在 |
| $\nexists$ | `\nexists` | 不存在 |
| $\land$ | `\land` | 且 |
| $\lor$ | `\lor` | 或 |
| $\lnot$ | `\lnot` | 非 |
| $\Rightarrow$ | `\Rightarrow` | 推出 |
| $\Leftarrow$ | `\Leftarrow` | 被推出 |
| $\Leftrightarrow$ | `\Leftrightarrow` | 等价 |
| $\therefore$ | `\therefore` | 因此 |
| $\because$ | `\because` | 因为 |

## 5. 微积分常用公式

```latex
\lim_{x \to a} f(x)
\frac{d}{dx} f(x)
\frac{\partial f}{\partial x}
\int_a^b f(x)\,dx
\iint_D f(x,y)\,dA
\iiint_V f(x,y,z)\,dV
\sum_{i=1}^{n} a_i
\prod_{i=1}^{n} a_i
```

常见公式示例：

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$

$$
\frac{d}{dx}x^n = n x^{n-1}
$$

$$
\int_a^b f'(x)\,dx = f(b)-f(a)
$$

$$
e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!}
$$

## 6. 线性代数

```latex
\vec{v}
\mathbf{A}
\begin{pmatrix} a & b \\ c & d \end{pmatrix}
\det(A)
A^{-1}
A^T
\langle u, v \rangle
\|v\|
```

常见公式示例：

$$
A = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}, \quad
\det(A)=ad-bc
$$

$$
A^{-1}=\frac{1}{ad-bc}\begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix}
$$

$$
\langle u,v\rangle = \sum_{i=1}^{n}u_i v_i, \quad \|v\|=\sqrt{\langle v,v\rangle}
$$

## 7. 概率与统计

| 用途 | LaTeX | 说明 |
| --- | --- | --- |
| 概率 | `P(A)` | 事件 A 的概率 |
| 条件概率 | `P(A\mid B)` | B 发生时 A 的概率 |
| 期望 | `\mathbb{E}[X]` | 随机变量期望 |
| 方差 | `\operatorname{Var}(X)` | 方差 |
| 协方差 | `\operatorname{Cov}(X,Y)` | 协方差 |
| 正态分布 | `X \sim \mathcal{N}(\mu,\sigma^2)` | X 服从正态分布 |

常见公式示例：

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
$$

$$
\mathbb{E}[X]=\sum_i x_i p_i
$$

$$
\operatorname{Var}(X)=\mathbb{E}\left[(X-\mu)^2\right]
$$

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

## 8. 三角函数与常用恒等式

| 函数 | LaTeX |
| --- | --- |
| $\sin x$ | `\sin x` |
| $\cos x$ | `\cos x` |
| $\tan x$ | `\tan x` |
| $\cot x$ | `\cot x` |
| $\sec x$ | `\sec x` |
| $\csc x$ | `\csc x` |
| $\arcsin x$ | `\arcsin x` |
| $\arccos x$ | `\arccos x` |
| $\arctan x$ | `\arctan x` |

常见公式示例：

$$
\sin^2 x + \cos^2 x = 1
$$

$$
\sin(a\pm b)=\sin a\cos b \pm \cos a\sin b
$$

$$
\cos(a\pm b)=\cos a\cos b \mp \sin a\sin b
$$

$$
e^{i\theta}=\cos\theta+i\sin\theta
$$

## 9. 箭头、关系与装饰符

| 符号 | LaTeX | 说明 |
| --- | --- | --- |
| $\to$ | `\to` | 到/趋向 |
| $\leftarrow$ | `\leftarrow` | 左箭头 |
| $\rightarrow$ | `\rightarrow` | 右箭头 |
| $\mapsto$ | `\mapsto` | 映射到 |
| $\leftrightarrow$ | `\leftrightarrow` | 双向箭头 |
| $\uparrow$ | `\uparrow` | 上箭头 |
| $\downarrow$ | `\downarrow` | 下箭头 |
| $\hat{x}$ | `\hat{x}` | 帽子 |
| $\bar{x}$ | `\bar{x}` | 横线 |
| $\tilde{x}$ | `\tilde{x}` | 波浪线 |
| $\dot{x}$ | `\dot{x}` | 一阶导点 |
| $\ddot{x}$ | `\ddot{x}` | 二阶导点 |
| $\overline{AB}$ | `\overline{AB}` | 上横线 |
| $\underline{AB}$ | `\underline{AB}` | 下横线 |

## 10. 括号与定界符

| 效果 | LaTeX |
| --- | --- |
| 圆括号 | `(x)` |
| 方括号 | `[x]` |
| 花括号 | `\{x\}` |
| 绝对值 | `\lvert x \rvert` |
| 范数 | `\lVert x \rVert` |
| 自动调整大小 | `\left( \frac{a}{b} \right)` |
| 分段函数 | `\begin{cases} ... \end{cases}` |

分段函数示例：

$$
f(x)=
\begin{cases}
x^2, & x \ge 0 \\
-x, & x < 0
\end{cases}
$$

## 11. 对齐与多行公式

```latex
\begin{aligned}
a+b &= c \\
x+y &= z
\end{aligned}
```

示例：

$$
\begin{aligned}
(a+b)^2 &= a^2 + 2ab + b^2 \\
(a-b)^2 &= a^2 - 2ab + b^2
\end{aligned}
$$

## 12. 常见字体与样式

| 效果 | LaTeX | 用途 |
| --- | --- | --- |
| $\mathbf{x}$ | `\mathbf{x}` | 粗体 |
| $\mathit{x}$ | `\mathit{x}` | 斜体 |
| $\mathrm{d}x$ | `\mathrm{d}x` | 正体文本/微分符号 |
| $\mathbb{R}$ | `\mathbb{R}` | 数集 |
| $\mathcal{F}$ | `\mathcal{F}` | 花体 |
| $\mathscr{L}$ | `\mathscr{L}` | 手写体，视渲染器支持情况而定 |
| $\operatorname{rank}(A)$ | `\operatorname{rank}(A)` | 自定义运算符 |

## 13. 物理与工程常用写法

$$
F=ma
$$

$$
E=mc^2
$$

$$
V=IR
$$

$$
\nabla f = \left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\right)
$$

$$
\nabla \cdot \mathbf{F}, \quad \nabla \times \mathbf{F}
$$

## 14. 速记建议

- 多字符上下标一定使用花括号，例如 `x^{n+1}`、`a_{i,j}`。
- 分数、根号、矩阵、分段函数是最常用的结构，建议优先掌握。
- 在 Markdown 中如果公式无法渲染，通常是平台未启用 MathJax/KaTeX，或反斜杠、美元符号需要转义。
- 长公式建议使用 `aligned` 环境保持等号对齐，提升可读性。
