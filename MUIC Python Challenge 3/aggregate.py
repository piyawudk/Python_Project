p = 13.0
q = 17.0
r = 14.0
p_2 = float(p)
q_2 = float(q)
r_2 = float(r)

def my_min(p_2, q_2, r_2):
    if p_2 >= q_2 and p_2 >= r_2:
        if q_2 >= r_2:
            return r_2
        else:
            return q_2
    if q_2 >= p_2 and q_2 >= r_2:
        if p_2 >= r_2:
            return r_2
        else:
            return p_2
    if r_2 >= p_2 and r_2 >= q_2:
        if p_2 >= q_2:
            return q_2
        else:
            return p_2
    if p_2 >= r_2 and p_2 >= q_2:
        if r_2 >= q_2:
            return q_2
        else:
            return r_2
    if q_2 >= r_2 and q_2 >= p_2:
        if r_2 >= p_2:
            return p_2
        else:
            return r_2
    if r_2 >= q_2 and r_2 >= p_2:
        if q_2 >= p_2:
            return p_2
        else:
            return q_2


def my_mean(p_2, q_2, r_2):
    return ((p_2 + q_2 + r_2) / 3.0)


def my_med(p_2, q_2, r_2):
    if p_2 >= q_2 and p_2 >= r_2:
        if q_2 >= r_2:
            return q_2
        else:
            return r_2
    if q_2 >= p_2 and q_2 >= r_2:
        if p_2 >= r_2:
            return p_2
        else:
            return r_2
    if r_2 >= p_2 and r_2 >= q_2:
        if p_2 >= q_2:
            return p_2
        else:
            return q_2
    if p_2 >= r_2 and p_2 >= q_2:
        if r_2 >= q_2:
            return r_2
        else:
            return q_2
    if q_2 >= r_2 and q_2 >= p_2:
        if r_2 >= p_2:
            return r_2
        else:
            return p_2
    if r_2 >= q_2 and r_2 >= p_2:
        if q_2 >= p_2:
            return q_2
        else:
            return p_2

print(my_min(3.0,1.0,9.0))
print(my_mean(3.0, 7.0, 4.0))
print(my_med(4.0,1.0,5.0))