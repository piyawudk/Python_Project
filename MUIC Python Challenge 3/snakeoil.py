# Assignment Snake Oil
# Name: Chatchayuth Supavichayakul
# Collaborators: # Collaborators: Piyawud Koonmanee from KMTL
# Time Spent:


def price(vol):
    base = float(18 * vol)
    if vol < 20:
        base += 250
        return base
    elif vol >= 20 and vol <= 100:
        base += 10 * vol
        return base
    elif vol > 100:
        discount = base * 1 // 100
        total = base - discount
        return total
    else:
        return 0

print(price(200))