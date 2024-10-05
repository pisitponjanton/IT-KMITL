"""RectangleArea"""
def overlapping_area(x1, y1, w1, h1, x2, y2, w2, h2):
    """RectangleArea"""
    x_overlap = min(x1 + w1, x2 + w2) - max(x1, x2)
    y_overlap = min(y1 + h1, y2 + h2) - max(y1, y2)
    area = x_overlap * y_overlap
    if area > 0 and x_overlap >0 and y_overlap>0:
        return area
    return "no overlapping"
def main():
    """RectangleArea"""
    x1, y1, w1, h1 = map(int, input().split())
    x2, y2, w2, h2 = map(int, input().split())
    result = overlapping_area(x1, y1, w1, h1, x2, y2, w2, h2)
    print(result)
main()
