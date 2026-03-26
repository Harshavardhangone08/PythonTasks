# Align text using formatting. 

# vertical or same line
text="{:<10}{:^5}{:>10}".format("Left","Center","Right")
print(text)
print()
# horizontal
print(f"{'Python':<10}")
print(f"{'Python':^10}")
print(f"{'Python':>10}")

