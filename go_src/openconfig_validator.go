package main

import (
	"C"

	oc_bindings "openconfig_validator/bindings"
)
import (
	"flag"
)

//export isValidBGP
func isValidBGP(documentPtr *C.char) *C.char {
	flag.Parse()
	documentString := C.GoString(documentPtr)

	test := []byte(documentString)
	if test == nil {
		return C.CString("empty string")
	}

	bgp := &oc_bindings.NetworkInstance_Protocol_Bgp{}
	if bgp == nil {
		return C.CString("error while instantiating openconfig struct")
	}
	if err := oc_bindings.Unmarshal([]byte(documentString), bgp); err != nil {
		return C.CString(err.Error())
	}

	err := bgp.Validate()
	if err != nil {
		return C.CString(err.Error())
	}
	return nil
}

//export isValidRoutingPolicy
func isValidRoutingPolicy(documentPtr *C.char) *C.char {
	flag.Parse()
	documentString := C.GoString(documentPtr)

	test := []byte(documentString)
	if test == nil {
		return C.CString("empty string")
	}

	rPol := &oc_bindings.RoutingPolicy{}
	if rPol == nil {
		return C.CString("error while instantiating openconfig struct")
	}
	if err := oc_bindings.Unmarshal([]byte(documentString), rPol); err != nil {
		return C.CString(err.Error())
	}

	err := rPol.Validate()
	if err != nil {
		return C.CString(err.Error())
	}
	return nil
}

func main() {
}
