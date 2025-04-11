import matplotlib.pyplot as plt
import math

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


def point_inside_polygon(polygons, points, classified):
    
    # Cria uma lista de listas para armazenar os índices dos polígonos que contêm cada ponto.
    result = [[] for _ in range(len(points))]
    
    # Itera sobre cada polígono com seu índice
    for i, polygon in enumerate(polygons):
        # Processa apenas polígonos classificados como simples (convexos ou côncavos)
        if classified[i] == 0 or classified[i] == 2:
            # Itera sobre cada ponto com seu índice
            for j, (px, py) in enumerate(points):
                # Se o ponto coincidir com algum vértice do polígono, já consideramos que ele está dentro
                if (px, py) in polygon:
                    result[j].append(i+1)  # +1 para usar indexação 1-base
                    continue

                # Cálculo do ângulo total formado pelas arestas com vértices do polígono
                angulo_total = 0.0
                n_vertices = len(polygon)
                for k in range(n_vertices):
                    x1 = polygon[k][0] - px
                    y1 = polygon[k][1] - py
                    x2 = polygon[(k + 1) % n_vertices][0] - px
                    y2 = polygon[(k + 1) % n_vertices][1] - py
                    
                    angulo_total += angle_between_vectors((x1, y1), (x2, y2))
                
                # Se a soma dos ângulos for aproximadamente 2pi(360 graus), o ponto está dentro
                if math.isclose(angulo_total, 2 * math.pi, rel_tol=1e-5):
                    result[j].append(i+1)
    
    # Para cada ponto, ordena os índices dos polígonos e imprime
    for j, lista_poligonos in enumerate(result):
        lista_poligonos.sort()
        if lista_poligonos:
            saida = " ".join(str(idx) for idx in lista_poligonos)
            print(f"{j+1}:{saida}")
        else:
            print(f"{j+1}:")


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
    plot_polygons(polygons, points)
