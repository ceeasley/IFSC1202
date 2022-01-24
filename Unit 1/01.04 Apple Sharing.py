#N students take K apples from a basket and distribute them among each other evenly. The remaining (the undivisible) apples remains in the basket.
#How many apples will each single student get?
#How many apples will remain in the basket?

basket = int(input("How many apples are in the basket?: "))
student = int(input("How many students are there?: "))

apples = basket//student
remain = basket%student

print("Each student will get "+ str(apples)+" apples.")
print("There will be "+str(remain)+" apples left in the basket.")
