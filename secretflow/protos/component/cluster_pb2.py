# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: secretflow/protos/component/cluster.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='secretflow/protos/component/cluster.proto',
  package='secretflow.component',
  syntax='proto3',
  serialized_options=b'\n\036org.secretflow.proto.component',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)secretflow/protos/component/cluster.proto\x12\x14secretflow.component\"\xcf\x02\n\rSFClusterDesc\x12\x12\n\nsf_version\x18\x01 \x01(\t\x12\x12\n\npy_version\x18\x02 \x01(\t\x12\x0f\n\x07parties\x18\x03 \x03(\t\x12?\n\x07\x64\x65vices\x18\x04 \x03(\x0b\x32..secretflow.component.SFClusterDesc.DeviceDesc\x12H\n\x0eray_fed_config\x18\x05 \x01(\x0b\x32\x30.secretflow.component.SFClusterDesc.RayFedConfig\x1aI\n\nDeviceDesc\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07parties\x18\x03 \x03(\t\x12\x0e\n\x06\x63onfig\x18\x04 \x01(\t\x1a/\n\x0cRayFedConfig\x12\x1f\n\x17\x63ross_silo_comm_backend\x18\x01 \x01(\t\"\x7f\n\rStorageConfig\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x43\n\x08local_fs\x18\x02 \x01(\x0b\x32\x31.secretflow.component.StorageConfig.LocalFSConfig\x1a\x1b\n\rLocalFSConfig\x12\n\n\x02wd\x18\x01 \x01(\t\"\x9f\x05\n\x0fSFClusterConfig\x12\x31\n\x04\x64\x65sc\x18\x01 \x01(\x0b\x32#.secretflow.component.SFClusterDesc\x12I\n\rpublic_config\x18\x02 \x01(\x0b\x32\x32.secretflow.component.SFClusterConfig.PublicConfig\x12K\n\x0eprivate_config\x18\x03 \x01(\x0b\x32\x33.secretflow.component.SFClusterConfig.PrivateConfig\x1aL\n\x0cRayFedConfig\x12\x0f\n\x07parties\x18\x01 \x03(\t\x12\x11\n\taddresses\x18\x02 \x03(\t\x12\x18\n\x10listen_addresses\x18\x03 \x03(\t\x1aW\n\tSPUConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07parties\x18\x02 \x03(\t\x12\x11\n\taddresses\x18\x03 \x03(\t\x12\x18\n\x10listen_addresses\x18\x04 \x03(\t\x1a\xa0\x01\n\x0cPublicConfig\x12J\n\x0eray_fed_config\x18\x01 \x01(\x0b\x32\x32.secretflow.component.SFClusterConfig.RayFedConfig\x12\x44\n\x0bspu_configs\x18\x02 \x03(\x0b\x32/.secretflow.component.SFClusterConfig.SPUConfig\x1aw\n\rPrivateConfig\x12\x12\n\nself_party\x18\x01 \x01(\t\x12\x15\n\rray_head_addr\x18\x02 \x01(\t\x12;\n\x0estorage_config\x18\x03 \x01(\x0b\x32#.secretflow.component.StorageConfigB \n\x1eorg.secretflow.proto.componentb\x06proto3'
)




_SFCLUSTERDESC_DEVICEDESC = _descriptor.Descriptor(
  name='DeviceDesc',
  full_name='secretflow.component.SFClusterDesc.DeviceDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='secretflow.component.SFClusterDesc.DeviceDesc.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='secretflow.component.SFClusterDesc.DeviceDesc.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parties', full_name='secretflow.component.SFClusterDesc.DeviceDesc.parties', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='secretflow.component.SFClusterDesc.DeviceDesc.config', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=281,
  serialized_end=354,
)

_SFCLUSTERDESC_RAYFEDCONFIG = _descriptor.Descriptor(
  name='RayFedConfig',
  full_name='secretflow.component.SFClusterDesc.RayFedConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cross_silo_comm_backend', full_name='secretflow.component.SFClusterDesc.RayFedConfig.cross_silo_comm_backend', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=356,
  serialized_end=403,
)

_SFCLUSTERDESC = _descriptor.Descriptor(
  name='SFClusterDesc',
  full_name='secretflow.component.SFClusterDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sf_version', full_name='secretflow.component.SFClusterDesc.sf_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='py_version', full_name='secretflow.component.SFClusterDesc.py_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parties', full_name='secretflow.component.SFClusterDesc.parties', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='devices', full_name='secretflow.component.SFClusterDesc.devices', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ray_fed_config', full_name='secretflow.component.SFClusterDesc.ray_fed_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SFCLUSTERDESC_DEVICEDESC, _SFCLUSTERDESC_RAYFEDCONFIG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=403,
)


_STORAGECONFIG_LOCALFSCONFIG = _descriptor.Descriptor(
  name='LocalFSConfig',
  full_name='secretflow.component.StorageConfig.LocalFSConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='wd', full_name='secretflow.component.StorageConfig.LocalFSConfig.wd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=505,
  serialized_end=532,
)

_STORAGECONFIG = _descriptor.Descriptor(
  name='StorageConfig',
  full_name='secretflow.component.StorageConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='secretflow.component.StorageConfig.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='local_fs', full_name='secretflow.component.StorageConfig.local_fs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STORAGECONFIG_LOCALFSCONFIG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=532,
)


_SFCLUSTERCONFIG_RAYFEDCONFIG = _descriptor.Descriptor(
  name='RayFedConfig',
  full_name='secretflow.component.SFClusterConfig.RayFedConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parties', full_name='secretflow.component.SFClusterConfig.RayFedConfig.parties', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addresses', full_name='secretflow.component.SFClusterConfig.RayFedConfig.addresses', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='listen_addresses', full_name='secretflow.component.SFClusterConfig.RayFedConfig.listen_addresses', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=757,
  serialized_end=833,
)

_SFCLUSTERCONFIG_SPUCONFIG = _descriptor.Descriptor(
  name='SPUConfig',
  full_name='secretflow.component.SFClusterConfig.SPUConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='secretflow.component.SFClusterConfig.SPUConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parties', full_name='secretflow.component.SFClusterConfig.SPUConfig.parties', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addresses', full_name='secretflow.component.SFClusterConfig.SPUConfig.addresses', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='listen_addresses', full_name='secretflow.component.SFClusterConfig.SPUConfig.listen_addresses', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=835,
  serialized_end=922,
)

_SFCLUSTERCONFIG_PUBLICCONFIG = _descriptor.Descriptor(
  name='PublicConfig',
  full_name='secretflow.component.SFClusterConfig.PublicConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ray_fed_config', full_name='secretflow.component.SFClusterConfig.PublicConfig.ray_fed_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spu_configs', full_name='secretflow.component.SFClusterConfig.PublicConfig.spu_configs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=925,
  serialized_end=1085,
)

_SFCLUSTERCONFIG_PRIVATECONFIG = _descriptor.Descriptor(
  name='PrivateConfig',
  full_name='secretflow.component.SFClusterConfig.PrivateConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='self_party', full_name='secretflow.component.SFClusterConfig.PrivateConfig.self_party', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ray_head_addr', full_name='secretflow.component.SFClusterConfig.PrivateConfig.ray_head_addr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storage_config', full_name='secretflow.component.SFClusterConfig.PrivateConfig.storage_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1087,
  serialized_end=1206,
)

_SFCLUSTERCONFIG = _descriptor.Descriptor(
  name='SFClusterConfig',
  full_name='secretflow.component.SFClusterConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='desc', full_name='secretflow.component.SFClusterConfig.desc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_config', full_name='secretflow.component.SFClusterConfig.public_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='private_config', full_name='secretflow.component.SFClusterConfig.private_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SFCLUSTERCONFIG_RAYFEDCONFIG, _SFCLUSTERCONFIG_SPUCONFIG, _SFCLUSTERCONFIG_PUBLICCONFIG, _SFCLUSTERCONFIG_PRIVATECONFIG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=1206,
)

_SFCLUSTERDESC_DEVICEDESC.containing_type = _SFCLUSTERDESC
_SFCLUSTERDESC_RAYFEDCONFIG.containing_type = _SFCLUSTERDESC
_SFCLUSTERDESC.fields_by_name['devices'].message_type = _SFCLUSTERDESC_DEVICEDESC
_SFCLUSTERDESC.fields_by_name['ray_fed_config'].message_type = _SFCLUSTERDESC_RAYFEDCONFIG
_STORAGECONFIG_LOCALFSCONFIG.containing_type = _STORAGECONFIG
_STORAGECONFIG.fields_by_name['local_fs'].message_type = _STORAGECONFIG_LOCALFSCONFIG
_SFCLUSTERCONFIG_RAYFEDCONFIG.containing_type = _SFCLUSTERCONFIG
_SFCLUSTERCONFIG_SPUCONFIG.containing_type = _SFCLUSTERCONFIG
_SFCLUSTERCONFIG_PUBLICCONFIG.fields_by_name['ray_fed_config'].message_type = _SFCLUSTERCONFIG_RAYFEDCONFIG
_SFCLUSTERCONFIG_PUBLICCONFIG.fields_by_name['spu_configs'].message_type = _SFCLUSTERCONFIG_SPUCONFIG
_SFCLUSTERCONFIG_PUBLICCONFIG.containing_type = _SFCLUSTERCONFIG
_SFCLUSTERCONFIG_PRIVATECONFIG.fields_by_name['storage_config'].message_type = _STORAGECONFIG
_SFCLUSTERCONFIG_PRIVATECONFIG.containing_type = _SFCLUSTERCONFIG
_SFCLUSTERCONFIG.fields_by_name['desc'].message_type = _SFCLUSTERDESC
_SFCLUSTERCONFIG.fields_by_name['public_config'].message_type = _SFCLUSTERCONFIG_PUBLICCONFIG
_SFCLUSTERCONFIG.fields_by_name['private_config'].message_type = _SFCLUSTERCONFIG_PRIVATECONFIG
DESCRIPTOR.message_types_by_name['SFClusterDesc'] = _SFCLUSTERDESC
DESCRIPTOR.message_types_by_name['StorageConfig'] = _STORAGECONFIG
DESCRIPTOR.message_types_by_name['SFClusterConfig'] = _SFCLUSTERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SFClusterDesc = _reflection.GeneratedProtocolMessageType('SFClusterDesc', (_message.Message,), {

  'DeviceDesc' : _reflection.GeneratedProtocolMessageType('DeviceDesc', (_message.Message,), {
    'DESCRIPTOR' : _SFCLUSTERDESC_DEVICEDESC,
    '__module__' : 'secretflow.protos.component.cluster_pb2'
    # @@protoc_insertion_point(class_scope:secretflow.component.SFClusterDesc.DeviceDesc)
    })
  ,

  'RayFedConfig' : _reflection.GeneratedProtocolMessageType('RayFedConfig', (_message.Message,), {
    'DESCRIPTOR' : _SFCLUSTERDESC_RAYFEDCONFIG,
    '__module__' : 'secretflow.protos.component.cluster_pb2'
    # @@protoc_insertion_point(class_scope:secretflow.component.SFClusterDesc.RayFedConfig)
    })
  ,
  'DESCRIPTOR' : _SFCLUSTERDESC,
  '__module__' : 'secretflow.protos.component.cluster_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.SFClusterDesc)
  })
_sym_db.RegisterMessage(SFClusterDesc)
_sym_db.RegisterMessage(SFClusterDesc.DeviceDesc)
_sym_db.RegisterMessage(SFClusterDesc.RayFedConfig)

StorageConfig = _reflection.GeneratedProtocolMessageType('StorageConfig', (_message.Message,), {

  'LocalFSConfig' : _reflection.GeneratedProtocolMessageType('LocalFSConfig', (_message.Message,), {
    'DESCRIPTOR' : _STORAGECONFIG_LOCALFSCONFIG,
    '__module__' : 'secretflow.protos.component.cluster_pb2'
    # @@protoc_insertion_point(class_scope:secretflow.component.StorageConfig.LocalFSConfig)
    })
  ,
  'DESCRIPTOR' : _STORAGECONFIG,
  '__module__' : 'secretflow.protos.component.cluster_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.StorageConfig)
  })
_sym_db.RegisterMessage(StorageConfig)
_sym_db.RegisterMessage(StorageConfig.LocalFSConfig)

SFClusterConfig = _reflection.GeneratedProtocolMessageType('SFClusterConfig', (_message.Message,), {

  'RayFedConfig' : _reflection.GeneratedProtocolMessageType('RayFedConfig', (_message.Message,), {
    'DESCRIPTOR' : _SFCLUSTERCONFIG_RAYFEDCONFIG,
    '__module__' : 'secretflow.protos.component.cluster_pb2'
    # @@protoc_insertion_point(class_scope:secretflow.component.SFClusterConfig.RayFedConfig)
    })
  ,

  'SPUConfig' : _reflection.GeneratedProtocolMessageType('SPUConfig', (_message.Message,), {
    'DESCRIPTOR' : _SFCLUSTERCONFIG_SPUCONFIG,
    '__module__' : 'secretflow.protos.component.cluster_pb2'
    # @@protoc_insertion_point(class_scope:secretflow.component.SFClusterConfig.SPUConfig)
    })
  ,

  'PublicConfig' : _reflection.GeneratedProtocolMessageType('PublicConfig', (_message.Message,), {
    'DESCRIPTOR' : _SFCLUSTERCONFIG_PUBLICCONFIG,
    '__module__' : 'secretflow.protos.component.cluster_pb2'
    # @@protoc_insertion_point(class_scope:secretflow.component.SFClusterConfig.PublicConfig)
    })
  ,

  'PrivateConfig' : _reflection.GeneratedProtocolMessageType('PrivateConfig', (_message.Message,), {
    'DESCRIPTOR' : _SFCLUSTERCONFIG_PRIVATECONFIG,
    '__module__' : 'secretflow.protos.component.cluster_pb2'
    # @@protoc_insertion_point(class_scope:secretflow.component.SFClusterConfig.PrivateConfig)
    })
  ,
  'DESCRIPTOR' : _SFCLUSTERCONFIG,
  '__module__' : 'secretflow.protos.component.cluster_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.SFClusterConfig)
  })
_sym_db.RegisterMessage(SFClusterConfig)
_sym_db.RegisterMessage(SFClusterConfig.RayFedConfig)
_sym_db.RegisterMessage(SFClusterConfig.SPUConfig)
_sym_db.RegisterMessage(SFClusterConfig.PublicConfig)
_sym_db.RegisterMessage(SFClusterConfig.PrivateConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
