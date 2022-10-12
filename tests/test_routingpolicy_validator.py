import pytest

from openconfig_validator.main import RoutingPolicyValidator
from openconfig_validator.validation_exceptions import \
    OpenconfigValidationError

routing_policy_data_valid = {
    "policy-definitions": {
        "policy-definition": [
            {
                "name": "RM-FABRIC-IN",
                "config": {"name": "RM-FABRIC-IN"},
                "statements": {
                    "statement": [
                        {
                            "actions": {"config": {"policy-result": "ACCEPT_ROUTE"}},
                            "config": {"name": "10"},
                            "name": "10",
                        }
                    ]
                },
            },
            {
                "name": "RM-FABRIC-OUT",
                "config": {"name": "RM-FABRIC-OUT"},
                "statements": {
                    "statement": [
                        {
                            "actions": {"config": {"policy-result": "ACCEPT_ROUTE"}},
                            "config": {"name": "10"},
                            "name": "10",
                        }
                    ]
                },
            },
        ]
    }
}

routing_policy_data_invalid = {
    "policy-definitions": {
        "policy-definition": [
            {
                "name": "RM-FABRIC-IN",
                "config": {"name": "RM-WHATEVER"},  # name is different
                "statements": {
                    "statement": [
                        {
                            "actions": {"config": {"policy-result": "ACCEPT_ROUTE"}},
                            "config": {"name": "10"},
                            "name": "10",
                        }
                    ]
                },
            },
            {
                "name": "RM-FABRIC-OUT",
                "config": {"name": "RM-FABRIC-OUT"},
                "statements": {
                    "statement": [
                        {
                            "actions": {"config": {"policy-result": "ACCEPT_ROUTE"}},
                            "config": {"name": "10"},
                            "name": "10",
                        }
                    ]
                },
            },
        ]
    }
}


def test__rpol_validator__valid_data():
    rp_val = RoutingPolicyValidator()
    is_valid = rp_val.validate(routing_policy_data_valid)

    assert is_valid == True


def test__rpol_validator__invalid_data():
    rp_val = RoutingPolicyValidator()
    with pytest.raises(OpenconfigValidationError):
        rp_val.validate(routing_policy_data_invalid)
