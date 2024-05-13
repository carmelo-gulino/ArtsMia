import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi e "
                                                      f"{self._model.getNumEdges()} archi."))
        self._view.update_page()

    def handleCompConnessa(self, e):
        idAdded = self._view._txtIdOggetto.value
        try:  #solo se il valore è corretto
            intIdAddedd = int(idAdded)
            if self._model.checkExistence(intIdAddedd):  #controllo che l'id inserito esista
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text(f"L'oggetto {intIdAddedd} è presente nel grafo"))
                sizeConn = self._model.getConnessa(intIdAddedd)
                self._view.txt_result.controls.append(ft.Text(f"La componente connessa che contiene "
                                                              f"{intIdAddedd} ha dimensione {sizeConn}"))
            else:
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text(f"L'oggetto {intIdAddedd} non è presente nel grafo"))
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Il valore inserito non è corretto"))
        self._view.update_page()
