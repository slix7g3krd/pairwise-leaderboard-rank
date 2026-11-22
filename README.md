# pairwise-leaderboard-rank

## 领域

游戏、图形与多媒体

## 主题

排行榜名次

## 说明

服务端校验、并列名次与游标分页。

初始状态下 `gameplay/leaderboard_rank.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
