import matplotlib.pyplot as plt

likes = [10, 50, 100, 200, 500]
shares = [1, 5, 10, 25, 60]

plt.scatter(likes, shares, color="red", marker="o", label="Likes")

plt.title("Interacciones en Redes Sociales")
plt.xlabel("Número de Likes")
plt.ylabel("Número de Shares")
plt.legend()
plt.grid()

plt.show()
