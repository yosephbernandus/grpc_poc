# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: application.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'application.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61pplication.proto\",\n\x12\x41pplicationRequest\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\x03\"#\n\x13\x41pplicationResponse\x12\x0c\n\x04name\x18\x01 \x01(\t2T\n\x12\x41pplicationService\x12>\n\x0f\x41pplicationData\x12\x13.ApplicationRequest\x1a\x14.ApplicationResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'application_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_APPLICATIONREQUEST']._serialized_start=21
  _globals['_APPLICATIONREQUEST']._serialized_end=65
  _globals['_APPLICATIONRESPONSE']._serialized_start=67
  _globals['_APPLICATIONRESPONSE']._serialized_end=102
  _globals['_APPLICATIONSERVICE']._serialized_start=104
  _globals['_APPLICATIONSERVICE']._serialized_end=188
# @@protoc_insertion_point(module_scope)
