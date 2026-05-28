---
concept: Design.md
slug: design-md
type: share
language: zh-CN
created_at: 2026-05-18
based_on: reports/2026-05-08-deep-dive.md
platform: x.com / linkedin
---

# 设计师的新画布：读完 Google DESIGN.md 之后

20 年来我第一次怀疑「UX 设计师」这个职位还能不能继续存在。

不是因为 AI 抢了我的活，是因为我自己越来越少打开 Figma 了。

我正在做自己的产品 Cap4u（一个帮非英语母语者打英文客服电话的 iOS App），日常工作变成写 Markdown、配合 Claude Code、改 AI 生成的代码。Figma 文件越来越像「画给自己看的中间产物」，而不是「真有人按它实现」。

我心里慢慢冒出来一个念头：作为设计师，我对产品视觉的「全局控制」是不是正在悄悄丢失？

直到我看到 Google Labs 在 2026 年 4 月开源了一个叫 `DESIGN.md` 的东西。

---

## 1. 这不是「又一个工具」

第一眼我以为这又是某种 design system 框架，差点关掉。仔细读完 spec 才意识到：这不是工具，而是一种**协议**。

它定义了一份 Markdown 文件的标准格式：

- 前半部分是机器读的 YAML（颜色、字体、间距、组件 token）
- 后半部分是人读的 Markdown（设计 rationale、do's and don'ts）

一份文件，同时给 designer 和 AI agent 读。你写一次，Claude Code、Cursor、Google Stitch，或者任何后续的 AI 工具，都能按这份文件生成符合品牌的 UI。

简单到让人怀疑：就这？

---

## 2. 这件事是一波趋势的一部分

往后退一步看，DESIGN.md 不是孤立的。它属于 2025-2026 年这一波「AI 工程文档协议」浪潮：

```text
AGENTS.md     2025-12，OpenAI / Google / Cursor 联合制定，已捐给 Linux Foundation
              -> agent 在我这个仓库里能做什么、不能做什么

SKILL.md      Anthropic / Agent Skills 标准
              -> agent 应该按什么步骤完成某类任务

DESIGN.md     2026-04，Google Labs
              -> agent 应该按什么样的视觉语言生成 UI

program.md    2026-03，Karpathy autoresearch
              -> agent 应该按什么纪律跑实验循环
```

这一波的共同特征：**人写 Markdown，agent 读 Markdown，工具链做校验**。

我们正从 2024 年「让 AI 看 Figma 截图猜风格」的混乱，过渡到 2026 年「让 AI 读结构化设计协议」的纪律。

---

## 3. 一个反直觉的发现：Cap4u 已经在做这件事

读完 spec 后，我顺手翻了一下自己 Cap4u 的仓库，发现一件连自己也意外的事。

我的 `.vibe-doc/design-token.json`（170 行）+ `design-system.md`（v1.3）+ `.agents/rules/shared/design-defaults.md` 三个文件加起来，**比 DESIGN.md alpha 当前的 spec 还要完整**。

DESIGN.md 当前缺三样东西，Cap4u 都已经有了：

| 维度 | DESIGN.md alpha | Cap4u |
|---|---|---|
| Negative Defaults（禁止做什么）| ✗ | ✓ |
| Appearance Policy（system / fixedLight）| ✗ | ✓ |
| Decision Order（设计冲突时优先级）| ✗ | ✓ |

我一直以为自己是「被 AI 时代推着往前走」的设计师，结果发现，我（在 Codex / Claude Code 协助下）已经提前 6 个月独立摸索出了 DESIGN.md 标准里还没收敛的几层约束。

这件事让我重新理解了 UX 设计师在 AI 时代的位置。

---

## 4. 设计师不会消失，只是换了画布

读完 DESIGN.md 后，我有一个判断：

```text
正在消失：
  Figma 操作员（画 mock 给开发者翻译）
  把品牌指南 PDF 写漂亮的人
  只在工具内部做装饰的人

正在涌现：
  能读 / 写 DESIGN.md 这种协议的设计师
  能维护「禁止做什么」规则的设计师
  能在 AGENTS.md 里定 agent 行为边界的设计师

简言之：
  设计师不再是「画图的人」，是「定规则的人」。
```

这件事对我个人意味着：**过去 10 年在 Figma 里做 design system 的能力，完全可以迁移到 DESIGN.md。技能没消失，只是载体变了**。

从 Figma 文件到 DESIGN.md，从拖动矩形到写 token references，本质上都是同一件事：**用结构化的方式表达「这个产品应该长什么样」**。

---

## 5. 几条可以带走的 Takeaways

写完这篇我自己留了一份清单。如果你只看这一段，至少把这七条带走：

**1. DESIGN.md 不是一份新文档，而是「设计的载体从图变成规则」**
过去 10 年在 Figma 里做的事不会消失，只是换了表达媒介。从 Figma 文件 → DESIGN.md，技能完全可迁移。

**2. 写 DESIGN.md 之前，先写一段「气质 prompt」**
跳过气质直接让 AI 做 DESIGN.md，会得到一份「正确但乏味」的产物。先用 5-10 行写清楚你要什么气质、不要什么气质（比如「绝对避免蓝紫渐变 / cyan-on-dark / 玻璃拟态」），再让 AI 提案。

**3. 跨平台产品不要用 H1 / H2 这种 Web 话术命名 token**
用 `display-large / headline-medium / body-medium` 这种语义命名。H1 是 HTML 的话术，iOS 没有；iOS 的 `largeTitle`，Web 也没有。每个平台再做一层映射。

**4. 严格执行靠 5 层互相补漏，不是某一层做到极致**
`agent 必读 → 运行时强约束 → CI lint → 视觉回归 → code review`。缺一层都会被绕过。最高 ROI 的一步：把 `npx @google/design.md lint` 接到 CI，2 小时工作量，长期价值。

**5. AI 时代 DESIGN.md 是设计师的新 canvas，不是事后总结**
旧流程：Figma → 设计系统 → 代码（DESIGN.md 是 after-the-fact 文档）。
新流程：DESIGN.md → AI 生成 UI → 审查 → 改 DESIGN.md（DESIGN.md 是设计师的主要 canvas）。
这种倒置正在悄悄发生，但很少有人显式化它。

**6. DESIGN.md alpha 在 Dark Mode 和 Negative Defaults 上还没收敛**
不要等 spec 告诉你怎么做这两件事——你自己定。Cap4u 用 `color.light.* / color.dark.* / liveCallAdaptive.*` 三套 namespace 表达 Dark Mode，比 spec 当前做法更工程化。

**7. UX 设计师不会消失，但会变形**
不再是「画图的人」，而是「定规则的人」。具体要做的事：把 token / rationale / negative defaults / decision order / runtime SSOT 这五层都写出来。任何一层缺失，AI 都会替你随便发挥。

---

## 6. 收尾

读 DESIGN.md 之前，我担心 AI Coding 时代的设计会变得越来越「松散」、越来越「不可控」。

读完之后，我反而比之前更乐观：**结构化的设计协议第一次让设计师可以一次定下「全局且持久」的视觉契约**，让 AI agent 跨 session、跨工具、跨平台都按这份契约执行。这件事在 Figma 时代是不可能的。

如果你手上也有一份 Figma 文件或者一组散落的 token，建议这个周末花 2 小时干一件事：把它整理成一份 DESIGN.md，放在仓库根目录。

参考起点：

- 官方 spec：`github.com/google-labs-code/design.md`
- 公开样本：`designmd.app`（已收录 454 个公开 design system）
- 社区精选：`github.com/VoltAgent/awesome-design-md`

也想听听：你的 AI Coding 工作流里，设计这块现在是怎么管的？欢迎留言。

再聊。
