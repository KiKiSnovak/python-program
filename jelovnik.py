#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "\n----------------------------------------\n"
print "Dobrodošli!"
print "Ovdje možete upisati svoj meni za danas."

meni_lista = {}

while True:

    name = raw_input("Unesite ime jela: ")
    price = raw_input("Unesite cijenu jela: ")
    if "kn" not in price:
        price = price + " kn"

    print "Unijeli ste jelo: " + name + ", sa cijenom: " + price

    while True:

        nastavi = raw_input("Jeste li ispravno unijeli jelo i cijenu?(da/ne): ")

        if nastavi == "da":
            meni_lista[name] = price
            break
        elif nastavi == "ne":
            break
        else:
            print "Molim vas da unesete da ili ne"

    if nastavi == "ne":
        print "probajte ponovo."
        continue

    while True:
        new = raw_input("Želite li unijeti još jela (da/ne) ili želite vidjeti sva jela (sve): ")

        if new == "da":
            break
        elif new == "ne":
            meni_file = open("meni.txt", "w+")

            meni_file.write("Vaš Meni:")
            print "\nVaš Meni:"
            for x in meni_lista:
                print x + ": " + meni_lista[x]
                meni_file.write("\n" + x + ": " + meni_lista[x])

            print "Vaš meni se ispisao u tekst dokument"
            print "Program se gasi"
            break

        elif new == "sve":
            meni_file = open("meni.txt", "w+")

            meni_file.write("Vaš Meni:")
            print "\nVaš Meni:"
            for x in meni_lista:
                print x + ": " + meni_lista[x]
                meni_file.write("\n" + x + ": " + meni_lista[x])

            continue

    if new == "da":
        continue
    if new == "ne":
        break






