# Notes — 用户的协作习惯 (LLM 必读)

> 本文件 = 用户的 meta 层个人习惯, 与分析框架 (00_framework / 各层 doc) 分工: 框架管"分析怎么做", 本文件管"怎么跟我合作"。
> CLAUDE.md 已要求: **开工前必读本文**。 SESSION_LOG 里的流程判例是这些习惯的来处, 本文是终态。

## 可读性 (readable)

- **我写纯文本, 用户看 IDE 渲染后的 markdown — 时刻注意这个差异**, 且两套渲染规则不同: **普通段落**内单个换行被合并成同一行 (soft break) — 段内换行是无效功, 控制所见"行"的唯一手段 = 空行分段; **blockquote (`>`) 内**单个换行被保留 (连续 `>` 行 = 同段内多行) — 段内短句分行是有效写法, 分段用空 `>` 行 (L3 "大师说" 与 L1/L2 "先说结论" 是两类, 别套错)。写完自查要按渲染效果想象, 不是看源码。
- **一行不要太长** — 长句拆短; 论点。证据。含义。三口气, 禁嵌套四层; 普通段落在渲染里就是一行, 巨长行的修法 = 拆段或砍字 (blockquote 内则是拆 `>` 行)。
- **段与段之间显式空行** — md 的分段必须真实空行; blockquote 内语义段之间空 `>` 行。

## 文档维护 (docs 必须 up to date)

- **docs = 面向终态的当前 spec, 随时 ready for review** — 不做 append only 的堆叠式修改; 新信息进来 = 改写旧段落, 不是在下面追加。
- 历史/演化过程不进 doc: SESSION_LOG 归 LLM 自己管理, 用户不管; 但 doc 里不留历史机制描述、跨 doc 关系对照、"为什么没选 X" 类决策叙事 (终态三删)。
- **deco = 删除** — rm 不留 stub, doc 零过程残留, 用户视野看不到删除痕迹; 演化史只存 SESSION_LOG。
- 修改后必须自查格式 (节号连续 / 跨卡引用 grep / 孤儿残句 / 长度) — 低级格式错误会返工。
- **条目多到平铺难读时, 按问题/目标分组重组** — 每组 = 病或目标一句 + 具体措施 (参考 00 §0.1.5 三问题分组 / edge_cases 四节); 平铺列表是欠组织态, 不是终态。
- **用户报问题 = 隐含 docs 维护事件** — 动手修前先做影响盘点: SESSION_LOG 判例 / edge_cases 新 EC / 框架规则 / notes 习惯四处过一遍, 有落点先报用户裁再写; 修复与沉淀一体, 只修不沉淀 = 半途。

## 协作流程 (先 align 再动手)

- **先 brainstorm, 禁止一上来动手改东西** — 任何修改/新功能/重构, 先跟用户对齐问题与方案, 用户拍板后才执行。
- **docs 修改 = 先 diff 后落盘, 用户同意才能改** — docs 是最核心的工作产物; 任何落盘 (含单文件小改) 先给 diff, 用户 "OK/落/改" 之后才动手 — 用户口头认可方向 ≠ 认可落盘, 不能抢跑; notes / edge_cases / SESSION_LOG 本身也是 docs, 同受此规。
- **给 agenda 时单步执行** — 用户给 agenda = 做一步等 review; 抢跑连续执行多步 = 违规。后续步骤标 "(等你点头)"。
- 逐文件串行给 diff — 用户要看每个文件的改动 (vim -d 式对照), 批量 sed 之类操作必须先展示再执行。
- **"重跑 X" 的工作流 (盲跑协议)**: ① 先不管旧链 (X.date 归档链), 独立生成新链 — 不读旧版本; ② 生成完 diff 新旧两版 report, 差异 flag 给用户看; ③ 用户说 OK 才拿 diff 结论回去修改新链 — diff 前禁读归档链。
- **输出涉及多个文件时, 一个一个逐个落盘** — 禁一次生成/一次派发多文件 (浇筑基本原则; 主 agent 与 subagent 同规): 每写完一个文件 = 一个 checkpoint, 展示/验证后再写下一个。subagent 派发同样单文件粒度 — 批量任务 (一次 9 卡) 实测过载死掉, 逐卡派发才稳定。

## Git 纪律

- **commit 用户自己做, LLM 不 commit 不 push** — 不得污染用户的 git history。
- LLM 的工作产物 (spec/plan/草稿/临时文件) 放 tmp/ 或 docs.v2/specs|plans/ 并进 .gitignore, git 视野只剩用户文件。
- **subagent 浏览器产物不落仓库根** — playwright 快照的 filename 参数按相对路径解析到 workspace root (判例: 两个 snap_*.yml 落在根上被用户抓); 派发 prompt 里写明 "落盘一律 tmp/ 前缀"; 主 agent 每层收口后顺手 `git status` 扫一遍 untracked 防漏网。
- 误提交了 → 用户要求时 reset 干净, 工作区修改保留。
- **git 分层**: 用户资产 (knowledgeBase/) 入库; LLM 记忆 (SESSION_LOG) 与报告产物 (ai_report*/) 不入库。
- **transactions/book.py = 用户自维护, LLM 只读** — 持仓真相源的唯一写入权在用户; LLM 不得预填/代改行权、过期、成交记录 (发现缺口 = 报告用户, 等用户自己记)。
- **看持仓跑 `python3 -m transactions.portfolio`, 禁直接读 book.py 拿数** — book.py 只是原始记录; portfolio.py/position.py/types.py 才是逻辑, 输出才是精髓: 分币种 realized/unrealized/fees 汇总 + 持仓含 **cost(w/ options)** 有效成本 (权利金自动折入, 如 MU 行权 700 − 5 = 695 这类账它原生会算) + 各持仓下挂未平仓期权腿。直接读 book.py = 只见流水不见仓位语义。
