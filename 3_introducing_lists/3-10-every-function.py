mes_villes = ["Avignon","Clermont-Ferrand"]
mes_villes.append("Marseille")
mes_villes.insert(2,"Aix-en-Provence")
print(mes_villes)

del mes_villes[3]
mes_villes.pop()
mes_villes.pop(0)
mes_villes.remove("Clermont-Ferrand")
print(mes_villes)

mes_villes = ["Avignon","Clermont-Ferrand","Aix-en-Provence"]
print(sorted(mes_villes))
print(sorted(mes_villes,reverse=True))

mes_villes.reverse()
print(mes_villes)

mes_villes.sort()
mes_villes.sort(reverse=True)
print(mes_villes)

print(len(mes_villes))
