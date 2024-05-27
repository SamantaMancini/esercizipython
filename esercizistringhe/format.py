name = "Alice"
age = 25
message = "Ciao, mi chiamo {} e ho {} anni." .format(name, age)
print(message)

pi = 3.14159265359

formatted_pi = "Valore di pi: {:.2f}" .format(pi)
print(formatted_pi)
formatted_pi = "Valore di pi: {:.4f}" .format(pi)
print(formatted_pi)

name = "Alice"
age = 25

print("Nome: {:<10} Età: {}" .format(name, age))

print("Nome: {:>10} Età: {}" .format(name, age))

print("Nome: {:^10} Età: {}" .format(name, age))

name = "Alice"
age = 25

message = "Il mio nome è {0} e ho {1} anni." .format(name, age)
print(message)

message = "Il mio nome è {0} e ho {1} anni. {0} è un bel nome!".format(name, age)
print(message)

