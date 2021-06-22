import cmath

N = 2

# Ensaio de Curto Circuito: Determina parâmetros do circuito série

# Com o secundário em curto (e portanto o circuito de magnetização em curto)
# aplica-se uma tensão no primário até que seja observada uma corrente no
# primário igual à sua corrente nominal

# Observe: A corrente envolvida é a nominal do primário. Ela pode ser omitida
# diretamente do resultado teste se essa informação for dada.

# Potência Ativa, Tensão e Corrente são assumidas a serem referidas pelo
# PRIMÁRIO. Se dadas pelo SECUNDÁRIO, reflexão é necessária.

P_cc = 400
V_cc = 125
I_cc = 10

R_t = round(P_cc/(I_cc**2), 2)
print(f"Rt = {R_t}")

Z_t = V_cc/I_cc
print(f"Zt = {Z_t}")

X_t = round(((Z_t**2) - (R_t**2))**(1/2), 2)

print(f"Xt = {X_t}")

# Ensaio a Vazio/Circuito Aberto: Determina parâmetros do circuito de
# magnetização

# Com o (geralmente) primário em aberto aplica-se a tensão nominal do
# enrolamento secundário a seus terminais.

# Observe: A tensão envolvida é a nominal do secundário. Ela pode ser omitida
# diretamente do resultado teste se essa informação for dada.

# Potência Ativa, Tensão e Corrente são assumidas a serem referidas pelo
# SECUNDÁRIO. Se dadas pelo PRIMÁRIO, reflexão é necessária.

P_ca = 100
V_ca = 500
I_ca = 0.84

R_2_a = ((V_ca)**2)/P_ca
print(f"R2a = {R_2_a}")
Z_2_ca = (V_ca/I_ca)
print(f"Z2ca = {Z_2_ca:.2f}")

X_2_m = ((((1/Z_2_ca)**2) - (1/R_2_a)**2)**(1/2))**-1
print(f"X2m = {X_2_m:.2f}")

# Reflexão para primário

X_m = round(X_2_m * (N**2), 2)
R_a = round(R_2_a * (N**2), 2)

print(f"Ra = {R_a}")
print(f"Xm = {X_m}")

# Associação em paralelo

X_m = complex(0, X_m)
R_a = complex(R_a, 0)

print(f"Impedância de Magnetização: Zm = {Z_m}")
