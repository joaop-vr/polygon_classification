import matplotlib.pyplot as plt
import math
import sys

######################## FUNÇÔES AUXILIARES #####################################

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


######################## FUNÇÔES PRINCIPAIS #####################################

def angle_between_vectors(v1, v2):
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    norm_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    norm_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    
    if norm_v1 == 0 or norm_v2 == 0:
        return 0  # Evita divisão por zero
    
    cos_theta = dot_product / (norm_v1 * norm_v2)
    cos_theta = max(-1, min(1, cos_theta))  # Garante que o valor esteja dentro do intervalo válido
    return math.acos(cos_theta)


import math

def point_on_segment(p, a, b):
    """Verifica se o ponto p está no segmento de reta entre a e b."""
    # Verifica colinearidade
    cross_product = (p[0] - a[0]) * (b[1] - a[1]) - (p[1] - a[1]) * (b[0] - a[0])
    if not math.isclose(cross_product, 0, rel_tol=1e-9, abs_tol=0.0):
        return False
    # Verifica se está dentro do retângulo delimitador
    min_x = min(a[0], b[0])
    max_x = max(a[0], b[0])
    min_y = min(a[1], b[1])
    max_y = max(a[1], b[1])
    if (p[0] < min_x - 1e-9 or p[0] > max_x + 1e-9 or
        p[1] < min_y - 1e-9 or p[1] > max_y + 1e-9):
        return False
    return True

def point_inside_polygon(polygons, points, classified):
    result = [[] for _ in range(len(points))]
    
    for i, polygon in enumerate(polygons):
        if classified[i] not in (0, 2):
            continue
        
        for j, (px, py) in enumerate(points):
            # Verifica se o ponto é um vértice
            is_vertex = False
            for vertex in polygon:
                if math.isclose(px, vertex[0], rel_tol=1e-9) and math.isclose(py, vertex[1], rel_tol=1e-9):
                    is_vertex = True
                    break
            if is_vertex:
                result[j].append(i+1)
                continue
            
            # Verifica se está em alguma aresta
            on_edge = False
            n = len(polygon)
            for k in range(n):
                a = polygon[k]
                b = polygon[(k+1) % n]
                if point_on_segment((px, py), a, b):
                    on_edge = True
                    break
            if on_edge:
                result[j].append(i+1)
                continue
            
            # Algoritmo do Ray Casting
            inside = False
            for k in range(n):
                a = polygon[k]
                b = polygon[(k+1) % n]
                ay, by = a[1], b[1]
                
                # Verifica se o raio cruza a aresta
                if ((ay > py) != (by > py)):
                    # Calcula a interseção x
                    dx = b[0] - a[0]
                    dy = b[1] - a[1]
                    if dy == 0:
                        continue  # Ignora arestas horizontais
                    t = (py - a[1]) / dy
                    x_intersec = a[0] + t * dx
                    # Verifica se o ponto está à esquerda da interseção
                    if px < x_intersec:
                        inside = not inside
            if inside:
                result[j].append(i+1)
    
    # Formata a saída
    for j, lista in enumerate(result):
        lista.sort()
        print(f"{j+1}:" + " ".join(map(str, lista))) if lista else print(f"{j+1}:")


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


def classify_polygons(polygons):
    output = []
    for i, polygon in enumerate(polygons):
        if is_convex(polygon):
            print(f"{i+1} simples e convexo")
            output.append(0)
        elif not is_simple(polygon):
            print(f"{i+1} nao simples")
            output.append(1)
        else:
            print(f"{i+1} simples e nao convexo")
            output.append(2)
    return output


if __name__ == "__main__":
    polygons, points = read_data()
    classified = classify_polygons(polygons)
    point_inside_polygon(polygons, points, classified)
    if "-p" in sys.argv:
        plot_polygons(polygons, points)
