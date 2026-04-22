# CLAUDE.md — 仓库级强制指令

## 核心约束（最高优先级）

当用户的消息中出现以下任何触发词或意图时：

**触发词列表：** 学习、了解、调研、深潜、deep dive、explain、研究、对比、分析、理解、搞懂、弄清、解释、比较、探索、探究、掌握、study、research、compare、investigate、什么是、帮我看看、帮我查、系统学习、深入了解、深挖

**你必须按以下顺序执行，不得跳过：**

1. **先读规则** — 依次读取以下文件：
   - `rules/research-workflow.md`
   - `rules/source-quality.md`
   - `rules/report-style.md`
   - `rules/report-filing.md`
   - `rules/writing-style.md`
   - `rules/share-article-guide.md`
2. **再读技能定义** — 读取 `skills/concept-deep-dive/SKILL.md`
3. **然后先问用户动机**（Step 2），不要直接开始研究
4. 等用户回答后，才开始执行调研和输出

## 禁止行为

- **禁止**在没有读取上述文件的情况下直接口头回复学习/调研类请求
- **禁止**凭记忆或通用知识直接讲解概念而跳过仓库定义的工作流
- **禁止**用「我来给你解释一下」这类方式开头然后直接输出内容
- **禁止**跳过 Step 2（询问动机）直接开始生成报告
- 如果因为任何原因无法读取上述文件，必须先告知用户并等待指示

## 执行确认

在完成步骤 1-2 的文件读取后，进入 SKILL.md 定义的 5 步工作流。最终输出包含两类文档：
- 调研报告（保存到 `concepts/<slug>/reports/`）
- 分享文章（保存到 `concepts/<slug>/`，中英文各一篇）

## 非学习类请求

对于不涉及概念学习/调研的请求（如文件整理、脚本修改、仓库维护等），按正常方式处理即可，无需触发上述流程。
