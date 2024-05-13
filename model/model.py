import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._artObjectsList = DAO.getAllObjects()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._artObjectsList)
        self._idMap = {}
        for artObject in self._artObjectsList:
            self._idMap[artObject.object_id] = artObject

    def creaGrafo(self):
        self.addEdges()

    def addEdges(self):
        """
        Resetta gli archi del grafo e ne crea di nuovi a seconda della richiesta
        """
        self._grafo.clear_edges()
        edges = DAO.getAllConnessioni(self._idMap)
        for e in edges:
            self._grafo.add_edge(e.v1, e.v2, weight=e.peso)
        print(self._grafo)

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def checkExistence(self, idOggetto):
        """
        Controlla che l'oggetto sia presente fra le chiavi della mappa
        """
        return idOggetto in self._idMap

    def getConnessa(self, v0Int):
        """
        Restituisce la componente connessa che contiene v0
        """
        v0 = self._idMap[v0Int]  #estraggo l'oggetto
        '''# Metodo 1: trovo i predecessori
        predecessors = nx.dfs_predecessors(self._grafo, v0)
        print(len(predecessors.values()))
        # Metodo 2: trovo i successori e li aggiungo tramite extend
        successors = nx.dfs_successors(self._grafo, v0)
        allSucc = []
        for v in successors.values():
            allSucc.extend(v)
        # Metodo 3: creo l'albero e conto i nodi dell'albero
        tree = nx.dfs_tree(self._grafo, v0)  #ottengo l'albero connesso a partire da v0
        print(len(tree.nodes))  #conto i nodi dell'albero'''
        # Metodo 4: uso il metodo dedicato
        connComp = nx.node_connected_component(self._grafo, v0)  #restituisce un set di nodi
        print(len(connComp))
        return len(connComp)

    @property
    def artObjectsList(self):
        return self._artObjectsList

    @property
    def grafo(self):
        return self._grafo

    @property
    def idMap(self):
        return self._idMap
