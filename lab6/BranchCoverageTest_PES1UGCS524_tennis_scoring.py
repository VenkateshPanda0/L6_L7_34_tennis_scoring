"""Exercise both sides and the boundaries of scoring decisions."""

import pytest
from tennis_scoring import game_score, match_status, set_winner


@pytest.mark.parametrize(("a", "b"), [(-1, 0), (0, -1)])
def test_negative_points_for_either_player(a, b):
    with pytest.raises(ValueError, match="negative points"):
        game_score(a, b)


@pytest.mark.parametrize(("a", "b", "expected"), [
    (0, 0, "0-0"), (2, 3, "30-40"), (3, 2, "40-30"),
    (3, 3, "deuce"), (5, 5, "deuce"),
    (5, 3, "game A"), (3, 5, "game B"), (4, 3, "advantage A"),
    (3, 4, "advantage B"), (4, 2, "game A"), (2, 4, "game B"),
])
def test_game_decisions(a, b, expected):
    assert game_score(a, b) == expected


@pytest.mark.parametrize(("a", "b", "expected"), [
    (5, 3, None), (3, 5, None), (6, 4, "A"), (4, 6, "B"),
    (6, 5, None), (5, 6, None), (6, 6, None), (7, 6, "A"), (6, 7, "B"),
    (7, 7, None), (8, 6, "A"), (6, 8, "B"),
])
def test_set_boundaries(a, b, expected):
    assert set_winner(a, b) == expected


@pytest.mark.parametrize(("a", "b", "best_of", "expected"), [
    (2, 1, 3, "A wins"), (1, 2, 3, "B wins"),
    (1, 1, 3, "decider"), (1, 0, 3, "in progress"),
    (0, 1, 3, "in progress"), (3, 2, 5, "A wins"),
    (2, 3, 5, "B wins"), (2, 2, 5, "decider"), (2, 1, 5, "in progress"),
])
def test_match_decisions(a, b, best_of, expected):
    assert match_status(a, b, best_of) == expected
