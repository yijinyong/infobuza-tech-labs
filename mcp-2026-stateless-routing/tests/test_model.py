from mcp_routing_lab.model import StatelessWorker, build_self_describing_request


def test_self_describing_request_is_accepted():
    assert StatelessWorker("a").call(build_self_describing_request())


def test_missing_meta_is_rejected():
    request = build_self_describing_request()
    del request["params"]["_meta"]
    assert not StatelessWorker("a").call(request)


def test_wrong_protocol_version_is_rejected():
    request = build_self_describing_request()
    request["params"]["_meta"]["io.modelcontextprotocol/protocolVersion"] = "2025-11-25"
    assert not StatelessWorker("a").call(request)
