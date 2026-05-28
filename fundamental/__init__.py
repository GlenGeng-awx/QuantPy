"""
Download:
    python3 -m fundamental.download                 # 下载全部
    python3 -m fundamental.download AAPL            # 下载单只

Statements:
    python3 -m fundamental.statements               # 打印全部财报
    python3 -m fundamental.statements AAPL          # 打印单只财报

Cheap:
    python3 -m fundamental.cheap                    # 全量筛选 + ranking
    python3 -m fundamental.cheap AAPL               # 单只筛选

Health:
    python3 -m fundamental.health | pbcopy          # 全量评分 + ranking
    python3 -m fundamental.health AAPL              # 单只评分

Combine:
    python3 -m fundamental.combine                  # cheap + health 合并排行
    python3 -m fundamental.combine AAPL             # cheap 明细 + health 明细
"""
