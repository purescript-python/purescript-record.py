def unsafeUnionFn(r1, r2):
    print("Unsafe Union Fn called.")
    print(r1, r2)
    print(result)
    result = {**r2, **r1}
    return result
