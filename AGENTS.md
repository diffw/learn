# AGENTS.md — Learn Project Router

## 项目定位

这是一个面向“新概念 / 新方法深度学习”的研究仓库。目标不是临时聊天回答，而是把一次次调研沉淀为可复用、可归档、可继续迭代的概念报告。

## 模块总览

| 模块 | 路径 | 作用 |
|---|---|---|
| Prompt | `concept-deep-dive-prompt-v5.md` | 当前概念深潜调研 prompt 真相源 |
| Rules | `rules/` | 研究流程、来源质量、归档规范 |
| Skills | `skills/` | 可重复执行的学习工作流 |
| Concepts | `concepts/` | 每个概念的长期知识目录 |
| Scripts | `scripts/` | 生成 slug、解析落盘路径等辅助脚本 |

## 路由规则

- 当用户表达”学习 / 了解 / 调研 / 深潜 / deep dive / explain / 研究 / 对比 / 分析 / 理解 / 搞懂 / 弄清 / 解释 / 比较 / 探索 / 探究 / 掌握 / study / research / compare / investigate / 深挖 / 什么是 / 系统学习 / 深入了解”等意图，涉及一个概念、方法、框架、模式、协议、工作流、心智模型时：
  1. **必须**先读 `rules/research-workflow.md`
  2. **必须**再读 `rules/source-quality.md`
  3. **必须**再读 `rules/report-style.md`
  4. **必须**再读 `rules/report-filing.md`
  5. **必须**再读 `rules/writing-style.md`
  6. **必须**再读 `rules/share-article-guide.md`
  7. **必须**最后打开 `skills/concept-deep-dive/SKILL.md`
  8. **禁止**在完成上述 1-7 步之前直接回复用户的学习请求
  9. **必须**先执行 Step 2（询问用户动机），等用户回答后才开始研究
- 当用户要求生成分享文章时，读 `rules/writing-style.md` + `rules/share-article-guide.md`。
- 当任务只是整理、重命名、搬运、归档已有报告时，只读 `rules/report-filing.md`。
- 不要默认递归扫描整个 `skills/`；只有在路由已命中后再打开对应 skill。

## 执行约束

- 默认使用 `concept-deep-dive-prompt-v5.md` 作为调研模板；只有当用户明确给出替代 prompt 时才覆盖。
- 默认输出语言为中文；只有用户明确要求其他语言时才切换。
- 凡是流程、逻辑、知识地图、状态迁移、输入输出表达，统一使用 ASCII 形式，如 `A -> B -> C`。
- 默认把“足够细、足够能学”放在“短”之前；只要资料足够，完整报告目标篇幅不低于 `10000` 字。
- 调研结果必须先保存到仓库里，再向用户汇报。
- 落盘路径必须通过 `python3 scripts/prepare_concept_report.py ...` 生成，避免手工随意命名。
- 已有概念目录优先复用既有 slug，不要重复创建近义目录。
- 第 5、7 层以及任何可能变化的信息必须联网核实，并优先使用一手来源。
- 第 8 层只能基于真实仓库内容分析；如果没有可访问的目标仓库，必须明确写出“无法分析”，禁止补写泛泛内容。

## 完成标准

- 报告已写入正确目录。
- 结构遵循 prompt 的 0-8 层。
- 不确定信息被显式标注为推测。
- 最终回复包含保存路径与一句话摘要。
