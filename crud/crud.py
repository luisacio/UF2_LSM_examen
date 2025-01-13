from bbdd.bbdd import connect_to_bbdd
from psycopg2 import DataError,DatabaseError

def insert_user(form):
    cur_conn = connect_to_bbdd()
    try:
        cur_conn[0].execute("""INSERT INTO public.users_db (nombre
                                                                ,apellido
                                                                ,correo_electronico
                                                                ,descripcion
                                                                ,curso
                                                                ,anyo
                                                                ,direccion
                                                                ,codigo_postal
                                                                ,password)
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(form.theme,form.word))
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