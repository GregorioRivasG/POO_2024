from conexionBD import *
try:
    micursor=conexion.cursor()
    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Daniel Contreras', 'Col. centro', '6181234567')"
    micursor.execute(sql)
    #Es necesario para que al final se complete el Execute(sql) y finalice la consulta SQL
    conexion.commit() 
except:
    print(f"hay un error en el sistema")