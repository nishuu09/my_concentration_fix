def hitung_massa(mol, massa_molar):
    massa = mol * massa_molar
    return massa

# Contoh penggunaan:
mol = 2  # mol
massa_molar = 18  # g/mol (contoh: H2O)

massa = hitung_massa(mol, massa_molar)
print(f"Massa: {massa} gram")

