#!/bin/bash

python -m grpc_tools.protoc -I ../korhal-java-server/src/main/proto --python_out=. --grpc_python_out=. ../korhal-java-server/src/main/proto/korhal.proto
