import pytest
import gameplay.leaderboard_rank as mod

CASES = [
    ("server_validate", (1, 2)),
    ("tie_rank", (100, 100)),
    ("season_clean", (1, 2)),
    ("cache_invalidate", (1, 2)),
    ("cursor_page", (10, 2)),
    ("cheat_filter", (1, 2)),
    ("settle_timezone", (8, 2)),
    ("account_map", (1, 2)),
    ("integer_display", (12345, 3)),
    ("my_rank", (1, 2)),
    ("score_clamp", (0, 1000000)),
    ("board_limit", (100, 2)),
    ("refresh_interval", (30, 10)),
    ("rank_delta", (5, 3)),
    ("entry_merge", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
