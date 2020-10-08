def hamming_kodieren(daten):
    kode = (daten & 0b1111111) | ((daten & 0b1110000000) << 1) | ((daten & 0b10000000000) << 2)
    teil1 = kode & 0b001010101010101
    teil2 = kode & 0b001011001100110
    teil3 = kode & 0b000011100001111
    teil4 = kode & 0b000000001111111
    bit1 = bin(teil1).count("1") % 2
    bit2 = bin(teil2).count("1") % 2
    bit3 = bin(teil3).count("1") % 2
    bit4 = bin(teil4).count("1") % 2
    kode = kode | (bit1 << 14) | (bit2 << 13) | (bit3 << 11) | (bit4 << 7)
    return kode

# Hauptprogramm

# Kodieren

daten = int(input("Datenwort (max. 11 Bits) eingeben: "),2)
print("Kodewort: " + bin(hamming_kodieren(daten)))

