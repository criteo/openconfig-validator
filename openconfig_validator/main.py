import ctypes
import json
import os
from sys import platform

from .validation_exceptions import OpenconfigValidationError


class CtypesLib:
    def __init__(self, fp_lib, dependencies=[]):
        self._dependencies = [CtypesLib(fp_dep) for fp_dep in dependencies]

        if platform == "linux" or platform == "linux2":  # Linux
            self._dlclose_func = ctypes.cdll.LoadLibrary("").dlclose
            self._dlclose_func.argtypes = [ctypes.c_void_p]

            self._ctypes_lib = ctypes.cdll.LoadLibrary(fp_lib)
        elif platform == "win32":  # Windows
            self._ctypes_lib = ctypes.WinDLL(fp_lib)

        # To avoid memory leak due to CString conversion on GO side
        self.free = self._ctypes_lib.free
        self.free.argtypes = [ctypes.c_void_p]

        self._handle = self._ctypes_lib._handle

    def __getattr__(self, attr):
        return self._ctypes_lib.__getattr__(attr)

    def __del__(self):
        for dep in self._dependencies:
            del dep

        del self._ctypes_lib

        if platform == "linux" or platform == "linux2":  # Linux
            self._dlclose_func(self._handle)
        elif platform == "win32":  # Windows
            ctypes.windll.kernel32.FreeLibrary(self._handle)


class OpenconfigValidator:
    validator: ctypes.CDLL

    def __init__(self):
        self.yang_validator = CtypesLib(
            f"{os.path.dirname(__file__)}/bin/openconfig_validator.so", []
        )

    def post_init(self):
        self.validator.argtypes = [ctypes.c_char_p]

    def validate(self, openconfig):
        openconfig_json = json.dumps(openconfig)
        result = self.validator(openconfig_json.encode("utf-8"))

        if result == 0:
            return True

        error = ctypes.string_at(result)

        # free memory from CString conversion
        self.yang_validator.free(result)

        raise OpenconfigValidationError(error.decode("utf-8"))


class BgpValidator(OpenconfigValidator):
    def __init__(self):
        super().__init__()
        self.validator = self.yang_validator.isValidBGP
        self.post_init()


class RoutingPolicyValidator(OpenconfigValidator):
    def __init__(self):
        super().__init__()
        self.validator = self.yang_validator.isValidRoutingPolicy
        self.post_init()
