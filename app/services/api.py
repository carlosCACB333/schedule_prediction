from libs.odbc import ODBC


class Api:
    def __init__(self):
        self.odbc = ODBC()

    def get_lessons(self):
        query_lessons = f"""
           select 
            c.Nombre as curso,
            cp.Nombredocente as docente,
            CONCAT(TRIM(c.Ciclo),'-',TRIM(cp.Seccion)) as grupo
            from dbo.CursoProgramado as cp
            inner join dbo.Curso as c on cp.Curso=c.Curso
            where cp.Semestre='2022-1' and c.Escuela='25'
            order by cp.Seccion
        """
        lessons = self.odbc.execute(query_lessons).fetchall()
        return lessons

    def get_rooms(self):
        query_rooms = f"""
                select 
                Ambiente as ambiente
                from dbo.Ambiente where Pabellon='G'
                order by ambiente
        """
        rooms = self.odbc.execute(query_rooms).fetchall()
        return rooms
