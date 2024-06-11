from validate_docbr import CPF

cpf = CPF()

# Validar CPF  # True
print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("99178188989"))
print(cpf.validate("251.870.504-00"))