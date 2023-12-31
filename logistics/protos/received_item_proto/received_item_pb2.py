# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logistics/protos/received_item_proto/received_item.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='logistics/protos/received_item_proto/received_item.proto',
  package='received_item',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8logistics/protos/received_item_proto/received_item.proto\x12\rreceived_item\x1a\x1bgoogle/protobuf/empty.proto\"\x94\x02\n\x0cReceivedItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x12\n\nproduct_id\x18\x04 \x01(\t\x12\x14\n\x0cproduct_name\x18\x05 \x01(\t\x12\x18\n\x10product_brand_id\x18\x06 \x01(\t\x12\x1a\n\x12product_brand_name\x18\x07 \x01(\t\x12\x14\n\x0cproduct_size\x18\x08 \x01(\t\x12\x15\n\rproduct_color\x18\t \x01(\t\x12\x12\n\ncreated_at\x18\n \x01(\t\x12\x12\n\nupdated_at\x18\x0b \x01(\t\x12\x12\n\ndeleted_at\x18\x0c \x01(\t\x12\x11\n\tinventory\x18\r \x01(\x03\"\x19\n\x17ReceivedItemListRequest\")\n\x1bReceivedItemRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\x8e\x03\n\x16ReceivedItemController\x12O\n\x04List\x12&.received_item.ReceivedItemListRequest\x1a\x1b.received_item.ReceivedItem\"\x00\x30\x01\x12\x44\n\x06\x43reate\x12\x1b.received_item.ReceivedItem\x1a\x1b.received_item.ReceivedItem\"\x00\x12U\n\x08Retrieve\x12*.received_item.ReceivedItemRetrieveRequest\x1a\x1b.received_item.ReceivedItem\"\x00\x12\x44\n\x06Update\x12\x1b.received_item.ReceivedItem\x1a\x1b.received_item.ReceivedItem\"\x00\x12@\n\x07\x44\x65stroy\x12\x1b.received_item.ReceivedItem\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_RECEIVEDITEM = _descriptor.Descriptor(
  name='ReceivedItem',
  full_name='received_item.ReceivedItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='received_item.ReceivedItem.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='received_item.ReceivedItem.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='received_item.ReceivedItem.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='received_item.ReceivedItem.product_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_name', full_name='received_item.ReceivedItem.product_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_brand_id', full_name='received_item.ReceivedItem.product_brand_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_brand_name', full_name='received_item.ReceivedItem.product_brand_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_size', full_name='received_item.ReceivedItem.product_size', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_color', full_name='received_item.ReceivedItem.product_color', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='received_item.ReceivedItem.created_at', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='received_item.ReceivedItem.updated_at', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted_at', full_name='received_item.ReceivedItem.deleted_at', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inventory', full_name='received_item.ReceivedItem.inventory', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=381,
)


_RECEIVEDITEMLISTREQUEST = _descriptor.Descriptor(
  name='ReceivedItemListRequest',
  full_name='received_item.ReceivedItemListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=408,
)


_RECEIVEDITEMRETRIEVEREQUEST = _descriptor.Descriptor(
  name='ReceivedItemRetrieveRequest',
  full_name='received_item.ReceivedItemRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='received_item.ReceivedItemRetrieveRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=451,
)

DESCRIPTOR.message_types_by_name['ReceivedItem'] = _RECEIVEDITEM
DESCRIPTOR.message_types_by_name['ReceivedItemListRequest'] = _RECEIVEDITEMLISTREQUEST
DESCRIPTOR.message_types_by_name['ReceivedItemRetrieveRequest'] = _RECEIVEDITEMRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReceivedItem = _reflection.GeneratedProtocolMessageType('ReceivedItem', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEDITEM,
  '__module__' : 'logistics.protos.received_item_proto.received_item_pb2'
  # @@protoc_insertion_point(class_scope:received_item.ReceivedItem)
  })
_sym_db.RegisterMessage(ReceivedItem)

ReceivedItemListRequest = _reflection.GeneratedProtocolMessageType('ReceivedItemListRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEDITEMLISTREQUEST,
  '__module__' : 'logistics.protos.received_item_proto.received_item_pb2'
  # @@protoc_insertion_point(class_scope:received_item.ReceivedItemListRequest)
  })
_sym_db.RegisterMessage(ReceivedItemListRequest)

ReceivedItemRetrieveRequest = _reflection.GeneratedProtocolMessageType('ReceivedItemRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEDITEMRETRIEVEREQUEST,
  '__module__' : 'logistics.protos.received_item_proto.received_item_pb2'
  # @@protoc_insertion_point(class_scope:received_item.ReceivedItemRetrieveRequest)
  })
_sym_db.RegisterMessage(ReceivedItemRetrieveRequest)



_RECEIVEDITEMCONTROLLER = _descriptor.ServiceDescriptor(
  name='ReceivedItemController',
  full_name='received_item.ReceivedItemController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=454,
  serialized_end=852,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='received_item.ReceivedItemController.List',
    index=0,
    containing_service=None,
    input_type=_RECEIVEDITEMLISTREQUEST,
    output_type=_RECEIVEDITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='received_item.ReceivedItemController.Create',
    index=1,
    containing_service=None,
    input_type=_RECEIVEDITEM,
    output_type=_RECEIVEDITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='received_item.ReceivedItemController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_RECEIVEDITEMRETRIEVEREQUEST,
    output_type=_RECEIVEDITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='received_item.ReceivedItemController.Update',
    index=3,
    containing_service=None,
    input_type=_RECEIVEDITEM,
    output_type=_RECEIVEDITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='received_item.ReceivedItemController.Destroy',
    index=4,
    containing_service=None,
    input_type=_RECEIVEDITEM,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECEIVEDITEMCONTROLLER)

DESCRIPTOR.services_by_name['ReceivedItemController'] = _RECEIVEDITEMCONTROLLER

# @@protoc_insertion_point(module_scope)
