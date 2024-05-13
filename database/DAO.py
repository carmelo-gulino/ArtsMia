from database.Connessione import Connessione
from database.DB_connect import DBConnect
from database.artObjects import ArtObject


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllObjects():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM objects"
        cursor.execute(query)

        for row in cursor:
            result.append(ArtObject(**row))  #se le chiavi del dict sono uguali a quelli del database, crea l'oggetto
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(idMap):
        """
        Controlla le coppie di oggetti comuni a tutte le connessioni, raggruppa per coppie di oggetti e ne
        calcola il numero (peso dell'arco) ordinando in modo decrescente. Crea contestualmente l'oggetto connessione
        trmaite l'idMap di model
        """
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select eo1.object_id o1, eo2.object_id o2, count(*) peso
                    from exhibition_objects eo1, exhibition_objects eo2
                    where eo2.exhibition_id = eo1.exhibition_id and eo1.object_id < eo2.object_id
                    group by eo1.object_id, eo2.object_id
                    order by peso desc"""
        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(idMap[row["o1"]],
                                      idMap[row["o2"]],
                                      row["peso"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(v1: ArtObject, v2: ArtObject):
        """
        Dati due oggetti, conta in quante esibizioni questi due sono esposti: quello è il peso dell'arco
        NON USATO ALL'INTERNO DEL PROGRAMMA
        """
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select count(*)
                    from exhibition_objects eo1, exhibition_objects eo2
                    where eo2.exhibition_id = eo1.exhibition_id and eo1.object_id < eo2.object_id
                    and eo1.object_id = %s and eo2.object_id = %s"""
        cursor.execute(query, (v1.object_id, v2.object_id))

        for row in cursor:
            result.append(ArtObject(**row))  # se le chiavi del dict sono uguali a quelli del database, crea l'oggetto
        cursor.close()
        conn.close()
        return result
