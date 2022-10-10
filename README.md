# openconfigValidator

## Description

This project is a simple Python library calling a ygot based Go library.
It permits to benefit ygot feature from Python, as Pyangbind is not maintained anymore.

To optimize validation performance on runtime, the bindings are limited to a subset of openconfig tree.

## Update Openconfig bindings

Just run `update_bindings.sh`.

## Build Go library

To make the library available from Python, you just need to build it:

```
go build -buildmode=c-shared -o openconfig_validator.so openconfig_validator.go
```

This is imported in the Python lib like this:

```
import ctypes
import json

openconfig_validator = ctypes.cdll.LoadLibrary("./openconfig_validator.so")
oc_bgp_validator = openconfig_validator.validateBGP
oc_bgp_validator.argtypes = [ctypes.c_char_p]
```

Use it like this:

```
oc_bgp_validator(json_string)
```

This part is abstracted by the library

## Usage
