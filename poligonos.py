import matplotlib.pyplot as plt
import math
import sys

# Constante global para tolerância
TOL = 1e-9

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

def cross_product(p, q, r):
    """Calcula o produto vetorial entre os vetores PQ e PR."""
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

def point_on_segment(p, a, b):
    """Verifica se o ponto p está no segmento AB com tolerância."""
    if not math.isclose(cross_product(a, b, p), 0.0, abs_tol=TOL):
        return False
    min_x = min(a[0], b[0]) - TOL
    max_x = max(a[0], b[0]) + TOL
    min_y = min(a[1], b[1]) - TOL
    max_y = max(a[1], b[1]) + TOL
    return (min_x <= p[0] <= max_x) and (min_y <= p[1] <= max_y)

def do_intersect(a1, a2, b1, b2):
    """Verifica se os segmentos A1A2 e B1B2 se intersectam."""
    if (point_on_segment(a1, b1, b2) or
        point_on_segment(a2, b1, b2) or
        point_on_segment(b1, a1, a2) or
        point_on_segment(b2, a1, a2)):
        return True
    o1 = cross_product(a1, a2, b1)
    o2 = cross_product(a1, a2, b2)
    o3 = cross_product(b1, b2, a1)
    o4 = cross_product(b1, b2, a2)
    return (o1 * o2 < 0) and (o3 * o4 < 0)

def is_simple(polygon):
    """Verifica se o polígono é simples."""
    n = len(polygon)
    for i in range(n):
        a1, a2 = polygon[i], polygon[(i+1) % n]
        for j in range(i + 1, n):
            if j == (i + 1) % n or i == (j + 1) % n: #Ignora arestas adjacentes
                continue
            b1, b2 = polygon[j], polygon[(j+1) % n]
            if do_intersect(a1, a2, b1, b2):
                return False
    return True

def is_convex(polygon):
    """Verifica se o polígono é convexo."""
    n = len(polygon)
    sign = None
    for i in range(n):
        p1, p2, p3 = polygon[i], polygon[(i+1)%n], polygon[(i+2)%n]
        cross = cross_product(p1, p2, p3)
        current_sign = cross > 0
        if sign is None:
            sign = current_sign
        elif sign != current_sign:
            return False
    return True

def classify_polygons(polygons):
    """Classifica cada polígono como convexo, não simples ou não convexo simples."""
    classified = []
    for i, polygon in enumerate(polygons):
        if is_convex(polygon):
            print(f"{i+1} simples e convexo")
            classified.append(0)
        elif not is_simple(polygon):
            print(f"{i+1} nao simples")
            classified.append(1)
        else:
            print(f"{i+1} simples e nao convexo")
            classified.append(2)
    return classified

def check_vertex(point, polygon):
    """Verifica se o ponto é um vértice do polígono."""
    px, py = point
    for vertex in polygon:
        if math.isclose(px, vertex[0], rel_tol=TOL) and math.isclose(py, vertex[1], rel_tol=TOL):
            return True
    return False

def check_edge(point, polygon):
    """Verifica se o ponto está em qualquer aresta do polígono."""
    px, py = point
    n = len(polygon)
    for k in range(n):
        a = polygon[k]
        b = polygon[(k+1) % n]
        if point_on_segment((px, py), a, b):
            return True
    return False

def ray_casting(point, polygon):
    """Determina se o ponto está dentro do polígono usando ray casting."""
    px, py = point
    inside = False
    n = len(polygon)
    for k in range(n):
        a = polygon[k]
        b = polygon[(k+1) % n]
        ay, by = a[1], b[1]
        if (ay > py) != (by > py):
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            if dy == 0:
                continue
            t = (py - a[1]) / dy
            x_intersec = a[0] + t * dx
            if px < x_intersec - TOL:
                inside = not inside
    return inside

def point_inside_polygon(polygons, points, classified):
    """Processa todos os pontos e polígonos para determinar relações."""
    result = [[] for _ in range(len(points))]
    for i, polygon in enumerate(polygons):
        if classified[i] not in (0, 2): # Ignora polígonos nao-simples
            continue
        for j, point in enumerate(points):
            if check_vertex(point, polygon):
                result[j].append(i+1)
                continue
            if check_edge(point, polygon):
                result[j].append(i+1)
                continue
            if ray_casting(point, polygon):
                result[j].append(i+1)
    # Formata a saída
    for j, lista in enumerate(result):
        lista.sort()
        print(f"{j+1}:" + " ".join(map(str, lista))) if lista else print(f"{j+1}:")

if __name__ == "__main__":
    polygons, points = read_data()
    classified = classify_polygons(polygons)
    point_inside_polygon(polygons, points, classified)
    if "-p" in sys.argv:
        plot_polygons(polygons, points)
