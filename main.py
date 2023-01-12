import Densidad as dn
import pandas as pd
import Poblacion as tn
import densidad_M2 as pn
if __name__=='__main__':
    cities = pd.read_csv("lista.csv")
    print(dn.density_per_km2(cities))
    print(pn.density_per_m2())
    print(tn.total_population())



