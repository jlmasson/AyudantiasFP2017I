def almacenarRentasEstudiantes(nombreArchivo, prefijoSalida, horaInicio, horaFinal):
    rentas = cargarInformacionRentas(nombreArchivo, horaInicio, horaFinal)
    if len(rentas) != 0:
        for idEstudiante, infoEstudiante in rentas.items():
            f = open("{}_{}.txt".format(prefijoSalida, idEstudiante), 'w')
            numRentas = infoEstudiante["rentas"]
            numMultas = infoEstudiante["multas"]
            totalMultas = infoEstudiante["totalMultas"]
            linea = "{:d}|{:d}|{:.2f}\n".format(numRentas, numMultas, totalMultas)
            f.write(linea)
            f.close()

def cargarInformacionRentas(nombreArchivo, horaInicio, horaFinal):
    rentas = {}
    f = open(nombreArchivo)
    for line in f:
        componentes = line.strip().split("|")
        idEstudiante = componentes[0].strip()
        horaInicioRenta = int(componentes[-3])
        horaFinRenta = int(componentes[-2])
        if horaInicioRenta >= horaInicio and horaFinRenta <= horaFinal:
            if idEstudiante not in rentas:
                rentas[idEstudiante] = {}
            if len(rentas[idEstudiante]) == 0:
                rentas[idEstudiante]["multas"] = 0
                rentas[idEstudiante]["totalMultas"] = 0
                rentas[idEstudiante]["rentas"] = 0
            valorMulta = float(componentes[-1])
            rentas[idEstudiante]["rentas"] += 1
            if valorMulta > 0:
                rentas[idEstudiante]["multas"] += 1
                rentas[idEstudiante]["totalMultas"] += valorMulta
    f.close()
    return rentas

almacenarRentasEstudiantes("rentas.txt", "reporte", 11, 16)