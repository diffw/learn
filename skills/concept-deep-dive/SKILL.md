---
name: concept-deep-dive
description: Research a concept in depth, answer the user's follow-up questions, and generate a Learn in Public article. Trigger words include: 学习、了解、调研、深潜、deep dive、explain、研究、对比、分析、理解、搞懂、弄清、解释、比较、探索、探究、掌握、study、research、compare、investigate、深挖、什么是、系统学习、深入了解. Examples: "帮我调研 X", "我想系统学习一个新方法", "什么是 Y", "帮我深入了解 Z". IMPORTANT: Before executing this skill, you MUST first read all files in rules/ directory. Never skip reading rules and this skill definition.
---

# Concept Deep Dive

## 完整工作流（5 步）

### Step 1：接收学习请求

用户表达想了解某个概念。提取初步信息：概念名、可能的领域、可能的目标仓库。

### Step 2：询问动机和背景（不可跳过）

在开始研究之前，向用户提出一组问题（放在**一条消息**里），包括但不限于：

- 你想了解这个概念的原因/动机是什么？
- 你目前对它了解多少？
- 你希望从哪个角度理解？
- 有没有具体项目或场景想结合分析？

**等用户回答后**才进入 Step 3。

### Step 3：研究并生成报告

1. Read `concept-deep-dive-prompt-v5.md` and treat it as the default report structure.
2. Read all rules: `rules/research-workflow.md`, `rules/source-quality.md`, `rules/report-style.md`, `rules/report-filing.md`.
3. Extract runtime inputs:
   - concept
   - optional domain
   - optional target repository or local project path for section 8
   - motivation（from Step 2）
4. Resolve output path:

```bash
python3 scripts/prepare_concept_report.py --concept "Honest Agent" --root . --json
```

5. Research the concept using the prompt's 0-8 structure, incorporating the user's background and motivation.
6. Save the report under `concepts/<slug>/reports/`.
7. Reply to the user with the saved path and a short summary.

### Step 4：问答跟进

用户阅读报告后会提出问题和思考。此时：

1. Read the user's questions (from Obsidian notes, chat messages, or other sources).
2. Answer each question in depth — same quality standard as the main report body. Do additional research if needed.
3. Integrate the Q&A into the **existing** report file as a new numbered section (e.g., section 9, 10, ...).
4. **Never create a new version file** (no v2, v3 suffixes). Always update the original report in place.
5. If the user asks multiple rounds of questions, append new subsections (9.1, 9.2, ...) without overwriting prior Q&A.
6. After updating, reply with what was added and the file path.

### Step 5：生成 Learn in Public 分享文章

When the report and Q&A are complete (or user explicitly requests it):

1. Read `rules/writing-style.md` — strictly follow the user's personal writing style.
2. Read `rules/share-article-guide.md` — follow platform length and format requirements.
3. Based on the report + Q&A + project analysis, produce two articles:
   - `concepts/<slug>/share-zh.md` — 中文版（1,500-3,000 字）
   - `concepts/<slug>/share-en.md` — 英文版（800-1,500 words）
4. The article must naturally mention the user's product name (e.g., Vibe Capture) as a real case study.
5. The English version is NOT a translation — it's a rewrite for native English readers.
6. Reply with saved paths.

## Decision Rules

- If the user provides a custom prompt, use it instead of `concept-deep-dive-prompt-v5.md`, but keep this repository's filing rules.
- If the user names only the concept, leave `domain` empty rather than guessing.
- If section 8 applies, read [references/repo-analysis-policy.md](references/repo-analysis-policy.md) before evaluating the repository.
- If no real target repository is available for section 8, keep the section and explicitly state that the repository analysis could not be completed.
- Do not force the current learning repository to become the section 8 target unless it is obviously the intended project.

## Research Rules

- Browse the web for any current, unstable, or source-sensitive information, especially in sections 5 and 7.
- Prefer primary sources: papers, official docs, official repositories, maintainer notes, release notes.
- Keep the report in Chinese unless the user explicitly requests another language.
- Distinguish facts from inferences. When a claim is inferred, label it clearly.
- If reliable information cannot be found, say so directly instead of filling the gap with generic prose.
- Treat report depth as the default. Unless the user asks for brevity, target a long-form report, typically 10000+ Chinese characters when reliable sources support it.
- In paper sections, explain problem setting, method design, validation logic, findings, limits, and influence. Do not collapse a paper into one short paragraph.

## Output Rules

- Save every finished report with the frontmatter defined in `rules/report-filing.md`.
- Preserve the prompt's numbered structure instead of rewriting it into a different outline.
- Reuse an existing concept slug folder when present.
- Use ASCII for all process, logic, state, and map expressions, such as `A -> B -> C` and `input -> process -> output`.
