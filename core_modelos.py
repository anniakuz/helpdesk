"""Bloque 1 (UF2404). Modelos POO independientes de Django."""


class EstadoInvalidoError(Exception):
    """Se intenta una transicion de estado no permitida."""


class PrioridadInvalidaError(Exception):
    """La prioridad indicada no existe."""


class TicketTecnico:
    ESTADOS = ("Abierto", "En Proceso", "Cerrado")
    PRIORIDADES = ("Baja", "Media", "Alta", "Critica")

    TRANSICIONES = {
        "Abierto": ("En Proceso", "Cerrado"),
        "En Proceso": ("Abierto", "Cerrado"),
        "Cerrado": ("Abierto",),
    }

    SLA_BASE = {"Baja": 72, "Media": 48, "Alta": 24, "Critica": 8}

    def __init__(self, id_ticket, titulo, prioridad="Media"):
        self._id = id_ticket
        self._titulo = titulo
        self._estado = "Abierto"
        self._prioridad = None
        self.prioridad = prioridad

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def estado(self):
        return self._estado

    @property
    def prioridad(self):
        return self._prioridad

    @prioridad.setter
    def prioridad(self, valor):
        if valor not in self.PRIORIDADES:
            raise PrioridadInvalidaError(f"Prioridad no valida: {valor}")
        self._prioridad = valor

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS:
            raise EstadoInvalidoError(f"Estado desconocido: {nuevo_estado}")
        if nuevo_estado not in self.TRANSICIONES[self._estado]:
            raise EstadoInvalidoError(
                f"Transicion no permitida: {self._estado} -> {nuevo_estado}"
            )
        self._estado = nuevo_estado

    def iniciar(self):
        self.cambiar_estado("En Proceso")

    def cerrar(self):
        self.cambiar_estado("Cerrado")

    def reabrir(self):
        self.cambiar_estado("Abierto")

    def calcular_sla(self):
        """Horas maximas de resolucion. Las hijas la sobrescriben."""
        return self.SLA_BASE[self._prioridad]

    def __str__(self):
        return (
            f"[{self.__class__.__name__} #{self._id}] {self._titulo} "
            f"({self._estado}, {self._prioridad}) SLA {self.calcular_sla()} h"
        )


class TicketHardware(TicketTecnico):
    FACTOR = 1.5

    def __init__(self, id_ticket, titulo, prioridad, componente):
        super().__init__(id_ticket, titulo, prioridad)
        self.componente = componente

    def calcular_sla(self):
        return int(super().calcular_sla() * self.FACTOR)


class TicketSoftware(TicketTecnico):
    def __init__(self, id_ticket, titulo, prioridad, sistema_operativo):
        super().__init__(id_ticket, titulo, prioridad)
        self.sistema_operativo = sistema_operativo

    def calcular_sla(self):
        horas = super().calcular_sla()
        if self.sistema_operativo.lower() == "linux":
            horas -= 4
        return max(horas, 2)


if __name__ == "__main__":
    tickets = [
        TicketHardware(1, "Disco duro con ruidos", "Alta", "SSD"),
        TicketSoftware(2, "Error al iniciar sesion", "Critica", "Windows"),
        TicketSoftware(3, "Servicio no arranca", "Media", "Linux"),
    ]

    print("1. Polimorfismo en calcular_sla")
    for t in tickets:
        print(t)

    print("\n2. Transiciones validas")
    t = tickets[0]
    t.iniciar()
    print(t.estado)
    t.cerrar()
    print(t.estado)

    print("\n3. Transicion invalida")
    try:
        t.cambiar_estado("En Proceso")
    except EstadoInvalidoError as e:
        print("EstadoInvalidoError:", e)

    print("\n4. Estado inexistente")
    try:
        t.cambiar_estado("Pausado")
    except EstadoInvalidoError as e:
        print("EstadoInvalidoError:", e)

    print("\n5. Prioridad invalida")
    try:
        TicketHardware(9, "Prueba", "Urgente", "RAM")
    except PrioridadInvalidaError as e:
        print("PrioridadInvalidaError:", e)

    print("\n6. Reabrir un ticket cerrado")
    t.reabrir()
    print(t.estado)