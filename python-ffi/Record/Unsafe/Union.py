def unsafeUnionFn(r1, r2):
    print("Unsafe Union Fn called.")
    print(r1, r2)
    result = {**r2, **r1}
    print(result)
    return result
