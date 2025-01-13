from bbdd.bbdd import connect_to_bbdd
from psycopg2 import DataError,DatabaseError

#insertar usuari nou
def insert_user(form):

    try:
        cur_conn = connect_to_bbdd()
        cur_conn[0].execute("""INSERT INTO public.users_db (nombre
                                                                ,apellido
                                                                ,correo_electronico
                                                                ,descripcion
                                                                ,curso
                                                                ,anyo
                                                                ,direccion
                                                                ,codigo_postal
                                                                ,password)
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(form.nombre
                                                                        ,form.apellido
                                                                        ,form.correoelectronico
                                                                        ,form.descripcion
                                                                        ,form.curso
                                                                        ,form.anyo
                                                                        ,form.direccion
                                                                        ,form.codigopostal
                                                                        ,form.password))
        cur_conn[1].commit()
        msg = {"msg":"OK"}
        cur_conn[0].close()
        cur_conn[1].close()
    except DataError:
        msg = {"msg": DataError}
        cur_conn[0].close()
        cur_conn[1].close()
    except DatabaseError:
        msg = {"msg": DatabaseError}
        cur_conn[0].close()
        cur_conn[1].close()

    return msg

#Mostrar tots el usuaris
def select_users():

    try:
        cur_conn = connect_to_bbdd()

        cur_conn[0].execute("""SELECT * FROM public.users_db
                                 ORDER BY SURNAME ASC  """)
        res = cur_conn[0].fetchall()
        cur_conn[0].close()
        cur_conn[1].close()
    except DataError:
        res = {"msg": DataError}
        cur_conn[0].close()
        cur_conn[1].close()
    except DatabaseError:
        res = {"msg": DatabaseError}
        cur_conn[0].close()
        cur_conn[1].close()
    return res