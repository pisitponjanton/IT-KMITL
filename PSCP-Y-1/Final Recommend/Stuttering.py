"""Stuttering"""
def main(n):
    """Stuttering"""
    print(*[i for j,i in enumerate(n) if i!=n[j-1] or not j])
main(input().split())
