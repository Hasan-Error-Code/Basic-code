use = input("Enter a String: ")
users = use.split()
up = ""
lo = ""
nu = ""
ch = ""

chu = "A, B, C, D, E, F, G, H, I, J, K, L, M ,N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
chl = chu.lower()

while users in chu: 
    up += users
print(up)