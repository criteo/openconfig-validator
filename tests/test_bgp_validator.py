import pytest

from openconfig_validator.main import BgpValidator
from openconfig_validator.validation_exceptions import \
    OpenconfigValidationError

bgp_data_valid = {
    "openconfig-bgp:neighbors": {
        "neighbor": [
            {
                "apply-policy": {"config": {"export-policy": ["out"], "import-policy": ["in"]}},
                "config": {
                    "peer-as": 65001,
                    "local-as": 65000,
                    "peer-type": None,
                    "auth-password": "secret",
                    "remove-private-as": None,
                    "send-community": "NONE",
                    "description": "to:device2",
                    "peer-group": "PG-TEST",
                    "neighbor-address": "192.0.2.1",
                    "enabled": True,
                },
                "afi-safis": {
                    "afi-safi": [
                        {
                            "ipv6-unicast": None,
                            "ipv4-unicast": {
                                "prefix-limit": {
                                    "config": {
                                        "max-prefixes": 100,
                                        "prevent-teardown": False,
                                        "warning-threshold-pct": None,
                                        "restart-timer": None,
                                    }
                                }
                            },
                            "config": {
                                "afi-safi-name": "IPV4_UNICAST",
                                "enabled": True,
                            },
                            "afi-safi-name": "IPV4_UNICAST",
                        }
                    ]
                },
                "neighbor-address": "192.0.2.1",
            }
        ]
    }
}

bgp_data_invalid = {
    "openconfig-bgp:neighbors": {
        "neighbor": [
            {
                "apply-policy": {"config": {"export-policy": ["out"], "import-policy": ["in"]}},
                "config": {
                    "peer-as": "toto",  # str instead of a int
                    "local-as": 65000,
                    "peer-type": None,
                    "auth-password": "secret",
                    "remove-private-as": None,
                    "send-community": "NONE",
                    "description": "to:device2",
                    "peer-group": "PG-TEST",
                    "neighbor-address": "192.0.2.1",
                    "enabled": True,
                },
                "afi-safis": {
                    "afi-safi": [
                        {
                            "ipv6-unicast": None,
                            "ipv4-unicast": {
                                "prefix-limit": {
                                    "config": {
                                        "max-prefixes": 100,
                                        "prevent-teardown": False,
                                        "warning-threshold-pct": None,
                                        "restart-timer": None,
                                    }
                                }
                            },
                            "config": {
                                "afi-safi-name": "IPV4_UNICAST",
                                "enabled": True,
                            },
                            "afi-safi-name": "IPV4_UNICAST",
                        }
                    ]
                },
                "neighbor-address": "192.0.2.1",
            }
        ]
    }
}


def test__bgp_validator__valid_data():
    rp_val = BgpValidator()
    is_valid = rp_val.validate(bgp_data_valid)

    assert is_valid == True


def test__bgp_validator__invalid_data():
    rp_val = BgpValidator()
    with pytest.raises(OpenconfigValidationError):
        rp_val.validate(bgp_data_invalid)
