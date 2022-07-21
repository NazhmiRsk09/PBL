#Group A MAN-2A PBL
#Nazhmi Fadhila, 2102411005
#Bagus Bayu Wijaya, 2102411011
#Wisnu Fajar Nugroho, 2102411024
#Abid Akmal, 2102411025
#Satria Gymnastiar, 2102411028

import csv
import pandas as pd
import numpy as np


###################Mem-proses data dari .csv###################

def interpolasidata(fx0, fx1, x0, x1, x):
    fx = fx0 + (((fx1 - fx0) / (x1 - x0)) * (x - x0))
    return fx

def prosesdata(F_Name, Inp_Fase, Inp_Temp):
    data = pd.read_csv(F_Name)
    ListTemp = data['temp'].tolist()
    if Inp_Temp in ListTemp:
        data_final = data.loc[data['temp'] == Inp_Temp]
        Int_Data = False

    else:
        data_final = data.iloc[(data['temp'] - Inp_Temp).abs().argsort()][:2]
        Int_Data = True

    if (Inp_Fase == 1):
        data_final = pd.DataFrame(data_final, columns=['temp', 'denli', 'heatli', 'therli', 'dynli', 'prandlli'])
        # Untuk output terakhir
        Fase_Out = "Cair"

    else:
        data_final = pd.DataFrame(data_final, columns=['temp', 'denva', 'heatva', 'therva', 'dynva', 'prandlva'])
        # Untuk output terakhir
        Fase_Out = "Uap"

    return Int_Data, Fase_Out, data_final

def memilahdata(Int_Data, data_final, Int_Temp, Int_Material, Int_Fase):
    var1 = []
    var2 = []
    n = 1
    final_var = []

    if (Int_Data == False):
        for x in list(data_final):
            var1.append(data_final[x].values[0])

        while n < 6:
            final_var.append(var1[n])
            n += 1

    elif (Int_Data == True):
        for x in list(data_final):
            var1.append(data_final[x].values[0])
            var2.append(data_final[x].values[1])

        while n < 6:
            final_var.append(interpolasidata(var1[n], var2[n], var1[0], var2[0], Int_Temp))
            n += 1

    return final_var

print("PBL Group A MAN-2A 2022")
print("Material Air, Refrigerant134-a, Ammonia\n")
# Input User
print("1. Air\n2. Refrigerant 134-a\n3. Ammonia")
InputMaterial = int(input("Pilih Material Berdasarkan Nomor: "))
if (InputMaterial <= 0) or (InputMaterial >= 4):
    exit("Program Error!")

print("\n1. Cair(Liquid)\n2. Uap(Vapor)")
InputFase = int(input("Pilih Fase Material Berdasarkan Nomor: "))
if (InputFase <= 0) or (InputFase >= 3):
    exit("Program Error!")

if (InputMaterial == 1):
    print("\nRentang temperatur 0.01C hingga 200C")
    FileName = 'air.csv'
    # Untuk output ke-file baru
    Material = "Air"
    UpperLimit = 200
    BottomLimit = 0.01
elif (InputMaterial == 2):
    print("\nRentang temperatur -40C hingga 100C")
    FileName = 'refrigerant134-a.csv'
    # Untuk output ke-file baru
    Material = "Refrigerant134-a"
    UpperLimit = 100
    BottomLimit = -40
else:
    print("\nRentang temperatur -40C hingga 100C")
    FileName = 'ammonia.csv'
    # Untuk output ke-file baru
    Material = "Ammonia"
    UpperLimit = 100
    BottomLimit = -40

InputTemp = float(input("Ketik Temperatur (dalam celcius): "))
if InputTemp < BottomLimit or InputTemp > UpperLimit:
    exit("Tidak ada data berdasarkan input temperatur yang diberikan, program akan berakhir.")

# Mem-proses data dari .csv berdasarkan input user

functiondata = prosesdata(FileName, InputFase, InputTemp)
InterData = functiondata[0]
Fase = functiondata[1]
datafinal = functiondata[2]

finalvar = memilahdata(InterData, datafinal, InputTemp, InputMaterial, InputFase)

# Output Data
print("\nTemperatur Material = " + str(InputTemp))
print("Densitas (" + Fase + ") = " + str(finalvar[0]) + " kg/m^3")
print("Specific Heat (" + Fase + ") = " + str(finalvar[1]) + " J/kg.K")
print("Thermal Conductivity (" + Fase + ") = " + str(finalvar[2])+ " W/m.K")
print("Dynamic Viscosity (" + Fase + ") = " + str(finalvar[3])+ " kg/m.s")
print("Prandtl Number (" + Fase + ") = " + str(finalvar[4]))

print("\nMemasukkan data yang diperoleh ke material_fase_suhu.csv . . .")
header = list(datafinal)
data = [InputTemp, finalvar[0], finalvar[1], finalvar[2], finalvar[3], finalvar[4]]

with open((Material + "_" + Fase + "_" + str(InputTemp) + ".csv"), 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

print("Pemasukan data sukses!")

###################Menghitung Bil. Reynold###################

#Input User
InputDiaPipa = float(input("\nKetik diameter pipa (dalam mm) = "))
DPipa = InputDiaPipa/1000

velocity = np.sort(np.random.uniform(0.01, 10, 100)).tolist()
BilanganReynold = []

KVNum = finalvar[3]/finalvar[0]

for num in velocity:
    TempNum = (num*DPipa)/KVNum
    BilanganReynold.append(TempNum)

BilanganReynoldLog = np.log10(BilanganReynold).tolist()
velocityLog = np.log10(velocity).tolist()

data = {'Bilangan_Reynold':BilanganReynold, 'Velocity':velocity, 'Bilangan_ReynoldLog':BilanganReynoldLog, 'VelocityLog':velocityLog}
df = pd.DataFrame(data, columns=['Bilangan_Reynold','Velocity','Bilangan_ReynoldLog','VelocityLog'])

VReTransisiB = (KVNum*2300)/DPipa
VReTurbulen = (KVNum*10001)/DPipa

#output

print("\nDensitas ("+Fase+") = "+str(finalvar[0])+ " kg/m^3")
print("Dynamic Viscosity ("+Fase+") = "+str(finalvar[3])+ " kg/m.s")
print("Kinematic Viscosity ("+Fase+") = "+str(round(KVNum,10))+ " m^2/s")
print("Kecepatan aliran saat transisi = "+str(round(VReTransisiB,5))+" m/s hingga kurang dari "+str(round(VReTurbulen,5))+" m/s")
print("Kecepatan aliran saat turbulen = sama dengan hingga lebih dari "+str(round(VReTurbulen,5))+" m/s")
print(df.plot(x='VelocityLog', y='Bilangan_ReynoldLog'))