import matplotlib.pyplot as plt
import math

def read_data():
    m, n = map(int, input().split())
    polygons = []
    points = []
    
    for _ in range(m):
        ni = int(input())  # Número de vertices do poligono
        vertices = []
        for _ in range(ni):
            x, y = map(int, input().split())
            vertices.append((x, y))
        polygons.append(vertices)
    
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    return polygons, points

def print_data(polygons, points):
    for i, polygon in enumerate(polygons):
        print(f"Polygon {i + 1}:")
        for vertex in polygon:
            print(f"  {vertex}")
    
    for i, point in enumerate(points):
        print(f"Point {i + 1}: {point}")

def plot_polygons(polygons, points):
    plt.figure(figsize=(8, 8))
    
    for i, polygon in enumerate(polygons):
        x, y = zip(*polygon)
        x += (x[0],)
        y += (y[0],)
        plt.plot(x, y, marker='o', linestyle='-', label=f"Polígono {i+1}")
    
    for j, (x, y) in enumerate(points):
        plt.scatter(x, y, color='red', label="Ponto" if j == 0 else "")
    
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("Polígonos e Pontos")
    plt.legend()
    plt.grid()
    plt.show()

def classify_polygon(polygons):
    for i, polygon in enumerate(polygons):
        if isConvex(polygon):
            print(f"O polígono {i+1} é convexo!")
        else:
            print(f"O polígono {i+1} é não-convexo!")

def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])

def isConvex(polygon):
    n = len(polygon)
    sign = None  # Variável da direção inicial do giro
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]
        p3 = polygon[(i + 2) % n] 
        
        cross = cross_product(p1, p2, p3)  # Calcula o produto vetorial
        
        current_sign = cross > 0
        
        if sign is None:
            sign = current_sign
        elif sign != current_sign:
            return False
    
    return True

if __name__ == "__main__":
    polygons, points = read_data()
    print_data(polygons, points)
    classify_polygon(polygons)
    plot_polygons(polygons, points)
