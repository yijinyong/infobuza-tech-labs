import pytest
from agent_safety_gate import ExecutionRequest,Policy,evaluate

def test_margin_calculation_is_read_only():
    d=evaluate(ExecutionRequest(runtime="python3",purpose="margin calculation"))
    assert d.allowed and d.sandbox_profile["network"]=="deny"

def test_research_network_is_denied_by_default():
    d=evaluate(ExecutionRequest(runtime="python3",network=True,purpose="research"))
    assert not d.allowed and "network_denied_by_default" in d.reasons

def test_explicit_research_profile_allows_network():
    d=evaluate(ExecutionRequest(runtime="python3",network=True,purpose="research"),Policy(allow_network=True))
    assert d.allowed

def test_home_budget_export_requires_write_profile():
    r=ExecutionRequest(runtime="python3",write_files=True,purpose="home budget")
    assert not evaluate(r).allowed
    assert evaluate(r,Policy(allow_write=True)).allowed

@pytest.mark.parametrize("exec_request,reason",[
    (ExecutionRequest(runtime="bash",purpose="x"),"runtime_not_allowed"),
    (ExecutionRequest(runtime="python3",reads_secrets=True,purpose="x"),"secret_access_never_allowed"),
    (ExecutionRequest(runtime="python3",timeout_seconds=60,purpose="x"),"timeout_exceeds_limit"),
    (ExecutionRequest(runtime="python3"),"purpose_required"),
])
def test_dangerous_requests_are_blocked(exec_request,reason):
    assert reason in evaluate(exec_request).reasons
