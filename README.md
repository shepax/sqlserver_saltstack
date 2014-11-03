sqlserver_saltstack
===================

Inicio de sqlserver para saltstack

para la instalacion es necesario lo siguiente:
  python pymssql
  saltstack
  
Paso siguiente generar pillar srv/pillar/db.sls
==== db.sls ====
sqlserver:
  db_name:
    host: ip host (111.111.111.1:port)
    uid: user name
    passw: password user
=== Fin name.sls ===

Para agregar mas bases de datos ejemplo:
==== db.sls ====
sqlserver:
  db_1:
    host: ip servidor
    uid: user name
    passw: password user
  db_2:
    host: ip servidor
    uid: user name
    passw: password user
    .
    .
    .
    db_n:
    host: ip servidor
    uid: user name
    passw: password user
=== Fin db.sls ===

