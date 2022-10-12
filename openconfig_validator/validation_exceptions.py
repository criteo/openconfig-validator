"""OpenconfigValidation exceptions."""


class OpenconfigValidationError(RuntimeError):
    """Validation exception."""

    def __init__(self, msg: str = "") -> None:
        """Initialize exception."""
        self.message = msg
        super().__init__(self.message)

    def __str__(self) -> str:
        """Customize string representation."""
        return f"{self.message}"
