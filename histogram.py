def histogram(points, bins):
    n = len(points)
    densities = []
    i = 0  

    for (a, b) in bins:
        count = 0
        width = b - a

        while i < n and points[i] < b:
            if points[i] >= a:
                count += 1
            i += 1

        densities.append(count / (n * width))

    return densities
