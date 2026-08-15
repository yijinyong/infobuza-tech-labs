from pathlib import Path

from okf_hermes_bridge import KnowledgeGraph, build_hermes_context

BUNDLE = Path(__file__).resolve().parents[1] / "sample-bundle"


def test_graph_follows_related_concept():
    graph = KnowledgeGraph.load(BUNDLE)
    results = graph.retrieve("배포 실패 시 어떻게 처리합니까?", max_nodes=2)
    assert [item.concept_id for item in results] == [
        "playbooks/deploy.md", "playbooks/rollback.md"
    ]


def test_hermes_payload_is_bounded_and_attributed():
    graph = KnowledgeGraph.load(BUNDLE)
    payload = build_hermes_context(graph, "배포 실패", max_nodes=2)
    assert set(payload) == {"context", "metadata"}
    assert "playbooks/deploy.md" in payload["context"]
    assert "playbooks/rollback.md" in payload["context"]
    assert "index.md" not in payload["context"]
    assert payload["metadata"]["concept_ids"] == [
        "playbooks/deploy.md", "playbooks/rollback.md"
    ]


def test_work_onboarding_follows_access_policy():
    graph = KnowledgeGraph.load(BUNDLE)
    results = graph.retrieve("신규 입사자 저장소 권한 신청", max_nodes=2)
    assert [item.concept_id for item in results] == [
        "people/onboarding.md", "people/access.md"
    ]


def test_life_scenario_follows_filter_instructions():
    graph = KnowledgeGraph.load(BUNDLE)
    results = graph.retrieve("정수기 필터 교체 알림", max_nodes=2)
    assert [item.concept_id for item in results] == [
        "home/water-filter.md", "home/replace-filter.md"
    ]


def test_policy_rejects_unbounded_context():
    graph = KnowledgeGraph.load(BUNDLE)
    try:
        build_hermes_context(graph, "배포", max_nodes=100)
    except ValueError as exc:
        assert "max_nodes" in str(exc)
    else:
        raise AssertionError("unsafe max_nodes must be rejected")
