# -*- coding: utf-8 -*-
db.define_tables('pagos',
        Field('num_caja','string'),
        Field('clav_cuenta','string'),
        Field('rfc','string'),
        Field('clav_catastral','string'),
        Field('nombre','string'),
        Field('direccion','string'),
        Field('fech_pago','datetime'),
        Field('folio_rec','string'),
        Field('import','double'),
        Field('actual','double'),
        Field('recarg','double'),
        Field('multas','double'),
        Field('gastos','double'),
        Field(

