from okf_hermes_bridge import KnowledgeGraph, build_hermes_context


def test_graph_follows_related_concept():
    graph = KnowledgeGraph.load("sample-bundle")
    results = graph.retrieve("배포 실패 시 어떻게 처리합니까?", max_nodes=2)
    assert [item.concept_id for item in results] == [
        "playbooks/deploy.md", "playbooks/rollback.md"
    ]


def test_hermes_payload_is_bounded_and_attributed():
    graph = KnowledgeGraph.load("sample-bundle")
    payload = build_hermes_context(graph, "배포 실패", max_nodes=2)
    assert set(payload) == {"context"}
    assert "playbooks/deploy.md" in payload["context"]
    assert "playbooks/rollback.md" in payload["context"]
    assert "index.md" not in payload["context"]
