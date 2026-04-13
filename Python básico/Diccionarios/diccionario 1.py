hotel = {
    "nombre": "Gran Hotel Paraíso",
    "numero_de_estrellas": 5,
    "habitaciones": [
        {"numero": 101, "piso": 1, "precio_por_noche": 85.50},
        {"numero": 202, "piso": 2, "precio_por_noche": 120.00},
        {"numero": 305, "piso": 3, "precio_por_noche": 250.00}
    ]
}

print(f"El precio de la habitación {hotel['habitaciones'][0]['numero']} es ${hotel['habitaciones'][0]['precio_por_noche']}")