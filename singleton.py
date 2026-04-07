class Sistema:
    _instancia = None

    def _new_(cls):
        if cls._instancia is None:
            cls.instancia = super().new_(cls)
        return cls._instancia

    def iniciar(self):
        print("Sistema iniciado")