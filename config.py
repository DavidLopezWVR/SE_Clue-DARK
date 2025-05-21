# config.py

# Personajes con detalles
personajes = [
    {
        "nombre": "Jonas",
        "profesion": "Viajero del tiempo",
        "edad": 19,
        "linea_temporal": "2053",
        "afiliacion": "Sic Mundus",
        "estado": "Desaparecido",
        "imagen": "jonas.png"
    },
    {
        "nombre": "Martha",
        "profesion": "Elegida del mundo alternativo",
        "edad": 17,
        "linea_temporal": "Mundo alternativo",
        "afiliacion": "Desconocida",
        "estado": "Viva",
        "imagen": "martha.png"
    },
    {
        "nombre": "Claudia",
        "profesion": "Investigadora del tiempo",
        "edad": 45,
        "linea_temporal": "1986",
        "afiliacion": "Independiente",
        "estado": "Muerta",
        "imagen": "claudia.png"
    },
    {
        "nombre": "Noah",
        "profesion": "Sacerdote misterioso",
        "edad": 38,
        "linea_temporal": "1953",
        "afiliacion": "Sic Mundus",
        "estado": "Vivo",
        "imagen": "noah.png"
    },
    {
        "nombre": "Ulrich",
        "profesion": "Policía de Winden",
        "edad": 41,
        "linea_temporal": "2019",
        "afiliacion": "Familia Nielsen",
        "estado": "Prisionero en el pasado",
        "imagen": "ulrich.png"
    }
]

# Locaciones con descripción, pista estática, personaje habitual e imagen
locaciones = [
    {
        "nombre": "La cueva",
        "descripcion": "Un pasadizo entre épocas, marcado por símbolos extraños.",
        "pista_estatica": "Se hallaron rastros de tierra húmeda y una linterna rota.",
        "habitual_de": "Jonas",
        "imagen": "cueva.png"
    },
    {
        "nombre": "El búnker",
        "descripcion": "Refugio usado para esconder secretos en múltiples tiempos.",
        "pista_estatica": "Una cuerda ensangrentada cuelga del techo.",
        "habitual_de": "Ulrich",
        "imagen": "bunker.png"
    },
    {
        "nombre": "La planta nuclear",
        "descripcion": "Fuente de energía... y de anomalías temporales.",
        "pista_estatica": "Un medidor de radiación alterado fue encontrado cerca.",
        "habitual_de": "Claudia",
        "imagen": "planta.png"
    },
    {
        "nombre": "Casa de los Doppler",
        "descripcion": "Lugar de reuniones y oscuros secretos familiares.",
        "pista_estatica": "Había documentos quemados en la chimenea.",
        "habitual_de": "Martha",
        "imagen": "casa_doppler.png"
    },
    {
        "nombre": "La iglesia",
        "descripcion": "Sede de predicaciones extrañas lideradas por Noah.",
        "pista_estatica": "Se encontraron notas escritas en latín.",
        "habitual_de": "Noah",
        "imagen": "iglesia.png"
    }
]

# Armas con descripción, época e imagen
armas = [
    {
        "nombre": "Revólver",
        "descripcion": "Un arma antigua, aún funcional, con rastros de sangre.",
        "tiempo": "1953",
        "imagen": "revolver.png"
    },
    {
        "nombre": "Cuerda",
        "descripcion": "Soga usada para colgar objetos... o personas.",
        "tiempo": "Desconocido",
        "imagen": "cuerda.png"
    },
    {
        "nombre": "Estatuilla",
        "descripcion": "Objeto ceremonial sólido, con bordes afilados.",
        "tiempo": "Mundo alternativo",
        "imagen": "estatuilla.png"
    },
    {
        "nombre": "Tijeras",
        "descripcion": "Instrumento quirúrgico de precisión.",
        "tiempo": "2019",
        "imagen": "tijeras.png"
    },
    {
        "nombre": "Jeringa con veneno",
        "descripcion": "Contiene un líquido amarillo brillante.",
        "tiempo": "2053",
        "imagen": "jeringa.png"
    }
]
