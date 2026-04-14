# Report Filing

## 目录约定

每个概念使用一个固定目录：

```text
concepts/<concept-slug>/
  reports/
```

只有真的需要补充材料时，才额外创建：

```text
concepts/<concept-slug>/notes/
concepts/<concept-slug>/assets/
```

## 报告命名

- 主报告路径：`concepts/<concept-slug>/reports/YYYY-MM-DD-deep-dive.md`
- 同一天重复生成时，追加版本号：`YYYY-MM-DD-deep-dive-v2.md`
- `concept-slug` 一旦建立，后续优先复用，不随意改名

## Frontmatter

每份报告顶部都使用如下 frontmatter：

```yaml
---
concept: Honest Agent
slug: honest-agent
domain:
created_at: 2026-04-14
prompt: concept-deep-dive-prompt-v5
language: zh-CN
target_repo:
status: final
---
```

## 落盘规则

- 先运行脚本生成目标路径，再创建文件。
- 不把报告直接丢在仓库根目录。
- 不为单次调研额外创建 README、SUMMARY、META 等旁支文档，除非用户明确要求。
- 最终回复里必须给出实际保存路径。
