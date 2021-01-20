# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notification.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='notification.proto',
  package='threemon',
  syntax='proto3',
  serialized_options=_b('H\002'),
  serialized_pb=_b('\n\x12notification.proto\x12\x08threemon\"D\n\x0cNotification\x12\n\n\x02ts\x18\x02 \x01(\r\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.threemon.NotificationType*,\n\x10NotificationType\x12\n\n\x06NoPids\x10\x00\x12\x0c\n\x08\x46inished\x10\x01\x42\x02H\x02\x62\x06proto3')
)

_NOTIFICATIONTYPE = _descriptor.EnumDescriptor(
  name='NotificationType',
  full_name='threemon.NotificationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoPids', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Finished', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=102,
  serialized_end=146,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONTYPE)

NotificationType = enum_type_wrapper.EnumTypeWrapper(_NOTIFICATIONTYPE)
NoPids = 0
Finished = 1



_NOTIFICATION = _descriptor.Descriptor(
  name='Notification',
  full_name='threemon.Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ts', full_name='threemon.Notification.ts', index=0,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='threemon.Notification.type', index=1,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=32,
  serialized_end=100,
)

_NOTIFICATION.fields_by_name['type'].enum_type = _NOTIFICATIONTYPE
DESCRIPTOR.message_types_by_name['Notification'] = _NOTIFICATION
DESCRIPTOR.enum_types_by_name['NotificationType'] = _NOTIFICATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Notification = _reflection.GeneratedProtocolMessageType('Notification', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFICATION,
  __module__ = 'notification_pb2'
  # @@protoc_insertion_point(class_scope:threemon.Notification)
  ))
_sym_db.RegisterMessage(Notification)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)