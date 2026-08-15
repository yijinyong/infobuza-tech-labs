import pytest

from mcp_routing_lab import run_comparison


def test_twenty_request_comparison_is_deterministic():
    result = run_comparison(20)
    assert result["legacy_round_robin_success"] == 10
    assert result["legacy_round_robin_failure"] == 10
    assert result["stateless_round_robin_success"] == 20
    assert result["stateless_round_robin_failure"] == 0


def test_odd_request_count_is_supported():
    result = run_comparison(5)
    assert result["legacy_round_robin_success"] == 3
    assert result["legacy_round_robin_failure"] == 2


def test_non_positive_request_count_is_rejected():
    with pytest.raises(ValueError):
        run_comparison(0)
