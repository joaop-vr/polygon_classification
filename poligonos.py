import matplotlib.pyplot as plt
import math
from sortedcontainers import SortedList

def read_data():
    m, n = map(int, input().split())
    polygons = []
    points = []
    for _ in range(m):
        ni = int(input())  # Número de vértices do polígono
        vertices = []
        for _ in range(ni):
            x, y = map(int, input().split())
            vertices.append((x, y))
        polygons.append(vertices)
    
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    return polygons, points

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

def classify_polygons(polygons):
    output = []
    for i, polygon in enumerate(polygons):
        if is_convex(polygon):
            print(f"O polígono {i+1} é simples convexo!")
            output.append(0)
        elif not is_simple(polygon):
            print(f"O polígono {i+1} é não-simples!")
            output.append(1)
        else:
            print(f"O polígono {i+1} é simples não-convexo!")
            output.append(2)
    return output

def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])

def is_convex(polygon):
    n = len(polygon)
    sign = None
    for i in range(n):
        p1, p2, p3 = polygon[i], polygon[(i + 1) % n], polygon[(i + 2) % n]
        cross = cross_product(p1, p2, p3)
        current_sign = cross > 0
        if sign is None:
            sign = current_sign
        elif sign != current_sign:
            return False
    return True

def do_intersect(p1, q1, p2, q2):
    o1 = cross_product(p1, q1, p2)
    o2 = cross_product(p1, q1, q2)
    o3 = cross_product(p2, q2, p1)
    o4 = cross_product(p2, q2, q1)
    
    # Verifica sinais opostos
    return (o1 * o2 < 0) and (o3 * o4 < 0)  

def is_simple(polygon):

    n = len(polygon)
    edges = []

    # Gera todas as arestas do polígono
    for i in range(n):
        edges.append((polygon[i], polygon[(i + 1) % n]))
    
    # Verifica todas as combinações de arestas não adjacentes
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            # Desconsidera arestas adjacentes
            if i != j and (i + 1) % n != j and (j + 1) % n != i:
                if do_intersect(edges[i][0], edges[i][1], edges[j][0], edges[j][1]):
                    return False
    return True

if __name__ == "__main__":
    polygons, points = read_data()
    classified = classify_polygons(polygons)
    plot_polygons(polygons, points)
