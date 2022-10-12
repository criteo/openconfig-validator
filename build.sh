#!/bin/bash

set -x

cd go_src
go build -buildmode=c-shared -o ../openconfig_validator/bin/openconfig_validator.so openconfig_validator.go
