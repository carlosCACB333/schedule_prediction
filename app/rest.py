dic = {
    "name": "Rahul",
    "age": 22,
}

other_dic = {
    **dic,
    "age": 23,
    "email": "ra"
}

print(other_dic)
