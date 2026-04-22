# Share Article Guide — Learn in Public 分享文章规范

## 定位

基于概念调研报告，生成可分享到 X.com / LinkedIn 的文章。理念是 Learn in Public：记录学习过程，不是展示专业。

## 输出文件

每个概念生成两篇分享文章，存放在概念目录下：

```text
concepts/<concept-slug>/
  reports/YYYY-MM-DD-deep-dive.md     # 调研报告（已有）
  share-zh.md                          # 中文分享文章
  share-en.md                          # 英文分享文章
```

## 中文文章规范

### 篇幅

- 目标：1,500-3,000 字（阅读 3-6 分钟）
- 硬下限：1,500 字
- 硬上限：5,000 字

### 结构模板

```text
1. 钩子（前 2-3 行）
   一个具体的个人经历或困惑，让读者想读下去

2. 背景 / 动机
   为什么我（一个 UX 设计师）要学这个概念
   我了解这个概念的原因

3. 概念的历史来源
   这个概念从哪来的、谁提出的、关键演进节点
   精简客观，不加个人解读
   让读者感受到概念的分量和时间跨度

4. 概念的核心流程 / 核心定义
   标准的、客观的概念介绍
   可以用 ASCII 流程图表达核心流程
   列出 2-3 个关键子概念，每个一句话
   这一块是全文最「硬」的部分，与前后的个人叙事形成对比

5. 我的理解
   用日常类比解释核心概念
   带上自己的理解和感悟
   承认可能理解不完整

6. 在我的项目中怎么用
   结合真实项目（如 Vibe Capture）做分析
   具体到文件、配置、流程
   产品名称自然出现，不是硬广

7. 几个关键心得
   编号列表，每条 1-2 句话
   从设计师/非工程师的视角提炼

8. 收尾
   简洁，一句话点题或开放性问题
   可自然联结更大的人生叙事
```

### 风格

严格遵守 `rules/writing-style.md` 中定义的所有规则。

## 英文文章规范

### 篇幅

- 目标：800-1,500 words（阅读 3-6 分钟）
- 硬下限：800 words
- 硬上限：3,000 words

### 语言要求

- 必须符合英语母语用户的语言习惯
- 语气：conversational，非正式但专业
- 避免 press-release 式的官方口吻
- Show, don't tell：用具体例子和数字说话
- 开头即给价值承诺：「Here's what I learned...」
- 每句话推动读者往下读

### 注意事项

- 英文版不是中文版的直译，而是基于同一素材的重新写作
- 保留作者的个人视角（UX designer learning engineering concepts）
- 产品名、项目名保持英文原形
- 适当加入 cultural context（如 design background, indie dev journey）

## X.com 发布策略

### 文章发布

- 使用 X Articles / 长推文功能发布完整文章
- 阅读停留 > 2 分钟可获 20 倍 like 权重（算法友好）
- 2026 年算法不再打压外链，文章类内容被主动推荐

### 配套 Thread（可选）

如果需要同时生成 Thread 版本：
- 5-8 条为最佳
- 每条是完整的思想单元
- 第一条是强钩子，能独立传播
- 最后一条做总结 + 提问

### 发布后

- 发布后 1 小时内积极回复每一条评论（算法权重 150 倍 like）
- 书签收藏权重 20 倍 like

## Frontmatter

分享文章使用以下 frontmatter：

```yaml
---
concept: PR and CI
slug: pr-and-ci
type: share
language: zh-CN / en
created_at: 2026-04-21
based_on: reports/2026-04-20-deep-dive.md
platform: x.com / linkedin
---
```
