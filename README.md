sqlserver_saltstack
===================

Inicio de sqlserver para saltstack

para la instalacion es necesario lo siguiente:
  python pymssql
  saltstack
  
Paso siguiente generar pillar srv/pillar/name.sls
==== name.sls ====
sqlserver:
  db_name:
    server: ip servidor
    uid: user name
    passw: password user
=== Fin name.sls ===

Para agregar mas bases de datos ejemplo:
==== name.sls ====
sqlserver:
  db_1:
    server: ip servidor
    uid: user name
    passw: password user
  db_2:
    server: ip servidor
    uid: user name
    passw: password user
    .
    .
    .
    db_n:
    server: ip servidor
    uid: user name
    passw: password user
=== Fin name.sls ===

