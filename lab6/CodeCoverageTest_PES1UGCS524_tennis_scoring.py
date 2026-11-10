"""Exercise each scoring outcome in the assigned tennis application."""

import pytest
from tennis_scoring import game_score, match_status, set_winner


@pytest.mark.parametrize(("a", "b", "expected"), [
    (0, 0, "0-0"), (2, 3, "30-40"), (3, 3, "deuce"),
    (5, 3, "game A"), (3, 5, "game B"), (4, 3, "advantage A"),
    (3, 4, "advantage B"), (4, 2, "game A"), (2, 4, "game B"),
])
def test_game_scores(a, b, expected):
    assert game_score(a, b) == expected


def test_game_rejects_negative_points():
    with pytest.raises(ValueError, match="negative points"):
        game_score(-1, 0)


@pytest.mark.parametrize(("a", "b", "expected"), [
    (6, 4, "A"), (4, 6, "B"), (7, 6, "A"), (6, 7, "B"),
    (3, 2, None), (6, 5, None),
])
def test_set_winners(a, b, expected):
    assert set_winner(a, b) == expected


@pytest.mark.parametrize(("a", "b", "best_of", "expected"), [
    (2, 1, 3, "A wins"), (1, 2, 3, "B wins"),
    (1, 1, 3, "decider"), (1, 0, 3, "in progress"),
])
def test_match_status(a, b, best_of, expected):
    assert match_status(a, b, best_of) == expected
