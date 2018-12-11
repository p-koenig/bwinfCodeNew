#  Copyright (c) 2018 Paul König. All rights reserved.
#
#  python Version 3.7; should work on 3.x
#
#  encoding: utf-8
#
#
#  *****************************************************

inputzahlen = 'beispiele/beispiel2.txt'


def zahlenimport(datei):
    puffer = []
    with open(datei) as f:
        for line in f:
            puffer.append(int(line))
    return puffer


def zahlendergroessenach(zahlen):
    outputzahlen = []
    for zahl in range(1, 1000):
        if zahl in zahlen:
            outputzahlen.append(zahl)
    return outputzahlen


def unterteileninfelder(zahlenimport):
    outputfelder = []
    puffer = []
    for feldindex in range(0, 10):
        for zahlenindex in range(feldindex*zahlenimport[-1]//10,
                                 feldindex*zahlenimport[-1]//10 +
                                 zahlenimport[-1]//10+2, 1):
            for zahl in zahlenimport:
                if zahl == zahlenindex:
                    puffer.append(zahl)
        outputfelder.append(puffer)
        puffer = []
    return outputfelder


def zahlensetzen(felder):
    gesetztezahlen = []
    for feld in felder:
        gesetztezahlen.append(feld[0] + (feld[-1]-feld[0])//2)
    return gesetztezahlen


def auszahlungberechnen(gewinnzahlen, glueckszahlen):
    auszahlung = 0
    for zahl in glueckszahlen:
        kleinstedifferenz = 1000
        for gesetztezahl in gewinnzahlen:
            if kleinstedifferenz >= abs(gesetztezahl - zahl):
                kleinstedifferenz = abs(gesetztezahl - zahl)
        auszahlung += kleinstedifferenz
    return auszahlung


if __name__ == '__main__':
    zahlen = zahlendergroessenach(zahlenimport(inputzahlen))
    gesetztezahlen = zahlensetzen(unterteileninfelder(zahlen))
    einzahlung = len(zahlen) * 25
    auszahlung = auszahlungberechnen(gesetztezahlen, zahlen)
    gewinn = einzahlung - auszahlung
    print('Gewählte Zahlen: ', gesetztezahlen, '\nEingenommen: ', einzahlung, '$\nAusgezahlt: ', auszahlung,
          '$\nGewinn: ', gewinn, '$')
