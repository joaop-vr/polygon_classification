import matplotlib.pyplot as plt

def read_data():
    m, n = map(int, input().split())
    polygons = []
    points = []
    
    for _ in range(m):
        ni = int(input())  # Number of vertices in the polygon
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
        x_coords, y_coords = zip(*polygon)
        x_coords += (x_coords[0],)  # Closing the polygon
        y_coords += (y_coords[0],)
        plt.plot(x_coords, y_coords, marker='o', linestyle='-', label=f"Poligono {i+1}")
    
    for j, (x, y) in enumerate(points):
        plt.scatter(x, y, color='red', label="Ponto" if j == 0 else "")
    
    plt.xlabel("eixo X")
    plt.ylabel("eixo Y")
    plt.title("Polígonos e Pontos")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    polygons, points = read_data()
    print_data(polygons, points)
    plot_polygons(polygons, points)
